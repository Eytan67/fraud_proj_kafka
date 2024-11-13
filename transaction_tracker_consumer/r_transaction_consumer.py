from kafka import KafkaConsumer

from stream_processor.mongo_connection import get_mongo_connection

consumer = KafkaConsumer(
    'f_transaction_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group'
)

for transaction in consumer:
    print(f"received message: {transaction.value.decode('utf-8')}")

