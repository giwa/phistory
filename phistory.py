#!/usr/bin/env python
from __future__ import print_function

import sys

for line in sys.stdin:
    splited_line = line.strip().split()[1:]
    print("$", " ".join(splited_line))
