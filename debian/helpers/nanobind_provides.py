#!/usr/bin/python3
import re
import sys


data = {}

with open("debian/versions", "r") as f:
    for line in f:
        mo = re.match(r"([a-z0-9-]+)\s+(.*)", line.strip())
        if mo:
            data[mo.group(1)] = mo.group(2)

assert "abi" in data
assert "api-min-version" in data

with open("docs/changelog.rst", "r") as f:
    for line in f:
        mo = re.match(r"\* ABI version (\d+)", line.strip(), re.I)
        if mo:
            if mo.group(1) != data["abi"]:
                print(f"ABI mismatch: Expected {data['abi']}, got {mo.group(1)}")
                sys.exit(1)
            break
    else:
        print("Unable to detect current ABI version in docs/changelog.rst")
        sys.exit(1)

with open("debian/python3-nanobind.substvars", "a") as f:
    f.write(f"nanobind:Provides=python3-nanobind-abi{data['abi']}\n")

with open("debian/python3-nanobind.pydist", "w") as f:
    f.write(f"nanobind python3-nanobind (>= {data['api-min-version']}), python3-nanobind-abi{data['abi']}\n")




