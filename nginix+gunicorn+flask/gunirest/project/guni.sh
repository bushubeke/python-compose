#!/bin/sh
gunicorn -w 1 -k eventlet -b 0.0.0.0:4000 'production:pro'