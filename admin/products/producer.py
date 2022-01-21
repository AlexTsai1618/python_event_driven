# amqps://cjcxavag:o2Qi8SS5BP1pdG37j4SCGFquF-7qRvNf@gerbil.rmq.cloudamqp.com/cjcxavag
import pika
import json

params = pika.URLParameters('amqps://cjcxavag:o2Qi8SS5BP1pdG37j4SCGFquF-7qRvNf@gerbil.rmq.cloudamqp.com/cjcxavag')


connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method,body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)