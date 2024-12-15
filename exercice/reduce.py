#!/usr/bin/env python3

import sys

current_key = None
current_subkey = None
current_total = 0
current_count = 0

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')
    if len(parts) < 3:
        continue

    key, subkey, value = parts[0], parts[1], parts[2]
    try:
        value = float(value)
    except ValueError:
        continue

    composite_key = f"{key}_{subkey}"

    if current_key == composite_key:
        current_total += value
        if key == 'overall_total':
            current_count += 1
    else:
        if current_key:
            if current_key.startswith('overall_total'):
                print(f'{current_key}\t{current_total}\t{current_count}')
            else:
                print(f'{current_key}\t{current_total}')
        current_key = composite_key
        current_total = value
        current_count = 1 if key == 'overall_total' else 0

if current_key:
    if current_key.startswith('overall_total'):
        print(f'{current_key}\t{current_total}\t{current_count}')
    else:
        print(f'{current_key}\t{current_total}')

