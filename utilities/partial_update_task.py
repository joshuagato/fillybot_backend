from utilities.flask_configs import db
from models.task_model import Task, task_schema

def partial_update_task(task_id, status_message):
  fetched_task = Task.query.get(task_id)
  if not fetched_task:
    return False
    
  fetched_task.status = status_message

  db.session.commit()
  task_schema.dump(fetched_task)
  return True