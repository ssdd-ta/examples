#!/usr/bin/python3
# Extracted from: https://www.rabbitmq.com/tutorials/tutorial-three-python.html

import sys
import pika


localhost = pika.ConnectionParameters(host='localhost')
connection=pika.BlockingConnection(localhost)
channel=connection.channel()

channel.exchange_declare(exchange='twitter', exchange_type='fanout')

message=' '.join(sys.argv[1:]) or "Hello world!"

channel.basic_publish(
    exchange='twitter',
    routing_key='',
    body=message
)

print("[x] Sent: ", message)
connection.close()
