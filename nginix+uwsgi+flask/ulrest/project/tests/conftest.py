import os

# wd="/home/Bushu/Documents/Enviroment/finalrest/texting"
# #wd="/home/Bushu/Documents/Enviroment/finalrest/texting/tests"
# os.chdir(wd)
##########################################################################################
##########################################################################################
from app import create_app
from app.models import db
from app.models.auth_models import *


##################################################################################################################################
import pytest

###############################################################################################
    #this fixture below is formed using flask testing documentation exposing client fixuture as a model
################################################################################################
@pytest.fixture(scope="module")
def client():
    #app = create_app('test')
    socketapp = create_app('test')    
    #app = create_app('test') 
    app = socketapp['app'] 
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    client = app.test_client()
 
    # Establish an application context before running the tests.
    contetxt = app.app_context()
    contetxt.push()
    yield client  # this is where the testing happens!
    
    contetxt.pop()

###############################################################################################################333
#soure of this fixture is found in the link below from patriks software blog, it has simmlarites with flask testing documentation with pytest
#https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
#################################################################################################################
# @pytest.fixture(scope='module')
# def init_database():
#     # Create the database and the database table
#     db.create_all()
 
#     # Insert user data
#     # user1 = User(email='patkennedy79@gmail.com', plaintext_password='FlaskIsAwesome')
#     # user2 = User(email='kennedyfamilyrecipes@gmail.com', plaintext_password='PaSsWoRd')
#     # db.session.add(user1)
#     # db.session.add(user2)
 
#     # Commit the changes for the users
#     db.session.commit()
 
#     yield db  # this is where the testing happens!
 
#     db.drop_all()

###############################################################################################################333

#################################################################################################################
@pytest.fixture(scope='module')
def setup_database():
    db.create_all()
    yield db
    #db.drop_all()

@pytest.fixture(scope='module')
def teardown_database():
    db.drop_all()

