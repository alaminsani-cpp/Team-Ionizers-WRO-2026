#!/usr/bin/env python3
"""Audit WRO documentation/evidence presence without inventing compliance.

Run from this repository: python tools/check_submission.py
"""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
checks = []

def check(name, condition, explanation):
    checks.append(bool(condition))
    print(f'{"PASS" if condition else "MISSING"}: {name} — {explanation}')

readme = (root/'README.md').read_text(encoding='utf-8')
check('README >= 5000 characters', len(readme)>=5000, f'{len(readme)} characters')
check('Engineering Journal PDF', (root/'docs/Engineering_Journal.pdf').is_file(), 'printable journal')
photos=['front','back','left','right','top','bottom']
for side in photos:
    check('Vehicle photo: '+side, any((root/'v-photos'/f'{side}{ext}').is_file() for ext in ['.jpg','.jpeg','.png','.webp']), 'photo file')
check('Team photo', any(x.suffix.lower() in {'.jpg','.png','.jpeg','.webp'} for x in (root/'t-photos').iterdir()), 'one photo')
for name in ['raspberry_pi','esp32']:
    p=root/'src'/name
    source=[x for x in p.rglob('*') if x.suffix.lower() in {'.py','.cpp','.c','.h','.hpp','.ino'} and x.is_file()]
    check('Actual code in src/'+name, len(source)>0, f'{len(source)} source files found; confirm they are genuine')
media=(root/'video/README.md').read_text(encoding='utf-8')
check('Open and Obstacle YouTube URLs', 'youtube.com/watch' in media or 'youtu.be/' in media, 'manually verify two distinct real links and each 30 s')
check('Actual CAD/print file', any(x.suffix.lower() in {'.stl','.step','.stp','.3mf','.f3d','.fcstd','.dxf'} for x in (root/'models').iterdir()), 'if custom parts were used')
check('Confirmed pinmap', 'TO_VERIFY' not in (root/'schemes/pinmap.csv').read_text(encoding='utf-8'), 'requires actual net entries')
check('Confirmed robot profile', 'TO VERIFY' not in (root/'ROBOT_PROFILE.md').read_text(encoding='utf-8'), 'replace all missing fields')
try:
    res=subprocess.run(['git','-C',str(root),'log','--format=%ad %h %s','--date=short'],capture_output=True,text=True)
    if res.returncode==0:
        history=[line for line in res.stdout.splitlines() if line]
        check('At least 3 actual Git commits',len(history)>=3,f'{len(history)} present; independently check WRO chronological milestones')
        if history: print('Recent commits:\n'+'\n'.join(history[:5]))
    else:
        check('Actual Git history',False,'ZIP does not include .git history; use existing genuine project history')
except FileNotFoundError:
    check('Actual Git history',False,'Git is not installed on this machine')
print(f'\nAUDIT: {sum(checks)}/{len(checks)} mechanical checks passed. A pass is not WRO approval.')
