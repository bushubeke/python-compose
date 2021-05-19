    
from . import *
###################################################################
#this section is to import related object for the route
from ..forms.auth_forms import RegisterForm,TokenLoginForm,ResendConfirmation,ChangePassword,UpdateUserForm,RemoveUserForm,   \
    RoleForm,UpadateRoleForm,RemoveRoleForm
from ..models.auth_models import *
##################################################################################
class UserRegister:
    api = Namespace('user', description='user registery')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'first_name': fields.String(required=True, description='first_name'),
        'middle_name': fields.String(required=True, description='middle_name'),
        'last_name': fields.String(required=True, description='last_name'),
        'password': fields.String(required=True, description='user password'),
        'confirm': fields.String(required=True, description='user password')
    })
    login = api.model('login', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
       
    })
    resend = api.model('resend_confirmation', {
        'email': fields.String(required=True, description='user email address'),
        
       
    })
    reset = api.model('reset_password', {
        'email': fields.String(required=True, description='user email address'),
        
       
    })
    change_password = api.model('reset_password', {
        'password': fields.String(required=True, description='user password'),
        'confirm': fields.String(required=True, description='user password')
       
    })
    update_user = api.model('update_password', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'first_name': fields.String(required=True, description='first_name'),
        'middle_name': fields.String(required=True, description='middle_name'),
        'last_name': fields.String(required=True, description='last_name')
       
    })
    remove = api.model('remove_user', {
        'email': fields.String(required=True, description='user email address'),
        
       
    })
    update_role = api.model('update_role', {
        'name': fields.String(required=True, description='user username'),
        'description': fields.String(required=True, description='first_name'),
       
    })
    role = api.model('add_role', {
        'name': fields.String(required=True, description='user username'),
        'description': fields.String(required=True, description='first_name'),
               
    })
    remove_role = api.model('add_role', {
        'name': fields.String(required=True, description='user username'),
        
    })

uapi=UserRegister.api
##########################################################################################
@uapi.route('/register')
class UserRegisterRoute(Resource):
    
    @uapi.expect(UserRegister.user)
    def post(self):
        #print(current_app.config['SECRET_KEY'])
        #print(request.data)
        form=RegisterForm()

        #print(request.headers)
        if form.validate():
            try:
                if not User.query.filter_by(email=form.data['email']).first():
                    user=User(username=form.data['username'],first_name=form.data['first_name'],middle_name=form.data['middle_name'],last_name=form.data['last_name'],\
                        email=form.data['email'])
                    #user.password=
                    user.password=pbkdf2_sha512.using(rounds=25000,salt_size=80).hash(form.data['password'])
                    db.session.add(user)
                    db.session.commit()
                
                    #####################################################################
                    #this is confirmation message section
                    exp=datetime.datetime.utcnow()+datetime.timedelta(hours=24)
                    key=current_app.config['SECRET_KEY']
                    data={'user' :form.data['username'] ,'email':form.data['email']}
                    contoken=generate_token(data=data,key=key,exp=exp)
                
                    msg=Message(recipients=[form.data['email']])
                    msg.subject='Welcome,this is confirmation Email'
                    msg.html=f'<h1>Hello {form.data["first_name"]} {form.data["last_name"]}<h1> <br /> \
                    <p>please follow the link below to confirm your registration,this link will expire after one day<p><br/> \
                    <a href={request.base_url[:-8]+"confirm/"+contoken}>{form.data["email"]} </a>'
                    # try:
                    #     mail.send(msg)
                    # except:
                    #     pass
                
                    #####################################################################
                    #return {'message':'user has been registerd sucessfully '},201
                    ################################################################################
                    #disable the line below for production use the above return line, this one is for testing purposes only
                    return {'message':contoken},201
                else:
                    return {'message':'there was server internal error'},400
            except Exception as e:
                db.session.rollback()
                #print('#####################################################################6')
                #print(f'the error that occured is {e}')
                return {'message':'there was server internal error'},500
            finally:
                db.session.close()
    
   
##########################################################################################            
@uapi.route('/confirm/<string:token>')    
class UserRegisterConfirmation(Resource):
    def get(self,token):
        data=None
        try:
            data = token_decode(data=token,key=current_app.config['SECRET_KEY'])
        except:
            pass
        if data:
            user=User.query.filter_by(email=data['data']['email']).first()
            if user.active:
                return {'message':'this user has already been confirmed'},204
            else:
                try:
                    user.confirmed_at=datetime.datetime.utcnow()
                    user.active=True
                    db.session.add(user)
                    db.session.commit()
                    return {'message':'yes this user has been confirmed'},201
                except:
                    db.session.rollback()
                    return {'message':'internal sever error occured,please try again later'},500
                finally:
                    db.session.close()
        else:
            return {'message':'the provided link is invalid'},403
        
##########################################################################################
@uapi.route('/login')    
class UserRegisterConfirmation(Resource):
    @uapi.expect(UserRegister.login)
    def post(self):
        form=TokenLoginForm()
               
        if form.validate():
            try:
                
                user=User.query.filter_by(email=form.data['email']).first()
               
                if  pbkdf2_sha512.verify(form.data['password'],user.password):
                    exp=datetime.datetime.utcnow()+datetime.timedelta(hours=5)
                    key=current_app.config['SECRET_KEY']
                    data={'user' : user.username,'email':user.email,'userid':user.id}
                    
                    token=generate_token(data=data,key=key,exp=exp)
                    #data = jwt.decode(token, app.config['SECRET_KEY'],algorithms="HS256")
                    #print(f'this is modified to show baseurl {request.base_url[:-5]+"confirm"}')
                    return {'token' : token,'user':user.username,'email':user.email, 'userid':user.id},201
                    #return {'yes':'it is working !'},201    
                else:
                    return {'invalid':'please enter valid credentials'},401
                #print(get_pw_context().verify(get_hmac(ppass),passwordhash))
                
            except:
                return {'message':'No such values'},404
        else:
            
            return {'message':'Illegall attempt inputing dubious values'},403
        #return {'message':'yes this has not been setup yet'},201
##########################################################################################
@uapi.route('/refresh')    
class UserRegisterConfirmation(Resource):
    #@token_required()
    def get(self):
        try:
            rtoken=None
            try:
                rtoken = request.headers['X-APP-KEY']
                #print(rtoken)
            except:
                return {'message' : 'Token is missing.'}, 401
            if rtoken: 
                try:
                    tokdata=token_decode(data=rtoken,key=current_app.config['SECRET_KEY'])
                    exp=datetime.datetime.utcnow()+datetime.timedelta(hours=5)
                    key=current_app.config['SECRET_KEY']
                    data=tokdata['data']
                    token=generate_token(data=data,key=key,exp=exp)
                    return {'token' : token,'user':data['user'],'email':data['email'], 'userid':data['userid']},201
                except Exception as e:
                  #print(e)
                  return {'message':'some error has occured, please contact administrator'},500
        except:
            pass
######################################################################################################################        
@uapi.route('/change')    
class UserPasswordChange(Resource):
    #@token_required()
    @uapi.expect(UserRegister.change_password)
    def post(self):
        form=ChangePassword()
        try:
            rtoken=None
        
            rtoken = request.headers['X-APP-KEY']
            #print(rtoken)
        
            if form.validate():    
                try:
                    tokdata=token_decode(data=rtoken,key=current_app.config['SECRET_KEY'])
                    user=User.query.filter_by(email=tokdata['data']['email']).first()
                    user.password=pbkdf2_sha512.using(rounds=25000,salt_size=80).hash(form.data['password'])
                    db.session.add(user)
                    db.session.commit()
                    return {'message':'sucessfuly changed password'},201
                except:
                    db.session.rollback()
                    return {'message':'this is invalid token, please contact administrator'},500
                finally:
                    db.session.close()
            else:
                return {'message':'Illegall attempt inputing dubious values'},403 
              
        except:
            return {'message' : 'Token is missing.'}, 401        

######################################################################################################################
@uapi.route('/resend')    
class UserConfirmationResend(Resource):
    #@token_required()
    @uapi.expect(UserRegister.resend)
    def post(self):
        form=ResendConfirmation()
        if form.validate():
                try:
                    #print(form.data['email'])
                    #db.session.rollback()
                    user=User.query.filter_by(email=form.data['email']).first()

                    exp=datetime.datetime.utcnow()+datetime.timedelta(hours=24)
                    key=current_app.config['SECRET_KEY']
                    data={'user' :user.username ,'email':user.email}
                    contoken=generate_token(data=data,key=key,exp=exp)
                    print(data)
                    print(contoken)
                    
                    #####################################################################################################################
                    
                    msg=Message(recipients=[form.data['email']])
                   
                    msg.subject='Welcome,this is confirmation Email'
                    
                    msg.html=f'<h1>Hello {user.first_name} {user.last_name}<h1> <br /> \
                    <p>please follow the link below to confirm your registration,this link will expire after one day<p><br/> \
                    <a href={request.base_url[:-6]+"confirm/"+contoken}>{form.data["email"]} </a>'
                   
                    # try:
                    #     mail.send(msg)
                    # except:
                    #     pass
                    #####################################################################
                   
                    return {'message':'confirmation link has been sent sucessfully'},201
                except Exception as e:
                    return {'message':'some kind of error occured,please try again later'},500
                    #return {'error':f'{e}'},500
        else:
           return {'message':'Illegall attempt inputing dubious values'},403 
###############################################################################################################################################

@uapi.route('/resetpassword')    
class UserResetPassword(Resource):
    #@token_required()
    @uapi.expect(UserRegister.reset)
    def post(self):
        form=ResendConfirmation()
        if form.validate():
            try:
                
                user=User.query.filter_by(email=form.data['email']).first()
                exp=datetime.datetime.utcnow()+datetime.timedelta(hours=24)
                key=current_app.config['SECRET_KEY']
                data={'user' :user.username ,'email':user.email}
                contoken=generate_token(data=data,key=key,exp=exp)
                
                #print(contoken)
                #####################################################################################################################
                
                return {'token': contoken },201
            except:
                return {'message':'some kind of error occured,please try again later '},500
        else:
            return {'message':'Illegall attempt inputing dubious values'},403 
###########################################################################################################################################

###########################################################################################################################################
@uapi.route('/user')
class UserOperations(Resource):
    def get(self):
    
        rtoken=None
        try:
            rtoken = request.headers['X-APP-KEY']
            #print(rtoken)
        except:
            return {'message' : 'Token is missing.'}, 401
    
        try:
            tokdata=token_decode(data=rtoken,key=current_app.config['SECRET_KEY'])
            users=User.query.all()
            user_mash=UserSchema(many=True)
            usersb=user_mash.dump(users)
                            
            return usersb,201
        except Exception as e:
            #print(e)
            return {'message':'some error has occured, please contact administrator'},500
        finally:
            db.session.close()
    
        
    @uapi.expect(UserRegister.update_user)
    def put(self):

        rtoken=None
        form=UpadateUserForm()
        try:
            rtoken = request.headers['X-APP-KEY']
            #print(rtoken)
        except:
            return {'message' : 'Token is missing.'}, 401
            
        try:
            tokdata=token_decode(data=rtoken,key=current_app.config['SECRET_KEY'])
            if rtoken and form.validate():
                User.query.filter_by(email=form.data['email']).update(**    form.data)
                db.session.add(role)
                db.session.commit()
                return {'message':'User updated sucessfully'},201
            else:
                return {'message':'something unexpected occured please contact administrator'}
        except:
            db.session.rollback()
            return {'message':'something occured error occured please contact administrator'},500
        finally:
            db.session.close()
    
        return {'message':'yes this user has been confirmed'},201
    @uapi.expect(UserRegister.remove)
    def delete(self):
        rtoken=None
        form=RemoveUserForm()
        try:
            rtoken = request.headers['X-APP-KEY']
            #print(rtoken)
        except:
            return {'message' : 'Token is missing.'}, 401
        
        try:
            tokdata=token_decode(data=rtoken,key=current_app.config['SECRET_KEY'])
            if rtoken and form.validate():
                user=User.query.filter_by(email=form.data['email']).first()
                db.session.delete(user)
                db.session.commit()
                return {'message':'Account has been removed sucessfuly'},201
            else:
                return {'message':'please input valid users'},404
        except:
            db.session.rollback()
            return {'message':'please input valid users'},404
        finally:
            db.session.close()
        
###########################################################################################################################################

###########################################################################################################################################
@uapi.route('/roles')
class RoleOperations(Resource):
    def get(self):
        token=None
        
        try:
            rtoken = request.headers['X-APP-KEY']
            #print(rtoken)
            tokdata=token_decode(data=rtoken,key=current_app.config['SECRET_KEY'])
            roles=User.query.all()
            role_mash=RoleSchema(many=True)
            rols=role_mash.dump(roles)
            return rols,201
        except:
            #db.session.rollback()
            return {'message' : 'Token is missing.'}, 401
        
        finally:
            db.session.close()
    @uapi.expect(UserRegister.role)
    def post(self):
        token=None
        form=RoleForm()
        try:
            rtoken = request.headers['X-APP-KEY']
            try:
                if rtoken and form.validate():
                    #role=Role(name=form.data['name'],description=form.data['description'])
                    role=Role(**form.data)
                    db.session.add(role)
                    db.session.commit()
                    return {'message':'role added sucessfully'},201
            except:
                db.session.rollback()
                return {'message':'something occured error occured please contact adminstrator'},500
            finally:
                db.session.close()
                #print(rtoken)
        except:
            return {'message' : 'Token is missing.'}, 401
            
       
    
        
    @uapi.expect(UserRegister.update_role)    
    def put(self):
        token=None
        form=UpadateRoleForm()
        try:
            rtoken = request.headers['X-APP-KEY']
            #print(rtoken)
        except:
            return {'message' : 'Token is missing.'}, 401
            
        try:
            if rtoken and form.validate():
                Role.query.filter_by(name=form.data['name']).update(**form.data)
                db.session.add(role)
                db.session.commit()
                return {'message':'role added sucessfully'},201 
            else:
                return {'message':'please input valid values or provide valid token'},201
        except:
            db.session.rollback()
            return {'message':'something occured error occured please contact adminstrator'},500
        finally:
            db.session.close()
    
        return {'message':'yes this user has been confirmed'},201
    @uapi.expect(UserRegister.remove_role)
    def delete(self):
        rtoken=None
        form=RemoveRoleForm()
        try:
            rtoken = request.headers['X-APP-KEY']
            #print(rtoken)
        except:
            return {'message' : 'Token is missing.'}, 401
        
        try:
            tokdata=token_decode(data=rtoken,key=current_app.config['SECRET_KEY'])
            if rtoken and form.validate():
                role=Role.query.filter_by(name=form.data['name']).first()
                db.session.delete(role)
                db.session.commit()
                return {'message':'Account has been removed sucessfuly'},201
            else:
                return {'message':'please input valid users'},404
        except:
            db.session.rollback()
            return {'message':'please input valid users'},404
        finally:
            db.session.close()
        return {'message':'yes this user has been confirmed'},201
###########################################################################################################################################

###########################################################################################################################################
@uapi.route('/adduserroles')
class ManageUserRole(Resource):
    def post(self):
        token=None
        form=RoleForm()
        try:
            rtoken = request.headers['X-APP-KEY']
            try:
                if rtoken and form.validate():
                    #role=Role(name=form.data['name'],description=form.data['description'])
                    role=Role(**form.data)
                    db.session.add(role)
                    db.session.commit()
                    return {'message':'role added sucessfully'},201
            except:
                db.session.rollback()
                return {'message':'something occured error occured please contact adminstrator'},500
            finally:
                db.session.close()
            
        except:
            return {'message' : 'Token is missing.'}, 401
            
        
         
    def put(self):
        # try:
        #     User.query.filter_by(id=1).update(data)
        #     db.session.commit()
        #     #or if relationship is like many to many and am adding user object
        #     role=Role.query.filter_by(name=form.data['role'])
        #     user=User.query.filter_by(email=forma.data['email'])
        #     user.roles.append(role)
        #     u1.roles.pop(0) to delete role from users  
        #     u1.roles.pop(u1.roles.index(r3)) to delete role from users
        #     r3=Role.query.filter_by(id=1)
        #     r3 in u1.roles

        # except:
        #     db.session.rollback()
        # finally
        #     db.session.close()
        return {'yes':'it is working'},200
    def delete(self):
        # try:
        #     User.query.filter_by(id=1).update(data)
        #     db.session.commit()
        #     #or if relationship is like many to many and am adding user object
        #     role=Role.query.filter_by(name=form.data['role'])
        #     user=User.query.filter_by(email=forma.data['email'])
        #     user.roles.append(role)
        #     u1.roles.pop(0) to delete role from users  
        #     u1.roles.pop(u1.roles.index(r3)) to delete role from users
        #     r3=Role.query.filter_by(id=1)
        #     r3 in u1.roles

        # except:
        #     db.session.rollback()
        # finally
        #     db.session.close()
        return {'yes':'it is working'},200  
