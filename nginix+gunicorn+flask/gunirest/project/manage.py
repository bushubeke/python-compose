import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import create_app, db
#from app import socketio
#   from app import user, RolesUsers,Roles
#print(sys.argv[2])
#app=None
#gunicorn -w 1 --worker-class eventlet -b 0.0.0.0:4000 'manage:create_prod_app()'
#################################################################################################
socketapp = create_app('dev')    
#app = create_app('test') 
app = socketapp['app'] 
socketio=socketapp['socketio']
manager = Manager(app)
#manager.init_app(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    socketio.run(app,host='0.0.0.0')



if __name__ == '__main__':
    manager.run()