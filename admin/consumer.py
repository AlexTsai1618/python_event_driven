import pika,json,django,os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('your cloud amqp url')


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Recieve in admin')

    id = json.loads(body)

    try:
        # if not Product.objects.filter(id=id).exists():
        product = Product.objects.get(id=id)
        product.likes = product.likes + 1
        print(Product.objects.get(id=id))
        product.save()
        
        print("Product likes increase")
        # else:
        #     print("Have already exists!")
    except:
        print("Error")


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
