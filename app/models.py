"""Tables created by sql/create_tables.sql, mapped for use in the app."""
from datetime import datetime

from app import db


class Department(db.Model):
    __tablename__ = "department"
    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(50), nullable=False, unique=True)


class ITUser(db.Model):
    __tablename__ = "it_user"
    it_user_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)


class Ticket(db.Model):
    __tablename__ = "ticket"
    ticket_id = db.Column(db.Integer, primary_key=True)
    staff_name = db.Column(db.String(50), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("department.department_id"), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    status = db.Column(db.String(15), nullable=False, default="Open")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    assigned_to = db.Column(db.Integer, db.ForeignKey("it_user.it_user_id"))

    department = db.relationship("Department")
    assignee = db.relationship("ITUser")

    @property
    def number(self):
        return f"ITS-{self.ticket_id:04d}"
