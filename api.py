from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db';

db = SQLAlchemy(app)

class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_description = db.Column(db.String(200))
    task_name = db.Column(db.String(200))
    is_done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Task({self.task_name}, {self.task_description}, {self.is_done})"
    
task_args = reqparse.RequestParser()
task_args.add_argument("task_description", type=str, help="Task description", required=True)
task_args.add_argument("task_name", type=str, help="Task name", required=True)

taskFields = {
    'id': fields.Integer,
    'task_description': fields.String,
    'task_name': fields.String,
    'is_done': fields.Boolean
}

class Task(Resource):
    @marshal_with(taskFields)
    def get(self):
        tasks = TaskModel.query.all()
        return tasks
    
    # @marshal_with(taskFields)
    def post(self):
        args = task_args.parse_args()
        task = TaskModel(task_description=args['task_description'], task_name=args['task_name'], is_done=False)
        db.session.add(task)
        db.session.commit()
        tasks = TaskModel.query.all()
        # return tasks, 201
        return f"{args['task_name']} has been added", 201
    
api.add_resource(Task, '/api/tasks/')


@app.route('/')

def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run(port=5001, debug=True)
    # app.run(port=5001)
