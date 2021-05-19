from fastapi import APIRouter,Request,HTTPException

auth=APIRouter()

current_num=[0]
@auth.get("/api", )
async def index(request: Request):
    return "nothing"



# @auth.route('/register')
# class UserRegisterRoute(Resource):
    
#     @uapi.expect(UserRegister.user)
#     def post(self):
#         #print(current_app.config['SECRET_KEY'])
#         #print(request.data)
#         form=RegisterForm()

#         #print(request.headers)
#         if form.validate():
#             try:
#                 if not User.query.filter_by(email=form.data['email']).first():
#                     user=User(username=form.data['username'],first_name=form.data['first_name'],middle_name=form.data['middle_name'],last_name=form.data['last_name'],\
#                         email=form.data['email'])
#                     #user.password=
#                     user.password=pbkdf2_sha512.using(rounds=25000,salt_size=80).hash(form.data['password'])
#                     db.session.add(user)
#                     db.session.commit()
                
#                     #####################################################################
#                     #this is confirmation message section
#                     exp=datetime.datetime.utcnow()+datetime.timedelta(hours=24)
#                     key=current_app.config['SECRET_KEY']
#                     data={'user' :form.data['username'] ,'email':form.data['email']}
#                     contoken=generate_token(data=data,key=key,exp=exp)
                
#                     msg=Message(recipients=[form.data['email']])
#                     msg.subject='Welcome,this is confirmation Email'
#                     msg.html=f'<h1>Hello {form.data["first_name"]} {form.data["last_name"]}<h1> <br /> \
#                     <p>please follow the link below to confirm your registration,this link will expire after one day<p><br/> \
#                     <a href={request.base_url[:-8]+"confirm/"+contoken}>{form.data["email"]} </a>'
#                     # try:
#                     #     mail.send(msg)
#                     # except:
#                     #     pass
                
#                     #####################################################################
#                     #return {'message':'user has been registerd sucessfully '},201
#                     ################################################################################
#                     #disable the line below for production use the above return line, this one is for testing purposes only
#                     return {'message':contoken},201
#                 else:
#                     return {'message':'there was server internal error'},400
#             except Exception as e:
#                 db.session.rollback()
#                 #print('#####################################################################6')
#                 #print(f'the error that occured is {e}')
#                 return {'message':'there was server internal error'},500
#             finally:
#                 db.session.close()
    
   
# ##########################################################################################
