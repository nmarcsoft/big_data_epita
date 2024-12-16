#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    if len(fields) == 6:
        cost = fields[4]
        try:
            cost = float(cost)
            print(f'overall_total\tall\t{cost}')
        except ValueError:
            continue
