from flask import request,jsonify,current_app
from flask_restx import Namespace, fields,Resource
import json
from passlib.hash import pbkdf2_sha512

from ..utils import generate_token,token_decode
import datetime
from flask_mail import Mail,Message


#from . import db
#################################################################################
#this area is for flask extenstion objects

mail=Mail()
##############