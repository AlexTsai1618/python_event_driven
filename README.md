# Python Event Driven Learning

A project that helps me know how to utilize event-driven in any service.

## Project overview
### System Architecture
<div style="width:100%">

![System architecture](pic/python_event_driven.jpg)

</div>

## Technologies
***
A list of technologies used within the project:

* [Django 3.1.3](https://www.djangoproject.com/)
* [Flask](https://flask.palletsprojects.com/)
* [CloudAMQP](https://www.cloudamqp.com/)
* [docker](https://www.docker.com/)
* [docker-compose](https://docs.docker.com/compose/)

#### 
## Usage

### step 1 launch admin service

```
cd admin
docker-compose up --build
```

### step 2 launch main service

```
cd main
docker-compose up --build
```

### step 3 api Testing
#### step 3.0 install postman and Signup a CloudAMQP account
install postman through following link
https://www.postman.com/downloads/

Signup a CloudAMQP account through following link
https://www.cloudamqp.com/

#### step 3.1 update the cloudamqp url to following file
admin/consumer.py
admin/products/producer.py
main/consumer.py
main/producer.py

```
please change URLParamerter to your own url
params = pika.URLParameters('Your CloudAMPQ url')
```

### step 3.2 

