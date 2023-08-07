#!/bin/bash

cat /root/anyconnect/$1/$1-cert.pem >> /root/anyconnect/revoked.pem
certtool --generate-crl --load-ca-privkey ca-key.pem  --load-ca-certificate ca-cert.pem --load-certificate revoked.pem  --template crl.tmpl --outfile /etc/ocserv/crl.pem

rm -f /var/www/html/$1-*
rm -rf /root/anyconnect/$1

systemctl reload ocserv
