import json
from pathlib import Path

import test_project

PACKAGE = "test_project"
PACKAGE_DIR = Path(test_project.__file__).parent
MANIFEST_FILE = PACKAGE_DIR / "__FRACTAL_MANIFEST__.json"
with MANIFEST_FILE.open("r") as f:
    MANIFEST = json.load(f)
    TASK_LIST = MANIFEST["task_list"]
