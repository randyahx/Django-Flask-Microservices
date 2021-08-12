# RabbitMQ: Message queue
from admin.product.models import Product
import pika
import json

KEY = pika.URLParameters(
    'amqps://wmtjajso:OVRn9xAU6HFhtkoVOxFxfR8t8JH-9-aO@elk.rmq2.cloudamqp.com/wmtjajso')

connection = pika.BlockingConnection(KEY)
channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(channel, method, props, body):
    print('admin ack')
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=id)
    product.likes = product.likes+1
    product.save()
    print(f'Product {id} liked!')

channel.basic_consume(queue='admin', on_message_callback=callback)
print('admin consuming')
channel.start_consuming()
channel.close()
