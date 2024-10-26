import json 
import random
import string
from sys import stdout
import logging
from time import time_ns, sleep

from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable


logger = logging.getLogger('KafkaLogger')
logger.setLevel(logging.DEBUG) 
logFormatter = logging.Formatter("%(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")
consoleHandler = logging.StreamHandler(stdout)
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)


def get_producer():
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers=['kafka:9092'],
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            logger.info("Connected to kafka:9092")
            return producer
        except NoBrokersAvailable:
            logger.info("Kafka NoBrokersAvailable! Retrying in 10 sec.")
            sleep(10)
        except Exception as e:
            logger.error(f"Encountered an error: {e}")
            raise e


def generate_message() -> dict:
    message = ''.join(random.choices(string.ascii_lowercase, k=10))
    timestamp_ns = time_ns() // 1_000_000
    return {
        'message': message,
        'timestamp_ns': timestamp_ns
    }


if __name__ == '__main__':
    producer = get_producer()
    while True:
        msg = generate_message()
        topic = "demotopic"
        logger.info(f"Producing message to topic: '{topic}' | {str(msg)}")
        producer.send(topic, msg)
        sleep(5)