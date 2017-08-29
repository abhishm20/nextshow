#!/bin/bash

NAME="posov5-apis"                                  # Name of the application
NUM_WORKERS=5                                     # how many worker processes should Gunicorn spawn
TIMEOUT=600                                     # how many worker processes should Gunicorn spawn
IP=192.168.0.101
DJANGO_WSGI_MODULE=project.wsgi                     # WSGI module name


# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --bind $IP \
  --timeout $TIMEOUT \
  --log-level=debug \
  --log-file=-
