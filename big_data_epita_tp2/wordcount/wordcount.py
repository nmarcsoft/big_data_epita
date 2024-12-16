#!/usr/bin/env python3

import sys
from pyspark import SparkContext

if len(sys.argv) < 3:
    print('Usage: PySpark_wc <file> <min_occurrences>', file=sys.stderr)
    sys.exit(-1)

limit = sys.argv[2]
limit = int(limit)

sc = SparkContext(appName='Spark Count')
sc.setLogLevel('ERROR')
lines = sc.textFile(sys.argv[1])
counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(lambda v1, v2: v1 + v2)
if (len(sys.argv) == 3):
    filtered_counts = counts.filter(lambda x: x[1] >= limit)
    filtered_counts.saveAsTextFile('sortie')
else:
    counts.saveAsTextFile('sortie')

sc.stop()
