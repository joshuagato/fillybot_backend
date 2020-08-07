from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pymysql
from sqlalchemy import desc
import bcrypt
# from flask.ext.bcrypt import Bcrypt
from flask_bcrypt import Bcrypt
from utilities.jsonwebtoken import verify_token
from kanpai import Kanpai

import jwt
import datetime

from controllers.adidas import Adidas

pymysql.install_as_MySQLdb()

# Init app
app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/fillybot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init Database
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)


# Task Model
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    website = db.Column(db.String(30))
    prod_name = db.Column(db.String(120))
    prod_number = db.Column(db.String(120))
    prod_size = db.Column(db.String(120))
    prod_qty = db.Column(db.Integer)
    profile = db.Column(db.Integer)

    def __init__(self, user, website, prod_name, prod_number, prod_size, prod_qty, profile):
        self.user = user
        self.website = website
        self.prod_name = prod_name
        self.prod_number = prod_number
        self.prod_size = prod_size
        self.prod_qty = prod_qty
        self.profile = profile


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


# User Model
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


# Task Schema
class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'website', 'prod_name', 'prod_number', 'prod_size', 'prod_qty', 'profile')


# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'firstname', 'lastname', 'email')


# Profile Schema
class ProfileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'profile_name', 'firstname', 'lastname', 'address', 'city', 'state', 'zipcode', 'phone', 'email')


# Init Schemma
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)
profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)


schema = Kanpai.Object({
    'firstname': (Kanpai.String(error='User first name must be string.')
    .trim().required(error='Please provide user first name.')
    .max(60, error='Maximum allowed length is 60')),

    'lastname': (Kanpai.String(error='User last name must be string.')
    .trim().required(error='Please provide user first name.')
    .max(60, error='Maximum allowed length is 60')),

    'email': (Kanpai.Email(error='Please enter a valid email')
    .trim().required(error='Please provide user email.')),

    'password': (Kanpai.String(error='Password must be alphanumeric.')
    .max(30, 'Maximum allowed password length is 30'))
})


db.create_all()
adidas = Adidas()

@app.route('/', methods=['GET'])
def hello_world():
  return "Hello World!"


@app.route('/register', methods=['POST'])
def register_user():
    if request.method == 'POST':
        if request.is_json:
            firstname = request.json['firstname']
            lastname = request.json['lastname']
            email = request.json['email']
            password = request.json['password']
            repassword = request.json['repassword']
            hashed_password = bcrypt.generate_password_hash(password)

            validation_result = schema.validate({
              'firstname': firstname,
              'lastname': lastname,
              'email': email,
              'password': password
            })

    if not validation_result['success']:
        return jsonify(validation_result.get('error'))

    matched_user = User.query.filter_by(email=email).first()
    if matched_user:
        return jsonify({ 'success': False, 'message': 'An account already exists with this email.' });

    new_user = User(firstname, lastname, email, hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({ 'success': True, 'message': 'Successfully Registered', 'user': user_schema.dump(new_user) }), 201


@app.route('/login', methods=['POST'])
def login_user():
    if request.method == 'POST':
        if request.is_json:
            email = request.json['email']
            password = request.json['password']

            matched_user = User.query.filter_by(email=email).first()
            if not matched_user:
                return jsonify({ 'success': False, 'message': 'Check your username or password' });

            hashed_password = matched_user.password

            if not bcrypt.check_password_hash(hashed_password, password):
                return jsonify({ 'success': False, 'message': 'Check your username or password' });

    token = jwt.encode({'user': user_schema.dump(matched_user)}, 'supersecretivesecret', algorithm='HS256')

    return jsonify({ 'success': True, 'user': user_schema.dump(matched_user), 'token': token.decode() }), 201


@app.route('/addprofile', methods=['POST'])
def add_profile():
    if request.method == 'POST':
        if request.is_json:
            user = request.json['user']
            profile_name = request.json['profile_name']
            firstname = request.json['firstname']
            lastname = request.json['lastname']
            address = request.json['address']
            city = request.json['city']
            state = request.json['state']
            zipcode = request.json['zipcode']
            phone = request.json['phone']
            email = request.json['email']

    new_profile = Profile(user, profile_name, firstname, lastname, address, city, state, zipcode, phone, email)
    db.session.add(new_profile)
    db.session.commit()
    return jsonify({ 'success': True, 'schema': profile_schema.dump(new_profile) }), 201


@app.route('/fetchalluserprofiles/<id>', methods=['GET'])
def get_profiles(id):
    all_profiles = Profile.query.filter_by(user=id).all()
    profiles = profiles_schema.dump(all_profiles)
    return jsonify({ 'success': True, 'profiles': profiles }), 200


@app.route('/updateprofile/<id>', methods=['PUT'])
def update_profile(id):
    fetched_profile = Profile.query.get(id)
    if request.method == 'PUT':
        if request.is_json:
            fetched_profile.user = request.json['user']
            fetched_profile.profile_name = request.json['profile_name']
            fetched_profile.firstname = request.json['firstname']
            fetched_profile.lastname = request.json['lastname']
            fetched_profile.address = request.json['address']
            fetched_profile.city = request.json['city']
            fetched_profile.state = request.json['state']
            fetched_profile.zipcode = request.json['zipcode']
            fetched_profile.phone = request.json['phone']
            fetched_profile.email = request.json['email']

    db.session.commit()
    profile = profile_schema.dump(fetched_profile)
    return jsonify({ 'success': True, 'profile': profile }), 201


@app.route('/deleteprofile/<id>', methods=['DELETE'])
def delete_profile(id):
    oneprofile = Profile.query.get(id)
    db.session.delete(oneprofile)
    db.session.commit()
    profile = profile_schema.dump(oneprofile)
    return jsonify({ 'success': True, 'profile': profile }), 201


@app.route('/addtask', methods=['POST'])
def add_task():
    if request.method == 'POST':
        if request.is_json:
            user = request.json['user']
            website = request.json['productsite']
            prod_name = request.json['productname']
            prod_number = request.json['productnumber']
            prod_size = request.json['productsize']
            prod_qty = request.json['productquantity']
            profile = request.json['profile']

    new_task = Task(user, website, prod_name, prod_number, prod_size, prod_qty, profile)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({ 'success': True , 'schema': task_schema.dump(new_task) }), 201


@app.route('/fetchallusertasks/<id>', methods=['GET'])
def get_tasks(id):
    all_tasks = Task.query.filter_by(user=id).order_by(Task.id.desc()).all()
    tasks = tasks_schema.dump(all_tasks)
    return jsonify({ 'success': True, 'tasks': tasks }), 200


@app.route('/deletetask/<id>', methods=['DELETE'])
def delete_task(id):
    onetask = Task.query.get(id)
    db.session.delete(onetask)
    db.session.commit()
    task = task_schema.dump(onetask)
    return jsonify({ 'success': True, 'task': task }), 201


@app.route('/adidas', methods=['POST'])
def fetch_url():
    if request.method == 'POST':
        if request.is_json:
            product_details = {
                'product_name': request.json['prod_name'], 'product_number': request.json['prod_number'],
                'product_size': request.json['prod_size'], 'product_quantity': request.json['prod_qty']
            }

            user_details = {
                'first_name': request.json['firstname'], 'last_name': request.json['lastname'],
                'address': request.json['address'], 'city': request.json['city'],
                'state': request.json['state'] , 'zipcode': request.json['zipcode'],
                'phone': request.json['phone'],'email': request.json['email'],
            }

    message = adidas.generate_url(product_details, user_details)
    response = { 'message': message }
    return jsonify(response), 200

    # response = {'message': message}
    # return jsonify(response), 200


if __name__  == "__main__":
    print('\n')
    app.run(debug=True, use_reloader=True, threaded=True)
