#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    if len(fields) == 6:
        store = fields[2]
        cost = fields[4]
        try:
            cost = float(cost)
            print(f'store_total\t{store}\t{cost}')
        except ValueError:
            continue
