import pika, json

params = pika.URLParameters('amqps://cjcxavag:o2Qi8SS5BP1pdG37j4SCGFquF-7qRvNf@gerbil.rmq.cloudamqp.com/cjcxavag')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    print(json.dumps(body))
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)