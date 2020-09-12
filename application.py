from utilities.flask_configs import app, db, Api, jsonify, request
from flask_cors import CORS

import pymysql
from sqlalchemy import desc

pymysql.install_as_MySQLdb()

from sitecontrollers.Adidas import Adidas
from sitecontrollers.Eastbay import Eastbay
from sitecontrollers.Footlocker import Footlocker
from sitecontrollers.Champssports import Champssports

from models.profile_model import Profile, profile_schema, profiles_schema
from models.task_model import Task, task_schema, tasks_schema
from models.user_model import User, users_schema, users_schema

CORS(app)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/fillybot'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hams4444@sneakerbot.ciiwjmf6az4h.us-west-2.rds.amazonaws.com/fillybot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.create_all()
# adidas = Adidas()
# eastbay = Eastbay()
# footlocker = Footlocker()
# champssports = Champssports()

from controllers.Register import Register
from controllers.Login import Login
from controllers.AddProfile import AddProfile
from controllers.AddTask import AddTask
from controllers.UpdateTask import UpdateTask
from controllers.DeleteTask import DeleteTask
from controllers.UpdateProfile import UpdateProfile
from controllers.DeleteProfile import DeleteProfile
from controllers.PurchaseAdidas import PurchaseAdidas
from controllers.PurchaseEastbay import PurchaseEastbay
from controllers.PurchaseFootlocker import PurchaseFootlocker
from controllers.PurchaseChampssports import PurchaseChampssports

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(AddTask, '/addtask')
api.add_resource(AddProfile, '/addprofile')
api.add_resource(UpdateTask, '/updatetask/<string:id>')
api.add_resource(DeleteTask, '/deletetask/<string:id>')
api.add_resource(UpdateProfile, '/updateprofile/<string:id>')
api.add_resource(DeleteProfile, '/deleteprofile/<string:id>')
api.add_resource(PurchaseAdidas, '/adidas')
api.add_resource(PurchaseEastbay, '/eastbay')
api.add_resource(PurchaseFootlocker, '/footlocker')
api.add_resource(PurchaseChampssports, '/champssports')

@app.route('/', methods=['GET'])
def hello_world():
  return "Hello World!"


@app.route('/fetchalluserprofiles/<id>', methods=['GET'])
def get_profiles(id):
  all_profiles = Profile.query.filter_by(user=id).all()
  profiles = profiles_schema.dump(all_profiles)
  return jsonify({'success': True, 'profiles': profiles}), 200


@app.route('/fetchallusertasks/<id>', methods=['GET'])
def get_tasks(id):
  all_tasks = Task.query.filter_by(user=id).order_by(Task.id.desc()).all()
  tasks = tasks_schema.dump(all_tasks)
  return jsonify({'success': True, 'tasks': tasks}), 200


if __name__  == "__main__":
  print('\n')
  app.run(debug=True, use_reloader=True, threaded=True)
