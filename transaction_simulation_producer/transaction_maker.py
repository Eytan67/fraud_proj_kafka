import datetime
import uuid
import random


class Transaction:
    user_ids = [user_id for user_id in range(999999999, 1000009999)]
    black_list = random.sample(user_ids, 1000)

    def __init__(self):
        self.transaction_id = str(uuid.uuid4())
        self.user_id = random.choice(Transaction.user_ids)
        self.amount = random.uniform(0.01, 7500)
        self.timestamp = datetime.datetime.now()
        self.is_fraud = self.mark_potential_fraud()


    def mark_potential_fraud(self) -> bool:
       return self.amount < 0.1 or self.amount > 5000 or self.user_id in Transaction.black_list

    def __str__(self):
        return (f'transaction_id: {self.transaction_id}, user_id: {self.user_id}, amount: {self.amount}'
                f', timestamp: {self.timestamp}, is_fraud: {self.is_fraud}')

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "timestamp": self.timestamp.isoformat(),
            "is_fraud": self.is_fraud
        }