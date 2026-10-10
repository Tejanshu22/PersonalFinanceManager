#!/usr/bin/env python3
"""Validate stable IDs and the FINNest release/roadmap manifest before CI or sync."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_RELEASES = {'V1', 'V1.5', 'V2', 'V3+', 'Future'}
ALLOWED_PRIORITIES = {'P0', 'P1', 'P2'}


def validate(features, days):
    errors = []
    ids = set()
    for index, f in enumerate(features, 1):
        tag = f'feature #{index}'
        fid = f.get('id', '')
        if not re.fullmatch(r'FIN-\d{3}', fid):
            errors.append(f'{tag}: invalid feature ID {fid!r}')
        if fid in ids:
            errors.append(f'{tag}: duplicate ID {fid}')
        ids.add(fid)
        for field in ('name', 'category', 'acceptance', 'owner'):
            if not str(f.get(field, '')).strip():
                errors.append(f'{fid}: missing {field}')
        if f.get('release') not in ALLOWED_RELEASES:
            errors.append(f'{fid}: invalid release')
        if f.get('priority') not in ALLOWED_PRIORITIES:
            errors.append(f'{fid}: invalid priority')
        day = f.get('target_day')
        if f.get('release') == 'V1' and (not isinstance(day, int) or not 1 <= day <= 85):
            errors.append(f'{fid}: V1 target_day must be between 1 and 85')
        if f.get('release') != 'V1' and day is not None:
            errors.append(f'{fid}: future target_day should remain null, until scheduled')
    day_ids = set()
    seen_day_numbers = set()
    for d in days:
        did = d.get('id', '')
        num = d.get('day')
        if not re.fullmatch(r'DAY-\d{3}', did):
            errors.append(f'bad daily ID {did!r}')
        if did in day_ids:
            errors.append(f'duplicate daily ID {did}')
        day_ids.add(did)
        if num in seen_day_numbers:
            errors.append(f'duplicate day number {num}')
        seen_day_numbers.add(num)
        if not isinstance(num, int) or not 1 <= num <= 85 or did != f'DAY-{num:03d}':
            errors.append(f'bad ID/day match {did}: {num}')
        if d.get('week') != (num - 1) // 5 + 1:
            errors.append(f'{did}: expected correct 5-day week')
        for field in ('phase', 'task', 'acceptance', 'owner'):
            if not str(d.get(field, '')).strip():
                errors.append(f'{did}: missing {field}')
    if sorted(seen_day_numbers) != list(range(1, 86)):
        errors.append('daily plan must contain exactly days 1–85')
    return errors


def main():
    features = json.loads((ROOT / 'data' / 'features.json').read_text(encoding='utf-8'))
    days = json.loads((ROOT / 'data' / 'daily_plan.json').read_text(encoding='utf-8'))
    errors = validate(features, days)
    if errors:
        print('\n'.join(f'ERROR: {e}' for e in errors))
        raise SystemExit(1)
    print(f'VALID: {len(features)} features, {len(days)} working days')


if __name__ == '__main__':
    main()
