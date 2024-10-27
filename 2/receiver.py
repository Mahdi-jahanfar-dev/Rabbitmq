import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch2 = connection.channel()

ch2.queue_declare(queue='test', durable=True)

def callback(char, method, properties, body):
    print(f'message : {body}')
    print(properties.headers)
    time.sleep(3)
    ch2.basic_ack(delivery_tag=method.delivery_tag)

ch2.basic_qos(prefetch_count=1)


ch2.basic_consume(queue='test', on_message_callback=callback,)

ch2.start_consuming()