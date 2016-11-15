#!/bin/bash

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/nignx.conf
sudo /etc/init.d/nginx restart
sudo rm /etc/gunicorn.d/*
sudo cp etc/{django.conf,wsgi.conf} /etc/gunicorn.d
sudo apt-get update && sudo apt-get install libmysqlclient-dev python3-dev
sudo pip3 install django gunicorn mysqlclient
sudo sed -i  -e '1s/python/python3/' -e 's/17.5/19.6.0/g' /usr/sbin/gunicorn-debian /usr/bin/gunicorn
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
mysql -u root -e "CREATE USER 'django'@'localhost' IDENTIFIED BY '123456';"
mysql -u root -e "CREATE DATABASE djangoDB;"
mysql -u root -e "GRANT ALL PRIVILEGES ON djangoDB.* To 'django'@'localhost';"
