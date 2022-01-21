import pika, json

params = pika.URLParameters('your amqp url')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    print(json.dumps(body))
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
