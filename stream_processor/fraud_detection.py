


# def check_fraud_by_time(transaction):
#     collection = get_mongo_connection()
#     transactions = collection.find({"user_id": transaction.user_id})
#     if transactions.count() == 9:
#
#     collection.insert_one(transaction, {'expireAfterSeconds':60})

def check_fraud_by_time(transactions):
    # transactions.sort(key=lambda x: x['user_id'])
    # transactions.sort(key=lambda x: x['timestamp'])
    return transactions
