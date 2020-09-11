from utilities.flask_configs import Resource, db, request, jsonify, make_response
from models.task_model import Task, task_schema, tasks_schema

class AddTask(Resource):
  def post(self):
    if request.method == 'POST':
      if request.is_json:
        user = request.json['user']
        website = request.json['productsite']
        prod_name = request.json['productname']
        prod_number = request.json['productnumber']
        prod_size = request.json['productsize']
        prod_qty = request.json['productquantity']
        profile = request.json['profile']
        status = request.json['status']

        new_task = Task(user, website, prod_name, prod_number, prod_size, prod_qty, profile, status)
        db.session.add(new_task)
        db.session.commit()
        data = {'success': True , 'schema': task_schema.dump(new_task)}
        return make_response(jsonify(data), 201)
      else:
        return make_response(jsonify({'success': False, 'message': 'Your request data must be jsonified'}))
    else:
      return make_response(jsonify({'success': False, 'message': 'Your request header must be put'}))