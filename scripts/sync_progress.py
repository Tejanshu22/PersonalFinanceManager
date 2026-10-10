#!/usr/bin/env python3
"""Keep FINNest generated tracker files consistent with GitHub Issues.

Status is truthfully gated:
- Planned: no corresponding issue or open issue without workflow labels
- In Progress: open issue labeled in-progress
- Blocked: open issue labeled blocked
- Needs Review: closed issue missing verified label
- Verified Done: closed issue labeled verified AND NOT canceled

This script never marks work complete because a file exists or AI said so.
The GitHub Actions job invokes the generator and commits its generated files.
The script uses only Python stdlib. Excel output is built by a separate Node helper.
"""
import argparse
import csv
import io
import json
import os
from pathlib import Path
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError

ROOT=Path(__file__).resolve().parents[1]
ID_RE=re.compile(r'\b(?:FIN|DAY)-\d{3}\b')
PRIORITIES={'P0':0,'P1':1,'P2':2}
STATES=('Planned','In Progress','Blocked','Needs Review','Verified Done')

def github_issues(repo, token):
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repo):
        raise ValueError('GITHUB_REPOSITORY must be owner/repo')
    if not token: raise ValueError('GITHUB_TOKEN not configured for live sync')
    out=[]
    for page in range(1, 50):
        url=f'https://api.github.com/repos/{repo}/issues?state=all&per_page=100&page={page}'
        req=Request(url,headers={
          'Accept':'application/vnd.github+json',
          'Authorization':f'Bearer {token}',
          'X-GitHub-Api-Version':'2022-11-28',
          'User-Agent':'FINNest-progress-tracker'
        })
        try:
            with urlopen(req,timeout=30) as res:
                batch=json.load(res)
        except HTTPError as e:
            raise RuntimeError(f'GitHub API request failed: HTTP {e.code}, repo={repo}') from e
        page_count=len(batch)
        batch=[v for v in batch if not v.get('pull_request')]
        out.extend(batch)
        if page_count<100:break
    else:
        raise RuntimeError('More than 4900 issues: add pagination support')
    return out

def parse_issue_title(issue):
    # Match an ID at beginning of title e.g. [FIN-031] or FIN-031:
    title=issue.get('title','').strip()
    m=re.match(r'^\[?((?:FIN|DAY)-\d{3})\]?(?=\s|:|\b)',title)
    return m.group(1) if m else None

def labels(issue):
    return {((v.get('name') if isinstance(v,dict) else v) or '').strip().lower() for v in issue.get('labels', [])}

def issue_state(issue):
    tags=labels(issue)
    if 'canceled' in tags or 'wontfix' in tags: return 'Blocked'
    if issue.get('state')=='closed':
        return 'Verified Done' if 'verified' in tags else 'Needs Review'
    if 'blocked' in tags:return 'Blocked'
    if 'in-progress' in tags:return 'In Progress'
    return 'Planned'

def map_issues(issues):
    index={}
    for issue in issues:
        fid=parse_issue_title(issue)
        if not fid:continue
        if fid in index:raise ValueError(f'Duplicate GitHub issue IDs: {fid}. Resolve duplicates before syncing.')
        index[fid]=issue
    return index

def status_for(item, index):
    issue=index.get(item['id'])
    return issue_state(issue) if issue else 'Planned'

def write_csv(path,headers,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    # Excel-compatible, encoded UTF-8 with BOM for ₹ and checkboxes.
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f);w.writerow(headers);w.writerows(rows)

def markdown_table(headers,rows):
    def esc(x):return str(x).replace('|','\\|').replace('\n',' ')
    return '| '+' | '.join(map(esc,headers))+' |\n'+'| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(map(esc,row))+' |\n' for row in rows)

def generate(features,days,issues,now=None):
    now=now or datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    brand=json.loads((ROOT/'config'/'brand.json').read_text())
    name=brand['display_name']
    index=map_issues(issues)
    feature_rows=[]; daily_rows=[]
    for f in features:
        s=status_for(f,index); gh=index.get(f['id'],{})
        feature_rows.append({**f,'status':s,'done':'☑' if s=='Verified Done' else '☐', 'issue':gh.get('html_url','')})
    for d in days:
        s=status_for(d,index);gh=index.get(d['id'],{})
        daily_rows.append({**d,'status':s,'done':'☑' if s=='Verified Done' else '☐','issue':gh.get('html_url','')})
    total=len(feature_rows)
    stat=Counter(f['status'] for f in feature_rows)
    v1=[f for f in feature_rows if f['release']=='V1']
    v1_done=sum(f['status']=='Verified Done' for f in v1)
    day_done=sum(d['status']=='Verified Done' for d in daily_rows)
    write_csv(ROOT/'tracking'/'Feature_Checklist.csv',
       ['Done','ID','Release','Category','Feature','Priority','Target Day','Status','Acceptance','Owner','GitHub Issue'],
       [[v['done'],v['id'],v['release'],v['category'],v['name'],v['priority'],v['target_day'] or '',v['status'],v['acceptance'],v['owner'],v['issue']] for v in feature_rows])
    write_csv(ROOT/'tracking'/'Daily_Checklist.csv',
       ['Done','Day','ID','Week','Phase','Task','Status','Acceptance','Owner','GitHub Issue'],
       [[d['done'],d['day'],d['id'],d['week'],d['phase'],d['task'],d['status'],d['acceptance'],d['owner'],d['issue']] for d in daily_rows])
    counts=Counter(f['release'] for f in feature_rows)
    lines=[f'# {name} — Live progress', '', '> AUTO-GENERATED from `data/features.json`, `data/daily_plan.json` and GitHub Issues. Do not hand-edit this file.', '',
           f'**Synced:** {now}  ',f'**Verified features:** {stat["Verified Done"]}/{total} ({stat["Verified Done"]/total:.1%})  ',
           f'**V1 verified:** {v1_done}/{len(v1)} ({v1_done/len(v1):.1%})  ',
           f'**Verified daily tasks:** {day_done}/{len(days)}', '',
           '## Feature status overview', '',
           markdown_table(['Status','Features'],[[k,stat[k]] for k in STATES]),'',
           '## Release breakdown','',
           markdown_table(['Release','Total','Verified','Progress'],[[release,counts[release],sum(x['release']==release and x['status']=='Verified Done' for x in feature_rows),f"{(sum(x['release']==release and x['status']=='Verified Done' for x in feature_rows)/counts[release]) if counts[release] else 0:.1%}"] for release in ['V1','V1.5','V2','V3+','Future']]),'',
           '## Verified work', '',]
    done_items=[f for f in feature_rows if f['status']=='Verified Done']
    if done_items: lines += [f"- **{f['id']}** {f['name']}"+(f" ([issue]({f['issue']}))" if f['issue'] else '') for f in done_items]
    else: lines.append('_No work has been verified yet. This is the expected initial state._')
    lines += ['', '## Needs review or blocked', '']
    urgent=[f for f in feature_rows if f['status'] in ('Needs Review','Blocked')]
    if urgent:lines += [f"- **{f['id']}** · {f['status']} · {f['name']}" for f in urgent]
    else:lines.append('_None._')
    lines += ['', '## How completion works', '',
      '- **Planned:** no matching issue, or an open issue without progress labels.',
      '- **In Progress:** open issue with `in-progress` label.',
      '- **Blocked:** open issue with `blocked` label.',
      '- **Needs Review:** closed issue without `verified` label.',
      '- **Verified Done:** issue closed **and** carrying the `verified` label; not `canceled` or `wontfix`.',
      '- Never add the `verified` label until acceptance criteria/tests and reviewer sign-off are satisfied.',
      '- Technical completion and professional tax/security launch approval are separate gates.', '']
    (ROOT/'docs'/'PROGRESS.md').write_text('\n'.join(lines),encoding='utf-8')
    f_lines=[f'# {name} — Feature catalog', '', '> AUTO-GENERATED; edit `data/features.json` instead of editing this document.', '',
       f'**Catalog:** {total} atomic features across V1, V1.5, V2, V3+ and Future.', '',]
    cats=list(dict.fromkeys((f['release'], f['category']) for f in feature_rows))
    for release,cat in cats:
        f_lines += [f'## {release} — {cat}', '',
          markdown_table(['Check','ID','Feature','Status','Acceptance'],[[f['done'],f['id'],f['name'],f['status'],f['acceptance']] for f in feature_rows if f['release']==release and f['category']==cat]),'']
    (ROOT/'docs'/'FEATURE_CATALOG.md').write_text('\n'.join(f_lines),encoding='utf-8')
    # This log records only issue state and evidence links — not claims about code correctness.
    completion = [f'# {name} — Verified completion log', '',
       '> AUTO-GENERATED from GitHub Issues; verification label + closed state required.', '',
       '| ID | Work item | Verified/closed UTC | Issue |',
       '| --- | --- | --- | --- |']
    verified_entries = []
    for item in feature_rows + daily_rows:
        if item['status'] != 'Verified Done':
            continue
        issue = index[item['id']]
        title = (item.get('name') or item.get('task') or '').replace('|','\\|')
        date = str(issue.get('closed_at') or 'Date not available')
        url = issue.get('html_url','')
        link = f'[View]({url})' if url else '—'
        verified_entries.append((date, f"| {item['id']} | {title} | {date} | {link} |"))
    for _, line in sorted(verified_entries, reverse=True):
        completion.append(line)
    if not verified_entries:
        completion += ['| — | No verified completions yet | — | — |']
    (ROOT/'docs'/'COMPLETION_LOG.md').write_text('\n'.join(completion)+'\n',encoding='utf-8')

    d_lines=[f'# {name} — 85-day plan', '', '> AUTO-GENERATED. Edit `data/daily_plan.json` to change the planned work.', '',
             '**Assumption:** 6–8 focused hours/day, five working days/week. This is a planning estimate, not a release guarantee.', '']
    for week in sorted({d['week'] for d in daily_rows}):
        ds=[d for d in daily_rows if d['week']==week]
        d_lines += [f'## Week {week} — {ds[0]["phase"]}','',markdown_table(['Done','Day','Task','Status','Issue'],[[d['done'],d['day'],d['task'],d['status'], f"[GitHub]({d['issue']})" if d['issue'] else '—'] for d in ds]),'']
    (ROOT/'docs'/'ROADMAP.md').write_text('\n'.join(d_lines),encoding='utf-8')
    # Machine readable output powers any future dashboard; avoid timestamps in files to suppress no-op churn?
    (ROOT/'tracking'/'status.json').write_text(json.dumps({'synced_at':now,'name':name,'counts':stat,'v1_verified':v1_done,'v1_total':len(v1),'days_verified':day_done,'days_total':len(days)},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return feature_rows,daily_rows

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--issues-json',help='Use a local JSON list of GitHub-like issues (offline testing)')
    parser.add_argument('--no-github',action='store_true',help='Initialize with planned status; intentionally ignore remote issues')
    parser.add_argument('--timestamp',help='Deterministic timestamp for tests')
    args=parser.parse_args()
    features=json.loads((ROOT/'data'/'features.json').read_text(encoding='utf-8'))
    days=json.loads((ROOT/'data'/'daily_plan.json').read_text(encoding='utf-8'))
    if args.issues_json:issues=json.loads(Path(args.issues_json).read_text(encoding='utf-8'))
    elif args.no_github:issues=[]
    elif os.environ.get('GITHUB_REPOSITORY'):
        issues=github_issues(os.environ['GITHUB_REPOSITORY'],os.environ.get('GITHUB_TOKEN'))
    else:
        parser.error('Live sync requires GITHUB_REPOSITORY and GITHUB_TOKEN; use --no-github explicitly to initialize a new tracker.')
    feature_rows,daily_rows=generate(features,days,issues,args.timestamp)
    print(f'SYNC OK: {len(feature_rows)} features, {len(daily_rows)} daily tasks, verified features={sum(v["status"]=="Verified Done" for v in feature_rows)}')

if __name__=='__main__':main()
