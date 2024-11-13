import json

from kafka import KafkaConsumer

from mongo_connection import get_mongo_connection

consumer = KafkaConsumer(
    'f_transaction_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group'
)

for transaction in consumer:
    transaction = transaction.value.decode('utf-8')
    print(f"received message: {transaction}")

    collection = get_mongo_connection('fraud_collection')
    collection.insert_one(json.loads(transaction))