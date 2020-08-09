from utilities.flask_configs import db, ma

# Profile Model
class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    profile_name = db.Column(db.String(60))
    firstname = db.Column(db.String(60))
    lastname = db.Column(db.String(60))
    address = db.Column(db.String(60))
    city = db.Column(db.String(60))
    state = db.Column(db.String(60))
    zipcode = db.Column(db.String(60))
    phone = db.Column(db.String(60))
    email = db.Column(db.String(120))

    def __init__(self, user, profile_name, firstname, lastname, address, city, state, zipcode, phone, email):
        self.user = user
        self.profile_name = profile_name
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone
        self.email = email


# Profile Schema
class ProfileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'profile_name', 'firstname', 'lastname', 'address', 'city', 'state', 'zipcode', 'phone', 'email')


# Init Schemma
profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)
