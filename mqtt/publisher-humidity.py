#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import json
import time
import random
import paho.mqtt.client as mqtt

IDENTIFIER = 'X001'


def take_reading():
    return {
        'identifier': IDENTIFIER,
        'value': random.randint(60, 80),
        'unit': '% RH',
        'timestamp': time.time()
    }


publisher = mqtt.Client()
publisher.connect('127.0.0.1')

n = 0

while 1:
    publisher.publish(
        'iotevents/humidity/{}'.format(IDENTIFIER),
        json.dumps(take_reading())
    )

    n += 1
    print('Published humidity reading: {}'.format(n))

    time.sleep(1)
