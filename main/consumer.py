# RabbitMQ: Message queue  
import pika  

KEY = pika.URLParameters('amqps://wmtjajso:OVRn9xAU6HFhtkoVOxFxfR8t8JH-9-aO@elk.rmq2.cloudamqp.com/wmtjajso')

connection = pika.BlockingConnection(KEY)
channel = connection.channel()  

def callback(channel, method, props, body):  
    print('main ack')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)
print('main consumingC')
channel.start_consuming()
channel.close()

