#!/usr/bin/env python3

import sys

excluded_categories = {"Customer Electronics", "Toys"}

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    if len(fields) == 6:
        category = fields[3]
        cost = fields[4]
        if category not in excluded_categories:
            try:
                cost = float(cost)
                print(f'filtered_category_total\t{category}\t{cost}')
            except ValueError:
                continue
