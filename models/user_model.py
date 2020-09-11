from utilities.flask_configs import db, ma

# User Model
class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(60))
  lastname = db.Column(db.String(60))
  email = db.Column(db.String(120))
  password = db.Column(db.String(120))

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.password = password


# User Schema
class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'firstname', 'lastname', 'email')


# Init Schemma
user_schema = UserSchema()
users_schema = UserSchema(many=True)
