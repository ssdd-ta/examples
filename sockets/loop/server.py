#!/usr/bin/python3
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('' , 4080))
    print('Waiting for messages...')

    while 1:
        msg, addr = s.recvfrom(1024)
        msg = msg.decode('utf-8', 'replace')
        s.sendto('OK'.encode(), addr)  # Send 'OK' back to the client
        print(f'{msg} from {addr}')
