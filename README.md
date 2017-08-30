# SparkStreaming-Kafka-Consumer
Consuming Kafka events from several topics in Python.

The python-spark-streaming-consumer Python class basically reads from the 'ping' topic generated by a Kafka Producer. This Kafka Producer can be seen and run in [here](https://github.com/edlectrico/Python-Kafka-Fake-Log-Producer).

## Run the Spark Streaming Job:
Open a new terminal and type the following:
```
<SPARK_PATH>/bin/spark-submit
    --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0
    <PATH_TO_REPO>/SparkStreaming-Kafka-Consumer/python-spark-streaming-consumer.py
```

## Next steps:
We aim to enable real time analytics through Kibana. To do so, we are going to write the events captured by Spark Streaming into elasticsearch. Elasticsearch officially [supports HDFS](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/spark.html) and Spark.
