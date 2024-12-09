#!/usr/bin/env python3

import sys
# reading entire line from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    # split the line into words
    words = line.split()
    for word in words:
        word = word.lower()
        clean_text = ''.join(char for char in word if char.isalnum())
        if (clean_text != ""):
            print('{}\t{}'.format(clean_text, 1))
