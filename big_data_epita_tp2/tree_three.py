#!/usr/bin/env python3

import sys
from pyspark import SparkContext

if len(sys.argv) < 2:
    print("Usage: PySpark_especes <file>", file=sys.stderr)
    sys.exit(-1)

input_file = sys.argv[1]

sc = SparkContext(appName="Espèces par Genre")
sc.setLogLevel("ERROR")

lines = sc.textFile(input_file)


def parse_line(line):
    try:
        fields = line.split(";")
        genre = fields[12].strip()
        espece = fields[13].strip()
        if genre and espece:
            return (genre, espece)
        return None
    except Exception as e:
        return None


parsed_lines = lines.map(parse_line).filter(lambda x: x is not None)
grouped_by_genre = parsed_lines.groupByKey()
sorted_by_genre = grouped_by_genre.sortByKey()
results = sorted_by_genre.collect()

for genre, especes in results:
    especes_list = sorted(list(set(especes)))
    print(f"Genre: {genre}")
    for espece in especes_list:
        print(f"  - {espece}")
