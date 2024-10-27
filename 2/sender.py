import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch1 = connection.channel()

ch1.queue_declare(queue='test', durable=True)


ch1.basic_publish(exchange='', routing_key='test',properties=pika.BasicProperties(delivery_mode=2,headers={'name':'mahdi'}), body='this is a request',)

print('message sent... ')

connection.close()

