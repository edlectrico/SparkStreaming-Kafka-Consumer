import os
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 pyspark-shell'
'''
./spark-2.2.0-bin-hadoop2.7/bin/spark-submit
    --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0
    ~/workspaces/kafka_spark_elasticsearch/SparkStreaming-Kafka-Consumer/python-spark-streaming-consumer.py
'''

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sc.setLogLevel("WARN")

# time = 1 second
ssc = StreamingContext(sc, 1)

# kafkaStream = KafkaUtils.createStream(streamingContext, [ZK quorum], [consumer group id], [per-topic number of Kafka partitions to consume])
kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181', 'test-consumer-group', {'ping':1})

# parsed = kafkaStream.map(lambda v: json.loads(v[1]))
parsed = kafkaStream.map(lambda (k, v): json.loads(v))
print('PARSED: ', parsed)

parsed.count().map(lambda x:'Events in this batch: %s' % x).pprint()

ssc.start()
ssc.awaitTermination()
