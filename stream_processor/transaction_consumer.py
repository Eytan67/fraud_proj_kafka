import json

from kafka import KafkaConsumer

from stream_processor.fraud_detection import check_fraud_by_time
from stream_processor.message_router import route_messages

consumer = KafkaConsumer(
    'transaction_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group'
)

for transaction in consumer:
    transaction = transaction.value.decode('utf-8')
    print(f"received message: {transaction}")
    route_messages(json.loads(transaction))

transactions_final = check_fraud_by_time(consumer)