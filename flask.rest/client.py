#!/usr/bin/env python3
# -*- coding:utf-8; mode:python -*-

from requests import put, get


print(get('http://localhost:5000/').json())

device_id = "door1"
response = get(f'http://localhost:5000/{device_id}')
print(response.json())

put(f'http://localhost:5000/{device_id}', data={'status': 'disabled'})
print(get(f'http://localhost:5000/{device_id}').json())
