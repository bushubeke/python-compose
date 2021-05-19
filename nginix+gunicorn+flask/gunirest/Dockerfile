#setting up python enviroment
#FROM python:3.8-slim-buster
FROM python:3.9-buster
#FROM ubuntu
# RUN useradd -m plusrest

#USER adduser -m home/plusrest -g root -G sudo --disabled-password --gecos '' -u plusrest
# Working Dir
RUN useradd -ms /bin/bash plusrest -g root
WORKDIR /home/plusrest/Documents/Enviroment/project


# coping contents of working dir to at app
ADD . /home/plusrest/Documents/Enviroment/



RUN apt-get update 
#RUN apt-get install nano
#RUN python -m pip install --upgrade pip

#install dependencies
COPY ./req.txt .
RUN pip install --upgrade pip
RUN pip install -r req.txt

COPY . /home/plusrest/Documents/Enviroment/


#run uwsgi command to start the uwsgi server

#CMD [ "uwsgi", "uwsgi.ini" ]
ENTRYPOINT ["./guni.sh"]
#CMD ["gunicorn" ,"-w" "1", "-k", "eventlet" ,"-b", "0.0.0.0:4000" ,"prod:pro"]

#CMD ["gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:5000 prod:pro"]

#using gunicorn 




