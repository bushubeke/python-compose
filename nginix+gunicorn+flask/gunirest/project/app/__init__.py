from flask import Flask,current_app, request, session


from flask_cors import CORS


from .config import DevelopmentConfig,TestingConfig,ProductionConfig
from flask import Blueprint
from flask_restx import Api

from .controller import mail
from .models import db
from .models.auth_models import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .fileresponse.front import front
from .appsock import *
from .appsock.testsock import *

#from flask.app import Flask
userauthblueprint = Blueprint('api', __name__)
########################################################################################
#this imports are for urls from controller module
from .controller.auth_controller import uapi
#from .controller import socketio
########################################################################################
authorizations = { 'apikey' : {'type' : 'apiKey','in' : 'header', 'name' : 'X-APP-KEY' }}
api = Api(userauthblueprint,
        title='FLASK RESTPLUS TOKEN BASED AUTH WITH PyJWT',
        version='1.0',
        authorizations=authorizations
        )

api.add_namespace(uapi, path='/api')


cors=CORS()

admin=Admin()



def create_app(config_name):
    app = Flask(__name__)
    if config_name=='dev':
        print(' * currently running with development configuration')
        app.config.from_object(DevelopmentConfig)
    elif config_name=='test' or None:
        print(' * currently running with testing configuration')
        app.config.from_object(TestingConfig)
    elif config_name=='prod':
        print(' * currently running with production configuration')
        app.config.from_object(ProductionConfig)
    else:
        pass
    app.register_blueprint(front,url_prefix='/pages')
    app.app_context().push()
    db.init_app(app)
    admin = Admin(app, name='DashBoard', template_mode='bootstrap4')
    admin.add_view(ModelView(User, db.session,category='Authentication'))
    admin.add_view(ModelView(Role, db.session,category='Authentication'))
    admin.add_view(ModelView(RolesUsers, db.session,category='Authentication'))
    cors.init_app(app, resources={r'/*': {'origins': '*'}})
    ma.init_app(app)
   
    mail.init_app(app)
    # @login_manager.unauthorized_handler
    # def unauthorized_handler():
    #     return render_template('page-403.html'), 403
    # @app.errorhandler(403)
    # def access_forbidden(error):
    #     return render_template('page-403.html'), 403

    # @app.errorhandler(404)
    # def not_found_error(error):
    #     return render_template('page-404.html'), 404

    # @app.errorhandler(500)
    # def internal_error(error):
    #     return render_template('page-500.html'), 500

    app.register_blueprint(userauthblueprint)
    #socketio.init_app(app,async_mode="gevent_uwsgi")
    socketio.init_app(app,host="0.0.0.0")
    app={'app':app,'socketio':socketio}
    return app
def create_prod_app():
    app = Flask(__name__)

    print(' * currently running with production configuration')
    app.config.from_object(ProductionConfig)
    app.register_blueprint(front,url_prefix='/pages')
    app.app_context().push()
    
    db.init_app(app)
    admin = Admin(app, name='DashBoard', template_mode='bootstrap4')
    admin.add_view(ModelView(User, db.session,category='Authentication'))
    admin.add_view(ModelView(Role, db.session,category='Authentication'))
    admin.add_view(ModelView(RolesUsers, db.session,category='Authentication'))
    cors.init_app(app, resources={r'/*': {'origins': '*'}})
    ma.init_app(app)
    
    mail.init_app(app)
    
   
    app.register_blueprint(userauthblueprint)
    # socketio.init_app(app,async_mode="gevent_uwsgi")
    socketio.init_app(app)
    #socketio.init_app(app)
    app={'app':app,'socketio':socketio}
    return app