
from . import *

###########################################################################
    #this is the user method along with the user model methods
##########################################################################
class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True,autoincrement="auto")
    email=Column(String(255), unique=True,nullable=False)
    username =Column(String(100),unique=True,nullable=False)
    first_name =Column(String(100),nullable=False)
    middle_name = Column(String(100),nullable=False)
    last_name= Column(String(100),nullable=False)
    password = Column(String(500),nullable=False)
    date_registerd=Column(DateTime(),default=datetime.datetime.now())
    confirmed_at=Column(DateTime(),nullable=True)
    active = Column(Boolean(),default=False)
    roles = relationship('Role', secondary='roles_users',backref=backref('users',cascade="all", lazy='dynamic'))
   
         
    #pbkdf2_sha512.verify(password,self.password_hash)


    def __repr__(self):
        return f"<User '{self.username}'>"


#############################################################################
    #this is roles table along with its methods
############################################################################
class Role(db.Model):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True,autoincrement="auto")
    name = Column(String(80), unique=True)
    description = Column(String(255))

    def __repr__(self):
        return f"{self.name}"
#############################################################################
###########################################################################
    #this is for many to many roles models relationship 
############################################################################
class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(Integer(), primary_key=True)
    user_id = db.Column('user_id', Integer(), ForeignKey('user.id'))
    role_id = db.Column('role_id', Integer(), ForeignKey('role.id'))
    #users = relationship('User',backref=backref('users', lazy='dynamic'))

    def __repr__(self):
        return f"<UserRole '{self.role_id}'>"


######################################################################################################################################################
    #after this section marshmallow modle schemas can be definded
#######################################################################################################################################################
class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Role
        fields = ('name','description')
###########################################################################################
class UserSchema(ma.SQLAlchemyAutoSchema):
    #Nested(RoleSchema, many=True)
    roles=ma.Nested(RoleSchema(only=("name",)), many=True)
    class Meta:
        
        model=User
        #fields = ('id', 'username', 'first_name', 'last_name','email','pictures','contacts')
        fields = ('id', 'username', 'first_name', 'last_name','email','roles')

#################################################################################################

