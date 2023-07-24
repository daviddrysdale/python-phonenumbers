#!/usr/bin/env python

import os
import re
import sys

import requests

# Fetch the latest upstream release tag.
try:
    response = requests.get(
        "https://api.github.com/repos/google/libphonenumber/releases/latest"
    )
    response.raise_for_status()
except requests.RequestException as err:
    print("Failed to connect to the GitHub API!", file=sys.stderr)
    raise SystemExit(2) from err
upstream_tag = response.json()["tag_name"]

# Check the tag name has the expected format.
m = re.match(r"v([\d.]+)$", upstream_tag)
if not m:
    print(f"Unexpected upstream tag {upstream_tag}", file=sys.stderr)
    raise SystemExit(2)
upstream_version = m.group(1)

# Fetch the current source code version.
init_path = os.path.join(
    os.path.dirname(__file__), "..", "..", "python", "phonenumbers", "__init__.py"
)
with open(init_path, "r") as fp:
    init_contents = fp.read()
m = re.search(r'^__version__ = "([^"]+)"$', init_contents, re.MULTILINE)
if not m:
    print("Could not extract python-phonenumbers version", file=sys.stderr)
    raise SystemExit(2)
local_version = m.group(1)

# Compare versions.
if upstream_version == local_version:
    print(f"Local version {local_version} matches upstream version {upstream_version}")
    raise SystemExit(0)
else:
    print(
        f"Local version {local_version} does not match upstream version {upstream_version}"
    )
    raise SystemExit(1)
