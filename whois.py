#!/usr/bin/python3
import socket

target = input("Inform target domain: ")

req = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
req.connect(("whois.iana.org",43))
req.send((target+"\r\n").encode())

resp = req.recv(1024).split()
whois = resp[19]
req.close()

req2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
req2.connect((whois,43))
req2.send((target+"\r\n").encode())

resp2 = req2.recv(1024)
print(resp2.decode("iso-8859-1"))
