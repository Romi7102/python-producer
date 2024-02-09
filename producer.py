from kafka import KafkaProducer
import time
import datetime
import random
import json

#! Pull from YAML config file
bootstrap_servers = 'localhost:9092'
topic = 'pyTest'
message = "Hello from python producer!"

producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

try:
    reporter_id = 1
    while True:
        event = {
            "reporterId": reporter_id,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "metricId": random.randint(1, 10),
            "metricValue": random.randint(1, 100),
            "message": message
        }

        producer.send(topic, value=event)
        print("Message sent successfully to topic:", topic)

        reporter_id += 1
        time.sleep(1)

except KeyboardInterrupt:
    producer.close()
