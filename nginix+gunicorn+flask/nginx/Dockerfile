#using Nginx image

FROM nginx
#FROM ubuntu

#RUN apt-get update
#RUN apt-get -y install software-properties-common
#RUN apt-get -y install dirmngr --install-recommends
# RUN apt-get install nano
#
#RUN add-apt-repository ppa:certbot/certbot
#RUN apt-get update 

#RUN apt-get -y install nano

#RUN apt-get install nginx
#RUN add-apt-repository ppa:certbot/certbot

#RUN apt-get update 

#RUN apt install -y python3-certbot-nginx
#RUN apt-get install python-certbot-nginx

#RUN certbot --nginx -d localhost -d localhost
# remove defautl configuration
RUN rm /etc/nginx/conf.d/default.conf

# COPY localhost.pem /

# COPY localhost-key.pem /
#copy our own configuration

COPY nginx.conf /etc/nginx/conf.d/