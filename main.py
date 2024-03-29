import json
import time
import datetime
import random
from kafka import KafkaProducer
from config import BOOTSTRAP_SERVER , TOPIC  , SLEEP , JSON_FORMAT , EVENT
from utils import get_event

def main():
    producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVER,
                            value_serializer=lambda x: json.dumps(x).encode(JSON_FORMAT))

    try:
        reporter_id = EVENT["REPORTER_ID_START"]
        while True:
            event = get_event(reporter_id)
            future = producer.send(TOPIC, value=event)
            try:
                record_metadata = future.get(timeout=10) 
                print(f"Message sent successfully to topic {record_metadata.topic}, partition {record_metadata.partition}, offset {record_metadata.offset}")

            except Exception as e:
                print(f"Failed to send message: {e}")

            reporter_id += EVENT["REPORTER_ID_INCREMENT"]
            time.sleep(int(SLEEP))
    except Exception:
        producer.close()
        
if __name__ == "__main__":
    main()
