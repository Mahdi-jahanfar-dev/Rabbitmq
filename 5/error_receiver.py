import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='t1', exchange_type='topic')

q = ch.queue_declare(queue='', exclusive=True)
q_name = q.method.queue

binding_key = '#.important'

ch.queue_bind(queue=q_name, exchange='t1', routing_key=binding_key)

def callback(ch, method, properties, body):
    with open('important_error', 'a') as err:
        err.write(f'{str(body)} \n')

print('wait....')

ch.basic_consume(queue=q_name, on_message_callback=callback, auto_ack=True)

ch.start_consuming()

