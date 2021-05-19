import os
#from dotenv import load_dotenv 
# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv('.env')

class Config(object):
    
    #SECRET_KEY=os.getenv("SECRET_KEY")
    SECRET_KEY='e24d0570b7e1fbca424732a3f99e6661e50c6ed0557657c26c2b1e6fdeaeb8c8295ec30a5e191e9971990aebac073966d704af76bec39330f67f77ef90ee6d7b5636d3963d52955133f818f0b8e0a286f3eb0b089b668a83fd9bfdee'
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'transtextdev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
      
    #flask upload configuration
    UPLOADED_PHOTOS_DEST='/uploads/profile'
    UPLOADED_MESSAGES_DEST='/uploads/message'
    MAIL_SERVER='nothing'
    MAIL_USERNAME="nothing"
    MAIL_PASSWORD="nothing"
    MAIL_DEFAULT_SENDER="nothing"
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False
    MAIL_MAX_EMAILS=500

class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'teleporttest.db')
    UPLOADED_PHOTOS_DEST='/uploads/profile'
    UPLOADED_MESSAGES_DEST='/uploads/message'
    MAIL_SERVER='"blabla@mail.com"'
    MAIL_USERNAME="blabla@mail.com"
    MAIL_PASSWORD="blabla@mail.com"
    MAIL_DEFAULT_SENDER="blabla@mail.com"
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False
    MAIL_MAX_EMAILS=500
    MAIL_SUPPRESS_SEND=False
   


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'transtextprod.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'teleporttest.db')
    UPLOADED_PHOTOS_DEST='/uploads/profile'
    UPLOADED_MESSAGES_DEST='/uploads/message'
    MAIL_SERVER='"blabla@mail.com"'
    MAIL_USERNAME="blabla@mail.com"
    MAIL_PASSWORD="blabla@mail.com"
    MAIL_DEFAULT_SENDER="blabla@mail.com"
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False
    MAIL_MAX_EMAILS=500
    MAIL_SUPPRESS_SEND=False
config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY