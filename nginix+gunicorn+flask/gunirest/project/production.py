import os
import pytest
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

#depending what conf you would want use read the comment below,
#normally this for working with docker or you can run uwsgi uwsgi.ini from plusrest directory

#from texting.app import create_prod_app,db

# use the line below if your running using python production.py run
#else use the above line for running in docker using uwsgi uwsgi.ini command

from app import create_prod_app,db
basde=os.path.abspath(os.path.dirname(__file__))

MIGRATION_DIR = os.path.join(basde, 'prodmigrations')

    
#app = create_app('test') 
#app=create_prod_app()
soc=create_prod_app()
pro=soc['app']
app=soc['socketio']

#prod=app.run(pro)
prodmanager=Manager(soc['app'])
#manager.init_app(tapp)
migrate_test = Migrate(soc['app'], db, directory=MIGRATION_DIR)
prodmanager.add_command('db', MigrateCommand)


###########################################################################################################333
#############################################################################################################
#############################################################################################################

# this sectionis when using uwsgi
#gunicorn --workers 4 --worker-class eventlet -w 1 --bind 0.0.0.0:5000 production:pro
#gunicorn -w 1 --worker-class eventlet -b 0.0.0.0:4000 'production:create_prod_app()'
#gunicorn --workers 1 --worker-class eventlet --bind 0.0.0.0:4000 'production:create_prod_app()'
#uwsgi --http :5000 --gevent 1000 --http-websockets --master --wsgi-file production.py --callable app
#################################################################################################
#############################################################################################
#this section below is to be put in ini file with while dockerizing my flask app
#note dome of the values might not apply 
#use the below link to deploy on sinle node locally
#https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04
##########################################################################################333
# [uwsgi]
# module=production
# master=True
# gevent=1000
# callable=app
# processes = 2

# #socket = myproject.sock #this configuration can be used to expose when using nginx
# #chmod-socket = 660
# vacuum = true

# die-on-term = true

##########################################################################################333

# if __name__ == '__main__':
#     prodmanager.run()