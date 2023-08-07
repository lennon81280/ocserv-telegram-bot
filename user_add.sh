#!/bin/bash

user_name=$1

rnd=$(echo $RANDOM | md5sum | head -c 6; echo;)

cd /root/anyconnect
mkdir $1
cd $1
expect<<-END
spawn /etc/ocserv/tg/gen-client-cert.sh $1 /root/anyconnect
expect "Enter Export Password:"
send "\r"
expect "Verifying - Enter Export Password:"
send "\r"
expect eof
exit
END

cp /root/anyconnect/$1/$1.p12 /var/www/html/$1-$rnd.p12
echo "$1 The user is successfully created."
