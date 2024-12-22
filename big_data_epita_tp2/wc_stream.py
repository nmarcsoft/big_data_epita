#!/usr/bin/env python3
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


sc = SparkContext(appName="PythonStreamingNetworkWordCount")
sc.setLogLevel("ERROR") # Valid log levels include: ALL, DEBUG, ERROR, FATAL, INFO, OFF, TRACE, WARN
ssc = StreamingContext(sc, 60)
lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)


counts.pprint()
ssc.start()
ssc.awaitTermination()
