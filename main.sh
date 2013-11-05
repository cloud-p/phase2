#!/bin/bash
hadoop_download="http://apache.claz.org/hadoop/common/hadoop-1.2.1/hadoop-1.2.1.tar.gz"
wget $hadoop_download
chmod a+x hadoop_install.sh
chmod a+x ssh-id-copy.sh
./hadoop_install.sh $1
identity_file=$1
properties_file=$1
user="root"
slaves=`cat $properties_file | grep -i tasktracker | cut -f 2`
echo "slaves" $slaves
if [ ! -e ~/.ssh/id_rsa ]
then
         ssh-keygen -f ~/.ssh/id_rsa -P ""
fi
for slave in $slaves
do
        scp -i $identity_file -o StrictHostKeyChecking=no ~/.ssh/id_rsa.pub $user@$slave:
        ssh -i $identity_file -o StrictHostkeyChecking=no $user@$slave "cat id_rsa.pub >> ~/.ssh/authorized_keys"
done
