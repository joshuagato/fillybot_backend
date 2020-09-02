from utilities.flask_configs import db, ma

# Profile Model
class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    profile_name = db.Column(db.String(60))
    firstname = db.Column(db.String(60))
    lastname = db.Column(db.String(60))
    address_1 = db.Column(db.String(120))
    address_2 = db.Column(db.String(120))
    city = db.Column(db.String(60))
    state = db.Column(db.String(60))
    zipcode = db.Column(db.String(60))
    phone = db.Column(db.String(60))
    email = db.Column(db.String(120))
    card_number = db.Column(db.String(120))
    card_name = db.Column(db.String(120))
    card_expiry = db.Column(db.String(120))
    card_cvv = db.Column(db.String(120))

    def __init__(self, user, profile_name, firstname, lastname, address_1, address_2, city, state, zipcode, phone, email, card_number, card_name, card_expiry, card_cvv):
        self.user = user
        self.profile_name = profile_name
        self.firstname = firstname
        self.lastname = lastname
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone
        self.email = email
        self.card_number = card_number
        self.card_name = card_name
        self.card_expiry = card_expiry
        self.card_cvv = card_cvv



# Profile Schema
class ProfileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'profile_name', 'firstname', 'lastname', 'address_1', 'address_2', 'city', 'state', 'zipcode', 'phone', 'email', 'card_number', 'card_name', 'card_expiry', 'card_cvv')


# Init Schemma
profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)
