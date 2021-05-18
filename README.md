# this are python webframework config sample without https 
 * python packages used are 
    * flask-restx
    * flask-sqlalchemy
    * pytest
    * flask-socketio
    * flask-marshmallow
    * gunicorn with eventlet
    * uwsgi with gevent (dependss on the compose file)
    * fast api ( with uvicorn is not updated yet)

 * nginx as a reverse proxy server(and no https configuration added)
 * it uses sqlite for all but ( psql containter config provided by fastapi creater Sebastián Ramírez for psql can be used) \
 with slight modification
the front end fcc is made by react and has not been made for mobile phones
the react codes can be found in here 
 * https://github.com/bushubeke/fcc
here are the pages you can test
  * localhost - open api documentaiton 
  * localhost/admin- flask admin home
  * localhost/pages/docktest - freecodecamp frontend certification apps(not optimized for mobile users)
  * localhost/pages/sockettest - flasksocket.io functionality page( it shuoud add one when clicked)

