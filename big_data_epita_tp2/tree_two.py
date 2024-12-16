#!/usr/bin/env python3

import sys
from pyspark import SparkContext

if len(sys.argv) < 2:
    print("Usage: PySpark_arbre <file>", file=sys.stderr)
    sys.exit(-1)

input_file = sys.argv[1]

sc = SparkContext(appName="Arbre Plus Grand par Arrondissement")
sc.setLogLevel("ERROR")

lines = sc.textFile(input_file)

def parse_line(line):
    try:
        fields = line.split(";")
        gps = fields[0] 
        circonference_string = fields[7]
        arrondissement = fields[3]
        if circonference_string.strip() == "":
            return None
        circonference_decimal = float(circonference_string)
        return (arrondissement, (gps, circonference_decimal))
    except Exception as e:
        return None


parsed_lines = lines.map(parse_line).filter(lambda x: x is not None)
largest_trees_by_arrondissement = parsed_lines.reduceByKey(lambda x, y: x if x[1] > y[1] else y)


results = largest_trees_by_arrondissement.collect()

for arrondissement, (gps, circonference) in results:
    print(f"Arrondissement: {arrondissement}, Coordonnées GPS: {gps}, Circonférence (cm): {circonference}")

