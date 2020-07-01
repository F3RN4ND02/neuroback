from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Column = db.Column
String = db.String
Integer = db.Integer
DateTime = db.DateTime
Date = db.Date
Enum = db.Enum
Boolean = db.Boolean
ForeignKey = db.ForeignKey
session = db.session
Model = db.Model
relationship = db.relationship
Float = db.Float