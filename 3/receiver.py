import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='test', exchange_type='fanout')

ch_queue = ch.queue_declare(queue='', exclusive=True)

ch.queue_bind(queue=ch_queue.method.queue, exchange='test')

def callback(ch, method, properties, body):
    print(f'request message : {body}')


ch.basic_consume(queue=ch_queue.method.queue, on_message_callback=callback, auto_ack=True)

print('waiting for message is you whant exit press ctrl+c')

ch.start_consuming()
