#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    if len(fields) == 6:
        store = fields[2]
        payment = fields[5]
        cost = fields[4]
        try:
            cost = float(cost)
            print(f'payment_store\t{store},{payment}\t{cost}')
        except ValueError:
            continue
