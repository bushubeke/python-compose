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
    MAIL_SERVER='smtp.aol.com'
    MAIL_USERNAME='beimnetdegefu@aol.com'
    MAIL_PASSWORD='jqxj hrns xrwu odwr'
    MAIL_DEFAULT_SENDER='beimnetdegefu@aol.com'
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
    SECURITY_PASSWORD_SALT=True
    SECURITY_REGISTERABLE=True
    SECURITY_RECOVERABLE=True
    SECURITY_CHANGEABLE=True
    SECURITY_PASSWORD_SALT=os.getenv('SECURITY_PASSWORD_SALT')
    SECURITY_CONFIRMABLE=True
    SECURITY_SEND_REGISTER_EMAIL=True
    SECURITY_CONFIRM_URL='/confirmationu'
    #SECURITY_POST_LOGOUT_VIEW='/login'
    SECURITY_SENDER_MAIL='beimnetdegefu@aol.com   ' 
    SECURITY_TRACKABLE=True
    SECURITY_PASSWORD_HASH='pbkdf2_sha512'
    #SECURITY_POST_LOGIN_VIEW='/transtext'
    #SECURITY_POST_LOGOUT_VIEW='/login'
    SECURITY_POST_REGISTER_VIEW='/register'
    #CORS_ENABLED=True
    #SECURITY_LOGIN_URL='/tlogin'
    #SECURITY_LOGOUT_URL='/nologout'
    #flask upload configuration
    UPLOADED_PHOTOS_DEST='/uploads/profile'
    UPLOADED_MESSAGES_DEST='/uploads/message'
    MAIL_SERVER='smtp.aol.com'
    MAIL_USERNAME='beimnetdegefu@aol.com'
    MAIL_PASSWORD='jqxj hrns xrwu odwr'
    MAIL_DEFAULT_SENDER='beimnetdegefu@aol.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False
    MAIL_MAX_EMAILS=500
    MAIL_SUPPRESS_SEND=False
    WTF_CSRF_SECRET_KEY=os.environ.get('WTF_CSRF_SECRET_KEY')


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'transtextprod.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_SEND_REGISTER_EMAIL=True
    SECURITY_CONFIRM_URL='/confirmationu'
    #SECURITY_POST_LOGOUT_VIEW='/login'
    SECURITY_SENDER_MAIL='beimnetdegefu@aol.com   ' 
    SECURITY_TRACKABLE=True
    SECURITY_PASSWORD_HASH='pbkdf2_sha512'
    #SECURITY_POST_LOGIN_VIEW='/transtext'
    #SECURITY_POST_LOGOUT_VIEW='/login'
    SECURITY_POST_REGISTER_VIEW='/register'
    #CORS_ENABLED=True
    #SECURITY_LOGIN_URL='/tlogin'
    #SECURITY_LOGOUT_URL='/nologout'
    #flask upload configuration
    WTF_CSRF_SECRET_KEY=os.environ.get('WTF_CSRF_SECRET_KEY')
    UPLOADED_PHOTOS_DEST='/uploads/profile'
    UPLOADED_MESSAGES_DEST='/uploads/message'

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY