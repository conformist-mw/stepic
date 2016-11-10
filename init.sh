#!/bin/bash

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
mkdir web/{public,uploads}
sudo rm /etc/gunicorn.d/*
sudo ln -s /home/box/etc/gunicorn-django.conf /etc/gunicorn.d/gunicorn.conf
sudo pip3 install django gunicorn
sudo sed -i  -e '1s/python/python3/' -e 's/17.5/19.6.0/g' /usr/sbin/gunicorn-debian \
/usr/bin/gunicorn /usr/bin/gunicorn-django /usr/bin/gunicorn-paster
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
