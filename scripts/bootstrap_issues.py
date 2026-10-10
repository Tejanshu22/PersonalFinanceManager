#!/usr/bin/env python3
"""Create issue-tracker tasks from catalog; default is DRY RUN.

Run from repo root:
  python scripts/bootstrap_issues.py --kind both --limit 12
  GITHUB_REPOSITORY=owner/repo GITHUB_TOKEN=... python scripts/bootstrap_issues.py --kind both --limit 12 --apply

The command is explicitly opt-in for any GitHub writes. It skips existing task IDs.
"""
import argparse
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen
import sync_progress

ROOT = Path(__file__).resolve().parents[1]


def construct(item, kind):
    if kind == 'feature':
        title = f"[{item['id']}] {item['name']}"
        body = (
            f"## Scope\n{item['name']}\n\n**Release:** {item['release']}  "
            f"\n**Priority:** {item['priority']}  \n**Target working day:** {item['target_day'] or 'Unscheduled'}"
            f"\n\n## Acceptance criteria\n{item['acceptance']}"
        )
    else:
        title = f"[{item['id']}] Day {item['day']}: {item['task']}"
        body = (f"## Day {item['day']} (week {item['week']})\n{item['task']}\n\n"
                f"**Phase:** {item['phase']}\n\n## Acceptance\n{item['acceptance']}")
    body += ("\n\n## Verification gate\n- [ ] Implementation/outputs reviewed\n"
             "- [ ] Acceptance tested\n- [ ] Privacy/security/tax checks completed where relevant\n"
             "- [ ] Documentation updated\n- [ ] Reviewer approves verification\n\n"
             "After review, add the `verified` label AND close the issue. Only then will the tracker check it off.\n")
    return {'title': title, 'body': body}


def create_one(repo, token, payload):
    data = json.dumps(payload).encode('utf-8')
    request = Request(f'https://api.github.com/repos/{repo}/issues',data=data,method='POST',headers={
        'Accept':'application/vnd.github+json', 'Authorization':f'Bearer {token}',
        'X-GitHub-Api-Version':'2022-11-28','Content-Type':'application/json',
        'User-Agent':'finance-platform-issue-bootstrap'})
    with urlopen(request, timeout=30) as res:
        return json.load(res)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--kind', choices=('features','days','both'), default='both')
    p.add_argument('--release', choices=('V1','V1.5','V2','V3+','Future','all'), default='V1')
    p.add_argument('--limit', type=int, default=12, help='Maximum new issues per run (1–50)')
    p.add_argument('--apply', action='store_true', help='Actually create GitHub issues; without this only previews')
    args=p.parse_args()
    if not 1 <= args.limit <= 50: p.error('--limit must be between 1 and 50')
    f=json.loads((ROOT/'data/features.json').read_text(encoding='utf-8'))
    d=json.loads((ROOT/'data/daily_plan.json').read_text(encoding='utf-8'))
    tasks=[]
    if args.kind in ('features','both'):
        tasks += [(x,'feature') for x in f if args.release=='all' or x['release']==args.release]
    if args.kind in ('days','both'):
        tasks += [(x,'day') for x in d]
    # Bootstrap the nearest daily issues alongside their related features.
    # Otherwise a small --limit batch could contain only feature issues,
    # leaving DAY-001 absent when development begins.
    if args.kind == 'both':
        tasks.sort(key=lambda pair: (
            pair[0]['day'] if pair[1]=='day' else (pair[0]['target_day'] or 999),
            0 if pair[1]=='day' else 1, pair[0]['id']))
    repo=os.environ.get('GITHUB_REPOSITORY','')
    token=os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
    existing = sync_progress.map_issues(sync_progress.github_issues(repo, token)) if args.apply else {}
    missing=[(item,kind) for item,kind in tasks if item['id'] not in existing][:args.limit]
    print(('APPLY' if args.apply else 'DRY RUN'),f'{len(missing)} issues; release={args.release}; kind={args.kind}')
    for item,kind in missing:
        payload=construct(item,kind)
        if args.apply:
            created=create_one(repo, token, payload)
            print('Created:',created['html_url'])
        else:
            print('Would create:',payload['title'])
    if not args.apply: print('No GitHub API write occurred. Use --apply explicitly after configuring a repository.')


if __name__=='__main__':main()
