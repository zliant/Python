#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a server example which send hello to client.'

import time, socket, threading

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!This is the welcome message from server')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# create a socket base on IPv4 and TCP

#moniter the port
s.bind(('127.0.0.1', 9999))
s.listen(5)
print 'Waiting for connection...'

while True:
    # Create new connection
    sock, addr = s.accept()
    # create new thread to deal with the TCP connection:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
