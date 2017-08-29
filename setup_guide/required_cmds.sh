#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install libmysqlclient-dev
sudo dpkg-reconfigure locales

sudo apt-get install -y mysql-server mysql-server-core-5.7

sudo apt-get install -y libmysqlclient-dev
sudo apt-get install -y build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev


sudo apt install -y python-pip
sudo pip install -r requirements.txt


# Supervisor setup
sudo apt-get install -y supervisor
# put conf file of supervisor in /etc/supervisor/conf.d/posov5.conf
sudo supervisorctl reread
sudo supervisorctl update

# Nginx setup
sudo apt-get install nginx-full
sudo nano /etc/nginx/sites-available/mojo
sudo ln -s /etc/nginx/sites-available/mojo /etc/nginx/sites-enabled/mojo

# Gunicorn
chmod 777 bin/gunicorn_start
sudo pip install gunicorn

# changes timezone
dpkg-reconfigure tzdata


# Change /etc/my.cnf
[mysqld]
max_allowed_packet = 16M