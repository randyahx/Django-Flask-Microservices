# RabbitMQ: Message queue  
from main import db, Product  
import pika  
import json  
import django
import os  

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")

KEY = pika.URLParameters('amqps://wmtjajso:OVRn9xAU6HFhtkoVOxFxfR8t8JH-9-aO@elk.rmq2.cloudamqp.com/wmtjajso')

connection = pika.BlockingConnection(KEY)
channel = connection.channel()  

def callback(channel, method, props, body):  
    print('Received in Main Consumer')
    data = json.loads(body)
    print(data)

    if props.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()

    elif props.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
    
    elif props.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()

channel.basic_consume(queue='main', on_message_callback=callback)
print('main consuming')
channel.start_consuming()
channel.close()

