import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()
ch.queue_declare(queue='rpc_queue', exclusive=True)

def callback(ch, method, proper, body):
    n = int(body)
    print('processing message..')
    response = n + 1
    ch.basic_publish(exchange='', routing_key=proper.reply_to, properties=pika.BasicProperties(correlation_id=proper.correlation_id), body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue='rpc_queue', on_message_callback=callback)
print('waiting for message')
ch.start_consuming()
