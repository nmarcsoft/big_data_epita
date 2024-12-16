#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    if len(fields) == 6:
        category = fields[3]
        cost = fields[4]
        try:
            cost = float(cost)
            print(f'category_total\t{category}\t{cost}')
        except ValueError:
            continue
