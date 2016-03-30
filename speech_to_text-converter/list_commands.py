#!/usr/bin/env python3

import os

#print (os.listdir("/bin"))
command_list = []
for i in os.listdir("/bin"):
	command_list.append(i)

for i in os.listdir("/sbin"):
	command_list.append(i)

for i in os.listdir("/usr/bin"):
	command_list.append(i)

for i in os.listdir("/usr/sbin"):
	command_list.append(i)

print (command_list)
