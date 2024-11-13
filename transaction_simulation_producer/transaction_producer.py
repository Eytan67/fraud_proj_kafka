import json

from kafka import KafkaProducer

from transaction_simulation_producer.transaction_maker import Transaction

producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )


for i in range(10):
    message = Transaction()
    producer.send('transaction_topic', message.to_dict())
    print(f'Sent {message}')

producer.flush()
producer.close()