from datetime import datetime

from marshmallow import Schema, fields

from setup_dp import db


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    date = db.Column(db.String(150))
    name_of_teacher = db.Column(db.String(150))
    class_number = db.Column(db.Integer())


class ScheduleSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    date = fields.String()
    name_of_teacher = fields.String()
    class_number = fields.Integer()


