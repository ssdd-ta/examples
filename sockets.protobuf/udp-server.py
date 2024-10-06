#!/usr/bin/env python3

import socket
from sensor_pb2 import Reading

sock = socket.socket(type=socket.SOCK_DGRAM)
sock.bind(('', 1234))
reading = Reading()

while True:
    data, address = sock.recvfrom(1024)
    print(f"sensor: {address},\nraw-data:\n{data}")

    reading.ParseFromString(data)
    print("Sensor {0.Id} ({1}) value:{0.value:.2f} {0.unit}".format(
        reading, Reading.SensorType.Name(reading.type)))
