#!/usr/bin/python3
import socket,sys

host = input("Inform hostname to resolve: ")

print(host,"--->",socket.gethostbyname(host))
