#!/bin/python
import sys
import os
import main
flavor_id=int(sys.argv[1])
i_id=int(sys.argv[2])
name=sys.argv[3]
image_id=main.imgs[1][0]
print flavor_id
print image_id
print name

image_id=str(image_id)
image_id="".join(image_id.split())
#print image_id
comm="nova boot --flavor="+str(flavor_id)+" --image="+str(image_id)+" "+name
print comm
os.system(comm)

