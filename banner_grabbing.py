#!/usr/bin/python3
import socket

ip = input("Inform target IP Address: ")
port = int(input("Inform destination port: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip,port))

banner = sock.recv(1024)
print(banner)
