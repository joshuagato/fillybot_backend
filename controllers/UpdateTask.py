from utilities.flask_configs import Resource, db, request, jsonify, make_response
from models.task_model import Task, task_schema, tasks_schema

class UpdateTask(Resource):
  def put(self, id):
    fetched_task = Task.query.get(id)
    if not fetched_task:
      return make_response(jsonify({'success': False, 'messgae': 'Task not found'}), 401)

    if request.method == 'PUT':
      if request.is_json:
        fetched_task.user = request.json['user'] if request.json['user'] else fetched_task.user
        fetched_task.website = request.json['productsite'] if request.json['productsite'] else fetched_task.website
        fetched_task.prod_name = request.json['productname'] if request.json['productname'] else fetched_task.prod_name
        fetched_task.prod_number = request.json['productnumber'] if request.json['productnumber'] else fetched_task.prod_number
        fetched_task.prod_size = request.json['productsize'] if request.json['productsize'] else fetched_task.prod_size
        fetched_task.prod_qty = request.json['productquantity'] if request.json['productquantity'] else fetched_task.prod_qty
        fetched_task.profile = request.json['profile'] if request.json['profile'] else fetched_task.profile
        fetched_task.status = request.json['status'] if request.json['status'] else fetched_task.status

        db.session.commit()
        task = task_schema.dump(fetched_task)
        return make_response(jsonify({'success': True, 'task': task}), 201)
      else:
        return make_response(jsonify({'success': False, 'message': 'Your request data must be jsonified'}))
    else:
      return make_response(jsonify({'success': False, 'message': 'Your request header must be put'}))
