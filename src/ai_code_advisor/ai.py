##########################################################################
# Copyright 2025 Vladislav Riabov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##########################################################################

import argparse
import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from rich import print

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def run(cmd):
    return subprocess.check_output(cmd, text=True, errors="replace")


def git_context():
    parts = []
    try:
        parts.append("=== git status ===\n" + run(["git", "status", "--porcelain=v1"]))
    except Exception:
        parts.append("=== git status ===\n(n/a)")
    try:
        parts.append("=== recent commits ===\n" + run(["git", "log", "-5", "--oneline"]))
    except Exception:
        pass
    return "\n\n".join(parts)


def read_file(path, max_chars=20000):
    return Path(path).read_text(encoding="utf-8", errors="replace")[:max_chars]


def call_llm(system, user):
    resp = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return resp.choices[0].message.content


def explain(path):
    code = read_file(path)
    prompt = f"""Explain this file for a junior teammate.

{git_context()}

File: {path}
```text
{code}"""
    
    print(call_llm("You are a senior software graphics engineer.", prompt))