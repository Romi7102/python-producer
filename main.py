import json
import time
import datetime
import random
import os
from kafka import KafkaProducer

def main():
    bootstrap_servers = os.environ.get("BOOTSTRAP_SERVER")
    topic = os.environ.get("TOPIC")
    message = os.environ.get("MESSAGE")
    sleep = os.environ.get("SLEEP")

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
            future = producer.send(topic, value=event)
            try:
                record_metadata = future.get(timeout=10)  # Timeout is optional, adjust as needed
                print(f"Message sent successfully to topic {record_metadata.topic}, partition {record_metadata.partition}, offset {record_metadata.offset}")

            except Exception as e:
                print(f"Failed to send message: {e}")

            reporter_id += 1
            time.sleep(int(sleep))
    except Exception:
        producer.close()
if __name__ == "__main__":
    main()
