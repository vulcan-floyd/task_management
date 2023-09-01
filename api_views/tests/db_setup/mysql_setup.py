import json
from os import abort

from models.model import User, Task
from extensions import db

import pymysql


def mysql_setup():
    Task.query.delete()
    User.query.delete()
    
    file2 = open(f'api_views/tests/db_setup/db_users.json',)
    file_json = json.load(file2)
    for user in file_json['users']:
        id = user['id']
        public_id = user['public_id']
        name = user['name']
        password = user['password']
        admin = user['admin']
        t = User(id=id,
                 public_id=public_id,
                 name=name,
                 password=password,
                 admin=admin)
        db.session.add(t)
        db.session.commit()

    file = open(f'api_views/tests/db_setup/db_tasks.json',)
    file_json = json.load(file)
    for task in file_json['tasks']:
        id = task['id']
        title = task['title']
        description = task['description']
        status = task['status']
        due_date = task['due_date']
        user_id = task['user_id']
        t = Task(id=id,
                 title=title,
                 description=description,
                 status=status,
                 user_id=user_id,
                 due_date=due_date)
        db.session.add(t)
        db.session.commit()
        

if __name__ == '__main__':
    mysql_setup()
    
    