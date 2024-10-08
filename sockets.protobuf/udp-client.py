#!/usr/bin/env python3

import sys
import socket
import sensor_pb2

if len(sys.argv) < 2:
    print('Usage: ./uddp-client.py <host>')
    exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination = (sys.argv[1], 1234)

reading = sensor_pb2.Reading()
reading.Id = 1
reading.type = sensor_pb2.Reading.HUMIDITY
reading.value = 0.2
reading.unit = "kg/m3"

data = reading.SerializeToString()
print(data)

sock.sendto(data, destination)
sock.close()
