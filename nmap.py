# Made by Ashutosh
#!/bin/python

import sys
from datetime import datetime
import socket

if len(sys.argv) == 2:	
	target=socket.gethostbyname(sys.argv[1]) # getting the host name as the second parameter
else:
	print("Invalid amount of arguments")
	print("Proper Format is nmap.py <ip address>")

#Adding our banner

print('*'*50)
print("Scanning Started (Made by:Ashutosh) " + target)
print("Time Started "+str(datetime.now()))
print('*'*50)

#Implementing the Port Scanner

try:
	for port in range(100,200):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target,port)) # returns 1 if port is closed else 0
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\n Exiting Program")
	sys.exit()
except socket.gaierror:
	print("Host Name could not be resolved")
	sys.exit()
except socket.error:
	print("could not connect to server")
	sys.exit()
