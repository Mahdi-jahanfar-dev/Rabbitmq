import pika
from uuid import uuid4
class Sender:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.ch = self.connection.channel()
        self.q = self.ch.queue_declare(queue='', exclusive=True)
        self.q_name = self.q.method.queue
        self.ch.basic_consume(queue=self.q_name, on_message_callback=self.callback, auto_ack=True)

    def callback(self ,ch, method, proper, body):
        if self.core_id == proper.correlation_id:
            self.response = body
    
    def call(self,n):
        n = str(n)
        self.core_id = str(uuid4())
        self.response = None
        self.ch.basic_publish(exchange='', routing_key='rpc_queue', properties=pika.BasicProperties(reply_to=self.q_name, correlation_id=self.core_id), body=n)
        
        while self.response == None:
            self.connection.process_data_events()
            
        return int(self.response)
    

send = Sender()
print(send.call(30))