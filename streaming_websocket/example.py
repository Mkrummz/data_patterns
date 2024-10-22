from kafka import KafkaProducer
import json
import time

# Kafka setup
producer = KafkaProducer(bootstrap_servers=['kafka-broker1:9092', 'kafka-broker2:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Sample streaming data
stream_data = {
    "device_id": "XYZ987",
    "humidity": 60.2,
    "timestamp": time.time(),
    "event": "environment_update",
    "team_tag": "Team-Alpha",
    "environment": "production"
}

# Send data to Kafka topic
producer.send('datalake-topic', stream_data)
producer.flush()
