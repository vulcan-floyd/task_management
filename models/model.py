from extensions import db
from enum import Enum

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   public_id = db.Column(db.String(100), unique=True)
   name = db.Column(db.String(50))
   password = db.Column(db.String(100))
   admin = db.Column(db.Boolean)

class TaskStatus(Enum):
    NotPicked = 1
    InProgress = 2
    Completed = 3

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.VARCHAR(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.Enum(TaskStatus))
    # status = db.Column(db.String(50))
    due_date = db.Column(db.DateTime)
    
    def __repr__(self) -> str:
        return f"{self.title}"