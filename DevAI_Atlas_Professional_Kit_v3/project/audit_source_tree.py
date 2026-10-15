#!/usr/bin/env python3
"""Audits file presence only, NOT working app; default P0 only, --all for P0+P1."""
from pathlib import Path
import sys,json
args=[v for v in sys.argv[1:] if v!='--all']
root=Path(args[0] if args else '.').resolve()
manifest=json.loads((Path(__file__).parent/'REQUIRED_SOURCE_FILES.json').read_text())
all_paths=[x for group in manifest['files_by_area'].values() for x in group]
paths=[x for x in all_paths if '--all' in sys.argv or manifest['priority'].get(x)=='P0']
missing=[x for x in paths if not (root/x).is_file()]
empty=[x for x in paths if (root/x).is_file() and (root/x).stat().st_size==0]
result={'root':str(root),'phase':'ALL' if '--all' in sys.argv else 'P0','files_expected':len(paths),'missing':missing,'empty':empty,'file_integrity_pass':not missing and not empty,'runtime_tested':False}
print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(0 if result['file_integrity_pass'] else 1)
