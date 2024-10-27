import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='test', exchange_type='fanout')

ch.basic_publish(exchange='test', routing_key='', body='hi this is a request from mahdi')

print('your request sent')

connection.close()
