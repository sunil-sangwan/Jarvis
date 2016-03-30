#!/usr/bin/env python3

import os

#print (os.listdir("/bin"))

""" all commands of system are stored in "/bin", "/sbin", "/usr/bin", "/usr/sbin" 
	so take input all directory in this directories
	"""
command_list = []
for i in os.listdir("/bin"):
	command_list.append(i)

for i in os.listdir("/sbin"):
	command_list.append(i)

for i in os.listdir("/usr/bin"):
	command_list.append(i)

for i in os.listdir("/usr/sbin"):
	command_list.append(i)

# check list
#print (command_list)
