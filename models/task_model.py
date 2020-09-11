from utilities.flask_configs import db, ma

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
  status = db.Column(db.String(60))

  def __init__(self, user, website, prod_name, prod_number, prod_size, prod_qty, profile, status):
    self.user = user
    self.website = website
    self.prod_name = prod_name
    self.prod_number = prod_number
    self.prod_size = prod_size
    self.prod_qty = prod_qty
    self.profile = profile
    self.status = status


# Task Schema
class TaskSchema(ma.Schema):
  class Meta:
    fields = ('id', 'user', 'website', 'prod_name', 'prod_number', 'prod_size', 'prod_qty', 'profile', 'status')


# Init Schemma
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
