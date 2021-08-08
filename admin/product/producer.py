# RabbitMQ: Message queue  
import pika  

KEY = pika.URLParameters('')

connection = pika.BlockingConnection(KEY)
channel = connection.channel()  

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')