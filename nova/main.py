#!/bin/python
import os
# can put in /etc/profile and run source /etc/profile
os.system("export OS_USERNAME=cloud_project2")
os.system("export OS_PASSWORD=cloud_project2")
os.system("export OS_TENANT_NAME=cloud_project2")
os.system("export OS_AUTH_URL=http://10.2.4.129:5000/v2.0/")
os.system("export OS_COMPUTE_API_VERSION=2.0")

os.system("nova image-list > .images")
f=open(".images","r")
a=f.readlines()
imgs={}
count=1
for i in range(2,len(a)):
	b=a[i].split('|')
	if(len(b)>1):
		imgs[count]=[b[1],b[2],b[3],b[4]]
		count=count+1
print imgs
f.close()


os.system("nova flavor-list > .flavor")
f=open(".flavor","r")
a=f.readlines()
flvs={}
for i in range(2,len(a)):
	b=a[i].split('|')
	if(len(b)>1):
		print b
		flvs[b[1]]=[b[2],b[3],b[4],b[5],b[6],b[7],b[8]]
print flvs 
f.close()


