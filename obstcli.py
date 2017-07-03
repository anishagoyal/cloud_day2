#!/usr/bin/python

import os,socket,sys,time,commands

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip="192.168.122.1"
s_port=8888

#taking input for device name
drive_name=raw_input("enter storage drive name: ")
#taking input for device size
drive_size=raw_input("enter drive size in MB: ")

s.sendto(drive_name,(s_ip,s_port))
s.sendto(drive_size,(s_ip,s_port))

res = s.recvfrom(4)


if res[0] == "done" :
	os.system('mkdir /media/' +drive_name)		
	os.system('mount ' +s_ip+ ':/mnt/' +drive_name+ ' /media/'+drive_name)
else:
	print "no response from storage cloud"
