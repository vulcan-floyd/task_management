from sqlalchemy import UniqueConstraint, ForeignKeyConstraint
from enum import Enum

from extensions import db

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   public_id = db.Column(db.String(100), unique=True)
   email = db.Column(db.String(50), unique=True, nullable=False)
   name = db.Column(db.String(50))
   password = db.Column(db.String(100))
   admin = db.Column(db.Boolean)
#    __table_args__ = (UniqueConstraint("name", name="name"),)

class TaskStatus(Enum):
    NotPicked = 1
    InProgress = 2
    Completed = 3

class TaskPriority(Enum):
    Low = 1
    Medium = 2
    High = 3
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True, autoincrement=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.VARCHAR(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.Enum(TaskStatus))
    # status = db.Column(db.String(50))
    due_date = db.Column(db.DateTime)
    priority = db.Column(db.Enum(TaskPriority))
    __table_args__ = (UniqueConstraint("title", name="title"),)
    
    def __repr__(self) -> str:
        return f"{self.title}"