import logging
from confluent_kafka import Consumer, Producer

from config import config

logger = logging.getLogger(__name__)
connection_config = {'bootstrap.servers': 'localhost:9092'}


def main(group_id):
    producer = Producer({**connection_config, **config.kafka_producer})
    consumer = Consumer({**connection_config, **config.kafka_consumer, 'group_id': group_id})
    consumer.subscribe([config.consumer_kafka_topic])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error:
                logger.error(msg.error())
                continue

            try:
                event = msg.value()
                logger.info(f'Received event:\n\tkey: {event["key"]}\n\tdata: {event}')

                # do some processing

                producer.produce(
                    topic=config.producer_kafka_topic,
                    value=event,
                    key=msg.key(),
                    on_delivery=(lambda err, msg: logger.error(msg.error()) if err else logger.info(f'Produced msg to topic {msg.topic}')),
                    headers={'key': msg.key()},
                )
            except Exception as e:
                logger.error(e)

    finally:
        producer.flush()
        consumer.close()
        logger.info('Kafka consumer closed')
