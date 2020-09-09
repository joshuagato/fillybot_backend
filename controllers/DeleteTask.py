from utilities.flask_configs import Resource, db, jsonify, make_response
from models.task_model import Task, task_schema, tasks_schema

class DeleteTask(Resource):
  def delete(self, id):
    onetask = Task.query.get(id)
    if not onetask:
      return make_response(jsonify({'success': False, 'messgae': 'Task not found'}), 401)

    db.session.delete(onetask)
    db.session.commit()
    task = task_schema.dump(onetask)

    return make_response(jsonify({ 'success': True, 'task': task }), 201)
