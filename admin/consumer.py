# RabbitMQ: Message queue
import pika

KEY = pika.URLParameters(
    'amqps://wmtjajso:OVRn9xAU6HFhtkoVOxFxfR8t8JH-9-aO@elk.rmq2.cloudamqp.com/wmtjajso')

connection = pika.BlockingConnection(KEY)
channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(channel, method, props, body):
    print('admin ack')


channel.basic_consume(queue='admin', on_message_callback=callback)
print('admin consuming')
channel.start_consuming()
channel.close()
