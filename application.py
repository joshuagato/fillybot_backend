from utilities.flask_configs import app, db, Api, jsonify, request
from flask_cors import CORS

import pymysql
from sqlalchemy import desc

pymysql.install_as_MySQLdb()

from sitecontrollers.Adidas import Adidas
from sitecontrollers.Eastbay import Eastbay

from models.profile_model import Profile, profile_schema, profiles_schema
from models.task_model import Task, task_schema, tasks_schema
from models.user_model import User, users_schema, users_schema

CORS(app)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/fillybot'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hams4444@sneakerbot.ciiwjmf6az4h.us-west-2.rds.amazonaws.com/fillybot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.create_all()
adidas = Adidas()
eastbay = Eastbay()

from controllers.Register import Register
from controllers.Login import Login
from controllers.AddProfile import AddProfile
from controllers.AddTask import AddTask
from controllers.DeleteTask import DeleteTask
from controllers.UpdateProfile import UpdateProfile
from controllers.DeleteProfile import DeleteProfile

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(AddProfile, '/addprofile')
api.add_resource(AddTask, '/addtask')
api.add_resource(DeleteTask, '/deletetask/<string:id>')
api.add_resource(UpdateProfile, '/updateprofile/<string:id>')
api.add_resource(DeleteProfile, '/deleteprofile/<string:id>')

@app.route('/', methods=['GET'])
def hello_world():
  return "Hello World!"


@app.route('/fetchalluserprofiles/<id>', methods=['GET'])
def get_profiles(id):
    all_profiles = Profile.query.filter_by(user=id).all()
    profiles = profiles_schema.dump(all_profiles)
    return jsonify({ 'success': True, 'profiles': profiles }), 200


@app.route('/fetchallusertasks/<id>', methods=['GET'])
def get_tasks(id):
    all_tasks = Task.query.filter_by(user=id).order_by(Task.id.desc()).all()
    tasks = tasks_schema.dump(all_tasks)
    return jsonify({ 'success': True, 'tasks': tasks }), 200


@app.route('/adidas', methods=['POST'])
def purchase_adidas():
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
                'phone': request.json['phone'], 'email': request.json['email'],
                'card_number': request.json['card_number'], 'card_holder': request.json['card_name'],
                'card_expiry': request.json['card_expiry'], 'card_cvv': request.json['card_cvv'],
            }

    message = adidas.generate_url(product_details, user_details)
    response = {'message': message}
    return jsonify(response), 200


@app.route('/eastbay', methods=['POST'])
def purchase_eastbay():
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
                'phone': request.json['phone'], 'email': request.json['email'],
                'card_number': request.json['card_number'], 'card_holder': request.json['card_name'],
                'card_expiry': request.json['card_expiry'], 'card_cvv': request.json['card_cvv'],
            }

    message = eastbay.generate_url(product_details, user_details)
    response = {'message': message}
    return jsonify(response), 200


if __name__  == "__main__":
    print('\n')
    app.run(debug=True, use_reloader=True, threaded=True)
