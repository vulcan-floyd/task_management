from datetime import datetime
from flask import current_app, g, abort
import uuid
from sqlalchemy import exc

from models.model import Task, User
from extensions import db


def create_task(content):
    title = content['title']
    description = content['description']
    due_date = content['due_date']
    date = due_date.split('-')
    due_date = datetime(int(date[0]), int(date[1]),int(date[2]))
    user_id = g.user_id
    try:
        task = Task(title=title,
                    description=description,
                    status='NotPicked',
                    user_id=user_id,
                    due_date=due_date)
        db.session.add(task)
        db.session.commit()
        return task
    except exc.IntegrityError:
        db.session.rollback()
        return exc.IntegrityError.__name__
    
def getTaskById(task_id):
    user_id = g.user_id
    task = Task.query.filter_by(user_id=user_id, id=task_id).first()
    data = {}
    if task:
        data['id'] = task.id
        data['title'] = task.title
        data['description'] = task.description
        data['status'] = task.status.name
        data['due_date'] = task.due_date
    return data

def getTask(page, count):
    user_id = g.user_id
    task = Task.query.filter_by(user_id=user_id).paginate(page=page,per_page=count,error_out=False)
    output = []
    if task:
        for t in task:
            data = {}
            data['id'] = t.id
            data['title'] = t.title 
            data['description'] = t.description
            data['status'] = t.status.name
            data['due_date'] = t.due_date
            output.append(data)
    
    return output

def getSortTask(sort_by, page, count):
    user_id = g.user_id
    if sort_by == 'title':
        tasks = Task.query.order_by(Task.title).paginate(page=page,per_page=count,error_out=False)
    elif sort_by == 'id':
        tasks = Task.query.order_by(Task.id).paginate(page=page,per_page=count,error_out=False)
    
    output = []
    if tasks:
        for t in tasks:
            data = {}
            data['id'] = t.id
            data['title'] = t.title 
            data['status'] = t.status.name
            output.append(data)
    return output
    
def getFilterTask(status):
    user_id = g.user_id
    task = Task.query.filter_by(user_id=user_id, status=status).all()
    output = []
    if task:
        for t in task:
            data = {}
            data['id'] = t.id
            data['title'] = t.title 
            data['status'] = t.status.name
            output.append(data)
    return output
    
def update_Task(content, task_id):
    user_id = g.user_id
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return False
    if 'status' in content:
        status = content['status']
        task.status = status
    if 'due_date' in content:
        due_date = content['due_date']
        task.due_date = due_date
    db.session.commit()
    return True

def delete_Task(task_id):
    user_id = g.user_id
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return False
    
    db.session.delete(task)
    db.session.commit()
    return True