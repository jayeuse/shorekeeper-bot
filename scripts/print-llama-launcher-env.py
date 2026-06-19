#!/usr/bin/env python3

import shlex
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "backend" / "brain"))

from core.config import LLAMA_LAUNCHER_SETTINGS  # noqa: E402


for key, value in LLAMA_LAUNCHER_SETTINGS.items():
    print(f"{key}={shlex.quote(str(value))}")
