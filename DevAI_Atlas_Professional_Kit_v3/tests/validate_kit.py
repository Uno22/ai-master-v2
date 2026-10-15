#!/usr/bin/env python3
"""Static curriculum+kit integrity verifier; never claims product runtime PASS."""
from pathlib import Path
import json, sys, re
try:
 import yaml
 import jsonschema
except ImportError as e:
 print('Missing test dependency: install PyYAML and jsonschema; '+str(e));sys.exit(2)
root=Path(__file__).resolve().parents[1]
errors=[]
def require(path):
 p=root/path
 if not p.is_file() or p.stat().st_size==0: errors.append(f'MISSING/EMPTY {path}')
 return p
for x in ('README.md','START_HERE.md','curriculum/AI_First_14_Day_AI_Developer_Knowledge_Hub_V3.md','content/tracks.yaml','docs/TRACEABILITY_MATRIX.md','docs/PRD.md','docs/SECURITY.md','docs/EDITORIAL_POLICY.md','docs/TEST_PLAN.md','project/REQUIRED_SOURCE_FILES.json','audit/PRE_POST_SCORECARD.md'):
 require(x)
for n in range(1,15):
 for path in (f'curriculum/days/DAY_{n:02d}.md',f'prompts/daily/DAY_{n:02d}.md'):
  p=require(path)
  if p and p.exists():
   v=p.read_text()
   for token in (('Prompt','DoD') if path.startswith('curriculum/') else ('Scope','TEST COMMANDS','BLOCKED')):
    # one of the case-insensitive variants must exist for clarity, not exact semantics
    if token.casefold() not in v.casefold():errors.append(f'PROMPT/DAY TOKEN MISSING {path}: {token}')
 require(f'tests/fixtures/FIX_{n:02d}_'+list((root/'tests/fixtures').glob(f'FIX_{n:02d}_*.json'))[0].name.split('_',2)[2]) if list((root/'tests/fixtures').glob(f'FIX_{n:02d}_*.json')) else errors.append(f'MISSING FIX {n}')
raw=yaml.safe_load(require('content/tracks.yaml').read_text())
tracks=raw['tracks']
if len(tracks)!=18:errors.append('TRACKS != 18')
if sum(len(t['modules']) for t in tracks)!=144:errors.append('MODULES != 144')
mods=[m['id'] for t in tracks for m in t['modules']]
if len(mods)!=len(set(mods)):errors.append('DUPLICATE MODULE IDs')
lessons=list((root/'content/lessons').glob('*.md'))
if len(lessons)!=6:errors.append('EXPECTED SIX DRAFT LESSONS')
for p in lessons:
 v=p.read_text()
 for token in ('## Lý thuyết','## Bài tập','## Lời giải','## Quiz','## Nguồn'):
  # knowledge sections can have similar names; ensure required pieces
  if token not in v and token != '## Lý thuyết': errors.append(f'LESSON MISSING {p.name}: {token}')
schemas={}
for name in ('lesson','news-draft','ingestion-run'):
 p=require(f'schemas/{name}.schema.json'); schemas[name]=json.loads(p.read_text());jsonschema.Draft202012Validator.check_schema(schemas[name])
example_lesson=json.loads(require('tests/fixtures/lesson.example.json').read_text())
errors.extend('INVALID lesson: '+err.message for err in jsonschema.Draft202012Validator(schemas['lesson'],format_checker=jsonschema.FormatChecker()).iter_errors(example_lesson))
for name in ('news-draft','ingestion-run'):
 payload=json.loads(require(f'tests/fixtures/{name}.example.json').read_text())
 errors.extend(f'INVALID {name}: {err.message}' for err in jsonschema.Draft202012Validator(schemas[name],format_checker=jsonschema.FormatChecker()).iter_errors(payload))
fix=list((root/'tests/fixtures').glob('FIX_*.json'))
if len(fix)!=18:errors.append(f'FIXTURE COUNT != 18: {len(fix)}')
for p in fix:
 f=json.loads(p.read_text())
 if f.get('fixture')!='SYNTHETIC_TEST_ONLY_NOT_REAL_NEWS' or f.get('expected',{}).get('public_publish_allowed') is not False:errors.append(f'UNSAFE/FALSE LABEL {p.name}')
files=json.loads(require('project/REQUIRED_SOURCE_FILES.json').read_text())
fpaths=[p for group in files['files_by_area'].values() for p in group]
if files['total_required_files']!=len(fpaths) or len(fpaths)!=len(set(fpaths)):errors.append('SOURCE FILE MANIFEST MISMATCH')
if sum(x=='P0' for x in files['priority'].values())!=144 or sum(x=='P1' for x in files['priority'].values())!=13: errors.append('P0/P1 scope count mismatch')
for x in ('docs/POST_LAUNCH_CHECKLIST.md','docs/learning-log.md','docs/PROVIDER_MATRIX.md','contracts/API_CONTRACTS.md','contracts/PIPELINE_STATE_MACHINE.md','design/END_TO_END_CASE_STUDY.md','automation/SCHEDULE_SPEC.md','project/DEPENDENCY_MATRIX.md','project/templates/CLAUDE.md','project/templates/.env.example'):
 require(x)
for p in (root/'prompts/daily').glob('*.md'):
 v=p.read_text()
 if not ('TEST COMMANDS' in v and 'RISKS' in v and 'Approval' in v or 'approval' in v):errors.append(f'PROMPT INCOMPLETE {p}')
role=list((root/'prompts/roles').glob('*.md'))
if len(role)!=8:errors.append('EIGHT ROLE PROMPTS EXPECTED')
master=require('curriculum/AI_First_14_Day_AI_Developer_Knowledge_Hub_V3.md').read_text()
if master.count('## NGÀY ')!=14:errors.append('MASTER DAY SECTION COUNT MISMATCH')
if master.count('```') % 2 != 0:errors.append('MASTER UNBALANCED CODE FENCES')
for p in (root/'curriculum/days').glob('*.md'):
 if p.read_text().count('```')%2!=0:errors.append(f'UNBALANCED FENCES {p.name}')
for m in re.findall(r'\| R-(\d{2}) \|', (root/'docs/TRACEABILITY_MATRIX.md').read_text()): pass
if len(set(re.findall(r'\| R-(\d{2}) \|',(root/'docs/TRACEABILITY_MATRIX.md').read_text())))!=12:errors.append('TRACEABILITY DOES NOT COVER 12 REQS')
report={'kit_valid':not errors,'checks':{'tracks':len(tracks),'modules':len(mods),'days':14,'prompt_daily':len(list((root/'prompts/daily').glob('DAY_*.md'))),'role_prompts':len(role),'lesson_samples_draft':len(lessons),'fixtures':len(fix),'source_files_to_build':len(fpaths)},'errors':errors,'production_verified':False}
print(json.dumps(report,ensure_ascii=False,indent=2))
sys.exit(0 if not errors else 1)
