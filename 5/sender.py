import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='t1', exchange_type='topic')

messages = {
    'error.warning.important':'this message is important',
    'error.warning.notimportant' : 'this message is not important'
}


for key, value in messages.items():
    ch.basic_publish(exchange='t1', routing_key=key, body=value)

print('message sent')

connection.close()