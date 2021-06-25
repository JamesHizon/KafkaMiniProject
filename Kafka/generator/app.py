# Generator Python Script

import os
import json
from time import sleep
from kafka import KafkaProducer
from transactions import create_random_transaction

# Grab URL of broker. --> Producers will use this URL to bootstrap connection to Kafka cluster.
KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = float(os.environ.get("TRANSACTIONS_PER_SECOND"))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND

if __name__ == "__main__":
    # Instantiate actual producer --> Exposes a simple API to send messages to a Kafka topic
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL,
                             value_serializer=lambda value: json.dumps(value).encode())  # Encode all values as JSON

    # Next Step: What do we do with the producer? --> Well, we can use it to send messages.

    # Now, the aim of the transaction generator is to fake an infinite stream of transactions flowing
    # through our system. So, we will simply run an infinite loop which produces these messages to a topic.
    while True:
        transaction = create_random_transaction()
        producer.send(TRANSACTIONS_TOPIC, value=transaction)  # Use producer to send message
        print(transaction)  # Debug
        sleep(SLEEP_TIME)






