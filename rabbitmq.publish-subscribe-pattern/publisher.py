#!/usr/bin/python3
# Extracted from: https://www.rabbitmq.com/tutorials/tutorial-three-python.html

import sys
import pika

localhost = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(localhost)
channel = connection.channel()

channel.exchange_declare(exchange='twitter-pattern', exchange_type='topic')
routing_key = sys.argv[1] if len(sys.argv)>2 else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or "Hello world!"

channel.basic_publish(
    exchange='twitter-pattern',
    routing_key=routing_key,
    body=message
)

print("[x] Sent %r:%r: " % (routing_key, message))
connection.close()
