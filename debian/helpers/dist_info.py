#!/usr/bin/python3
import argparse
import re
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="package name")
parser.add_argument("--version", help="package version")
parser.add_argument("--add-metadata", metavar="LINE", action="append", default=[], help="add LINE to metadata")
parser.add_argument("--output-dir", metavar="DIR", type=Path, default=Path("."), help="write .dist-info to DIR")

args = parser.parse_args()

distinfo_name = re.sub(r"[-_.]+", "_", args.name).lower()
distinfo_version = args.version.split("+", 1)[0]

distinfo_dir = args.output_dir / f"{distinfo_name}-{distinfo_version}.dist-info"

distinfo_dir.mkdir(parents=True, exist_ok=True)
extras = "\n".join(args.add_metadata)

with open(distinfo_dir / "METADATA", "w") as f:
    f.write(f"""\
Metadata-Version: 2.1
Name: {args.name}
Version: {args.version}
{extras}
""")
   
with open(distinfo_dir / "INSTALLER", "w") as f:
    f.write("Debian")

