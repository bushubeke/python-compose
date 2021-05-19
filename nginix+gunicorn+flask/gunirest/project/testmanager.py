import os
import pytest
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import create_app, db
basde=os.path.abspath(os.path.dirname(__file__))

MIGRATION_DIR = os.path.join(basde, 'testmigrations')

socketapp = create_app('test')    
#app = create_app('test') 
app = socketapp['app'] 
socketio=socketapp['socketio']
testmanager=Manager(app)
#manager.init_app(tapp)
migrate_test = Migrate(app, db, directory=MIGRATION_DIR)
testmanager.add_command('db', MigrateCommand)

@testmanager.command
def run():
    socketio.run(app,host='0.0.0.0')
    #app.run(host='0.0.0.0')


@testmanager.command
def test():
  
    pytest.main(["-v"])
    """Runs the unit tests."""
    
# @testmanager.command()
# def cove():
#     pytest.main(["--cov","app" ,"tests/"])
if __name__ == '__main__':
    testmanager.run()