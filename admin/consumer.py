# RabbitMQ: Message queue  
import pika  

KEY = pika.URLParameters('')

connection = pika.BlockingConnection(KEY)
channel = connection.channel()  

def callback(channel, method, props, body):  
    print('admin ack')  

channel.basic_consume(queue='admin', on_message_callback=callback)
print('admin consuming')       
channel.start_consuming()
channel.close()

