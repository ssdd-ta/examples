#!/usr/bin/python3
# Extracted from: https://www.rabbitmq.com/tutorials/tutorial-five-python.html

import sys
import pika


def callback(ch, method, properties, body):
    print("[x] Received %r: %r " % (method.routing_key, body.decode("UTF-8")))


localhost = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(localhost)
channel = connection.channel()

channel.exchange_declare(exchange='twitter-pattern', exchange_type='topic')
result = channel.queue_declare(queue='', exclusive='True')
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: {} [binding key]...\n".format(sys.argv[0]))
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='twitter-pattern',
        queue=queue_name,
        routing_key=binding_key
    )

channel.basic_consume(
    on_message_callback=callback,
    queue=queue_name,
    auto_ack=True
)

print("[*] Waiting for messages. To exit press Ctrl+")
channel.start_consuming()
