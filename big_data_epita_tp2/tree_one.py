#!/usr/bin/env python3

import sys
from pyspark import SparkContext

if len(sys.argv) < 2:
    print("Usage: PySpark_arbre <file>", file=sys.stderr)
    sys.exit(-1)


sc = SparkContext(appName="Arbre Plus Grand")
sc.setLogLevel("ERROR")
lines = sc.textFile(sys.argv[1])


def parse_line(line):
    try:
        fields = line.split(";")
        gps = fields[0]
        hauteur_string = fields[8]
        adresse = fields[6]
        if hauteur_string.strip() == "":
            return None
        hauteur_decimal = float(hauteur_string)
        return (gps, hauteur_decimal, adresse)
    except Exception as e:
        return None

parsed_lines = lines.map(parse_line).filter(lambda x: x is not None)

largest_tree = parsed_lines.max(lambda x: x[1])

print(f"Coordonnées GPS: {largest_tree[0]}")
print(f"Taille (m): {largest_tree[1]}")
print(f"Adresse: {largest_tree[2]}")

