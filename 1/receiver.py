import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel_2 = connection.channel()

channel_2.queue_declare('hello')

def first_test(char, method, properties, body):
    print(f'received message : {body}')

channel_2.basic_consume(queue='hello', on_message_callback=first_test, auto_ack=True)

print('wait for message. if you whant to exit press ctrl + c')

channel_2.start_consuming()
