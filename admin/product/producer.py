# RabbitMQ: Message queue
import pika

KEY = pika.URLParameters(
    'amqps://wmtjajso:OVRn9xAU6HFhtkoVOxFxfR8t8JH-9-aO@elk.rmq2.cloudamqp.com/wmtjajso')

connection = pika.BlockingConnection(KEY)
channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')
