# RabbitMQ를 쓰위위한 패키지 pika
import pika
import json

params = pika.URLParameters('amqps://vxfoqgjz:EfqcPhZ9xPZIpS3Jc_1MJpWY9EwYHQA8@dingo.rmq.cloudamqp.com/vxfoqgjz')

# rabbitMQ에 connect
connection = pika.BlockingConnection(params)

# connection을 가지고 채널을 연결
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(content_type=method)
    channel.basic_publish(exchange='', routing_key='microboss', body=json.dumps(body), properties=properties)
