import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='t3', exchange_type='direct')

q = ch.queue_declare(queue='', exclusive=True)

q_name = q.method.queue

r_key = ('error')

ch.queue_bind(queue=q_name, exchange='t3', routing_key=r_key)

def callback(ch, method, properties, body):
    with open('error_info', 'a') as el:
        el.write(f'{str(body)} \n')

print('wait...')

ch.basic_consume(queue=q_name, on_message_callback=callback, auto_ack=True)

ch.start_consuming()
