#!/usr/bin/python3
import sys
import socket
import time

host = sys.argv[1]
port = sys.argv[2]
msg = "Your UCLM ID"  # "John.Doe" if your email is "John.Doe@alu.uclm.es

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while 1:
        s.sendto(msg.encode(), (host, int(port)))
        data, addr = s.recvfrom(1024)
        print(data.decode())
        time.sleep(1)
