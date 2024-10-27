import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='t3', exchange_type='direct')


messages = {
    'warning': 'this is warning message',
    'info' : 'this is info message',
    'error' : 'this is error message'
}

for k , v in messages.items():
    ch.basic_publish(exchange='t3', routing_key=k, body=v)

print('message sent....')

connection.close()