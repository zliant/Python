#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a socket example which send echo message to server.'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# create connection:
s.connect(('127.0.0.1', 9999))
# revieve the welcome message:
print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
    # send data:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
