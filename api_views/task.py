from flask import current_app, jsonify, Blueprint, request
from datetime import datetime
from flasgger.utils import swag_from

from extensions import db
from models.model import Task
from middleware import token_required

from utils.task_feed import create_task, getTaskById, getTask, getFilterTask, update_Task, delete_Task



api_task_blueprint = Blueprint('api_task_blueprint', __name__)



@swag_from("api_views/api_docs/task/task-create-tasks.yml")
@api_task_blueprint.route('/create', methods=['POST'])
@token_required
def createTask():
    content = request.get_json()
    if 'title' not in content:
        return jsonify(error=400, text="Please pass the title of task"), 400
    
    if 'description' not in content:
        return jsonify(error=400, text="Please pass the description of task"), 400
    
    if 'due_date' not in content:
        return jsonify(error=400, text="Please pass the due_date of task"), 400
    
    task = create_task(content)
    if task == 'IntegrityError':
        return jsonify(text='Created Task is Already Exist')
    return jsonify({'status_code': 201, 'data': task.title})




@swag_from("api_views/api_docs/task/task-id-tasks.yml")
@api_task_blueprint.route('/<task_id>/tasks', methods=['GET'])
@token_required
def taskViewId(task_id):
    if not task_id.isdigit():
        return jsonify(error=400, text='Invalid TaskId'), 400
    
    data = getTaskById(task_id)
    if len(data) == 0:
        return jsonify(error=404, text='No Task found for given Id'), 404
    return jsonify({'tasks': data})
   
   
   
   
@swag_from("api_views/api_docs/task/task-tasks.yml")
@api_task_blueprint.route('/tasks', methods=['GET'])
@token_required
def taskView():
    page = int(request.args.get('page', 1))
    count = int(request.args.get('count', 2))
    data = getTask(page, count)
    
    if len(data) == 0:
        return jsonify(error=404, text='No Task found for User'), 404
    return jsonify({'tasks': data})



@swag_from("api_views/api_docs/task/task-filter-tasks.yml")
@api_task_blueprint.route('/filter/tasks', methods=['GET'])
@token_required
def taskFilterView():
    status = request.args.get('status', 'NotPicked')
    dueDate = request.args.get('due_date', str(datetime.now()))
    # date = dueDate.split('-')
    # dueDate = datetime(int(date[0]), int(date[1]),int(date[2]))
    data = getFilterTask(status)
    
    if len(data) == 0:
        return jsonify(error=404, text='No Task found for given Filter'), 404
    return jsonify({'tasks': data})



@swag_from("api_views/api_docs/task/task-id-update.yml")
@api_task_blueprint.route('/<task_id>/update', methods=['PUT'])
@token_required
def updateTask(task_id):
    content = request.get_json()
    
    task = update_Task(content, task_id)
    
    if not task:
        return jsonify(error=404, text='No Task Found'), 404
    return jsonify({'text': "Task has been Updated"})



@swag_from("api_views/api_docs/task/task-id-delete.yml")
@api_task_blueprint.route('/<task_id>/delete', methods=['DELETE'])
@token_required
def deleteTask(task_id):
    task = delete_Task(task_id)
    if not task:
        return jsonify(error=404, text='No Task Found'), 404
    return jsonify({'text': "Task has been Deleted"})

