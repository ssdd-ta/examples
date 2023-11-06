#!/usr/bin/python3
# Extracted from: https://www.rabbitmq.com/tutorials/tutorial-two-python.html

import sys
import pika


localhost = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(localhost)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

for msg in sys.argv[1:]:
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=msg,
        properties=pika.BasicProperties(
            delivery_mode=2  # make message persistent
        ))

    print(f'[x] Sent: {msg}')

connection.close()
