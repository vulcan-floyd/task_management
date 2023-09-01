from flask import current_app, jsonify, Blueprint, request
from extensions import db
from models.model import Task
from datetime import datetime
from flasgger.utils import swag_from

from middleware import token_required

api_task_blueprint = Blueprint('api_task_blueprint', __name__)

@swag_from("api_views/api_docs/task/task-create-tasks.yml")
@api_task_blueprint.route('/create', methods=['POST'])
@token_required
def createTask(current_user):
    content = request.get_json()
    title = content['title']
    description = content['description']
    due_date = content['due_date']
    date = due_date.split('-')
    due_date = datetime(int(date[0]), int(date[1]),int(date[2]))
    user_id = current_user.id
    task = Task(title=title,
                description=description,
                status='NotPicked',
                user_id=user_id,
                due_date=due_date)
    db.session.add(task)
    db.session.commit()
    return jsonify({'status_code': 201, 'data': task.title})

@swag_from("api_views/api_docs/task/task-id-tasks.yml")
@api_task_blueprint.route('/<task_id>/tasks', methods=['GET'])
@token_required
def taskViewId(current_user, task_id):
    print(current_user, task_id)
    task = Task.query.filter_by(user_id=current_user.id, id=task_id).first()
    if not task:
        return jsonify(error=404, text='No Task Found with given ID'), 404
    
    
    data = {}
    data['id'] = task.id
    data['title'] = task.title
    data['description'] = task.description
    # data['status'] = task.status
    data['due_date'] = task.due_date
    print(data)
    return jsonify({'tasks': data})
   
@swag_from("api_views/api_docs/task/task-tasks.yml")
@api_task_blueprint.route('/tasks', methods=['GET'])
@token_required
def taskView(current_user):
    page = int(request.args.get('page', 1))
    count = int(request.args.get('count', 2))
    task = Task.query.filter_by(user_id=current_user.id).paginate(page=page,per_page=count,error_out=False)
    output = []
    for t in task:
        data = {}
        data['id'] = t.id
        data['title'] = t.title
        output.append(data)
    
    return jsonify({'tasks': output})

@swag_from("api_views/api_docs/task/task-filter-tasks.yml")
@api_task_blueprint.route('/filter/tasks', methods=['GET'])
@token_required
def taskFilterView(current_user):
    status = request.args.get('status', 'NotPicked')
    dueDate = request.args.get('due_date', str(datetime.now()))
    # date = dueDate.split('-')
    # dueDate = datetime(int(date[0]), int(date[1]),int(date[2]))
    task = Task.query.filter_by(user_id=current_user.id, status=status).all()
    output = []
    for t in task:
        data = {}
        data['id'] = t.id
        data['title'] = t.title
        output.append(data)
    
    return jsonify({'tasks': output})

@swag_from("api_views/api_docs/task/task-id-update.yml")
@api_task_blueprint.route('/<task_id>/update', methods=['PUT'])
@token_required
def updateTask(current_user, task_id):
    content = request.get_json()
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if not task:
        return jsonify(error=404, text='No Task Found'), 404
    
    if 'status' in content:
        status = content['status']
        task.status = status
    if 'due_date' in content:
        due_date = content['due_date']
        task.due_date = due_date
    db.session.commit()
    
    return jsonify({'text': "Task has been updated"})

@swag_from("api_views/api_docs/task/task-id-delete.yml")
@api_task_blueprint.route('/<task_id>/delete', methods=['DELETE'])
@token_required
def deleteTask(current_user, task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if not task:
        return jsonify(error=404, text='No Task Found'), 404
    
    db.session.delete(task)
    db.session.commit()
    return jsonify({'text': 'Task is Deleted'})

