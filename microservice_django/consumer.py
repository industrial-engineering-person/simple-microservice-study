from enum import auto
from tabnanny import check
import os, django, json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()
from user_order.models import Order, Shop
import pika 


params = pika.URLParameters('amqps://vxfoqgjz:EfqcPhZ9xPZIpS3Jc_1MJpWY9EwYHQA8@dingo.rmq.cloudamqp.com/vxfoqgjz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='microorder')

def callback(ch, method, properties, body):
    print('Received in Django')
    id = json.loads(body)
    print(id)
    order = Order.objects.get(id=id)
    order.deliver_finish = 1
    order.save()
    print('order deliver finished')

channel.basic_consume(queue='microorder', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()

