#!/usr/bin/env python3
"""Rebrand visible copy without changing stable internal IDs.

Usage: python scripts/rebrand.py NewDisplayName --tagline 'Your tagline'
Then commit config change, which triggers GitHub to regenerate catalog/progress.
"""
import argparse
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('name')
p.add_argument('--tagline')
args=p.parse_args()
name=args.name.strip()
if not name or len(name)>50 or '\n' in name: raise SystemExit('Display name must be 1–50 characters, one line')
f=ROOT/'config'/'brand.json';data=json.loads(f.read_text(encoding='utf-8'))
old=data['display_name'];data['display_name']=name
if args.tagline: data['tagline']=args.tagline.strip()
data['brand_status']='working-name-unverified'
f.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Curated human-authored files only; generated documents change at next sync.
for rel in ['README.md','AGENTS.md','docs/BRANDING.md','docs/ARCHITECTURE.md','docs/SECURITY.md','docs/TAX_POLICY.md','docs/GITHUB_AUTOMATION.md','docs/REQUIREMENTS.md','docs/RELEASE_CHECKLIST.md','docs/MONETIZATION.md','docs/SCREENS.md']:
    target=ROOT/rel
    if target.exists():target.write_text(target.read_text(encoding='utf-8').replace(old,name),encoding='utf-8')
print(f'Brand updated: {old} -> {name}. Stable IDs unchanged; commit changes to rebuild generated docs.')
