import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel_1 = connection.channel()

channel_1.queue_declare(queue='hello')

channel_1.basic_publish(exchange='', routing_key='hello', body='hello world')

print('message sent...')

connection.close()
