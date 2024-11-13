import json

from kafka import KafkaProducer

from transaction_simulation_producer.transaction_maker import Transaction

producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )


def route_messages(transaction):
    # for transaction in transactions_final:
    if transaction.get('is_fraud'):
        producer.send('f_transaction_topic', transaction)
    elif transaction.get('amount') > 3000:
        producer.send('h_transaction_topic', transaction)
    else:
        producer.send('r_transaction_topic', transaction)
