# python-producer
This Python Kafka producer generates random events and sends them to a Kafka topic using the kafka-python library.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Clone this repository:

    ```git clone https://github.com/Romi7102/python-producer.git```

2. Install the required dependencies:
    
    ``` pip install -r requirements.txt```


## Usage

1. Ensure that you have a running Kafka cluster and a MongoDB instance.

2. Build the docker image using the dokcer file

    ```dokcer build -t python-consumer .```

3. Run the image with the following environment variables

    ```docker run -e BOOTSTRAP_SERVER=<kafka server> -e TOPIC=<kafka topic> -e MESSAGE=<message string> python-consumer```

    BOOTSTRAP_SERVER: This environment variable specifies the bootstrap servers for your Kafka cluster. These are used by the Kafka consumer to initially establish connections with the Kafka brokers in the cluster

    KAFKA_TOPIC: This environment variable specifies the Kafka topic that the Kafka consumer will subscribe to. The consumer will receive messages from this topic and process them accordingly.

    MESSAGE: This environment variable specifies the message to be sent to the Kafka broker inside the event object.

    The event object is randomly generated:
    ``` 
    event = {
                "reporterId": reporter_id,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "metricId": random.randint(1, 10),
                "metricValue": random.randint(1, 100),
                "message": message
            } 
    ```

## Running without docker

Alternatively, you can run the project locally , you would just need a way to load environment variables so the main.py file will recognize them , you can use any way you see fit.