#!/usr/bin/python

import os,socket,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("",8888))

#while true:
#data will recieve drive name
data=s.recvfrom(50)
d_name=data[0]

#data will recieve drive size
data1=s.recvfrom(10)
d_size=data1[0]

#here client address will be stored
cliaddr=data1[1][0]

print d_name
print d_size
print cliaddr

#creating LVM by the name of client drive
os.system('lvcreate --name ' +d_name+ ' --size ' +d_size+ 'M mydevice')

#format client drive by xfs or ext4
os.system('mkfs.ext4  /dev/mydevice/' +d_name)

#creating mount point
os.system('mkdir  /mnt/' +d_name)
#mounting the drive locally
os.system('mount  /dev/mydevice/' +d_name+ ' /mnt/' +d_name)
#nfs server configuration
os.system('yum install nfs-utils -y')
#making entry in nfs export file 
entry = " /mnt/" +d_name+ " " +cliaddr+ "(rw,no_root_squash)"
#appending this var to /etc/exports file
f=open('/etc/exports','a')
f.write(entry)
f.write("\n")
f.close()

#finally starting nfs service and service persistent
os.system('systemctl restart nfs-server')
os.system('systemctl enable nfs-server')
check=os.system('exportfs -r')
if check==0:
	s.sendto("done",data1[1])
else :
	print "plz check your code"

