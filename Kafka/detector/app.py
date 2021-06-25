# Detector Python Script

# Fraud Detector Details:
# - Takes a stream of transactions as input, performs some kind of filtering, then
# outputs the result into two separate streams -- those that are legitimate,
# and those are suspicious, an operation known as branching.
# - Uses a consumer to read messages, then does its own processing on those
# messages and produces messages back into one of the two output topics.
# --> Thus, we will need a consumer and a producer.


# Consumers:
# - Reads messages from a topic.

# Kafka will then broadcast the messages to these consumers as they are being
# published. --> A feature at the core of the "reactiveness" of
# streaming applications made w/ Kafka.

import os
import json
from kafka import KafkaConsumer, KafkaProducer

# Grab broker URL and transaction topic from environment variables
KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
LEGIT_TOPIC = os.environ.get("LEGIT_TOPIC")
FRAUD_TOPIC = os.environ.get("FRAUD_TOPIC")


# Function to determine if transaction is suspicious:
def is_suspicious(transact):
    return transact["amount"] >= 900


if __name__ == "__main__":
    # Instantiate consumer
    consumer = KafkaConsumer(
        TRANSACTIONS_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=json.loads
    )
    # Use producer to redirect transaction to two streams (Fraud or Legit)
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode()
    )
    # Now, we can process the stream of messages by iterating over the consumer and produce messages:
    for message in consumer:
        transaction = message.value
        topic = FRAUD_TOPIC if is_suspicious(transaction) else LEGIT_TOPIC
        producer.send(topic, value=transaction)
        # print(topic, transaction)



























