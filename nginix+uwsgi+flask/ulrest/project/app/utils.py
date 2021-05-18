import jwt
from functools import wraps

####################################################################################################
#this section generates token 
####################################################################################################
def generate_token(data,key,exp):
    return  jwt.encode({'data':data,'exp':exp},key,algorithm="HS256")
def token_decode(data,key):
    return jwt.decode(data,key,algorithms="HS256")

#################################################################################################
#this is little bit modified token verification decorator taken from anthony at pretty printed
#################################################################################################
# def token_required(func,key):
#     @wraps(func)
#     def decorated(*args, **kwargs):

#         token = None

#         try:
#             token = request.headers['X-APP-KEY']
#         except:
#             pass
            
#         if token:
           
#             return {'message' : 'Token is missing.'}, 401
#         data=None
#         try:
#            data = jwt.decode(token, key,algorithms="HS256")
#         except Exception as e:
#             print(e)
#             print('token decoding error')
#         if data:
#             return func(*args, **kwargs)
#         else:
#             return {'message' : 'The token provided is either invalid or missing.'}, 401
#     return decorated

###################################################################################################

####################################################################################################

