from . import db 
from flask_login import UserMixin


class PatientMoreDetail(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    blood_grp = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    dob = db.Column(db.String(10))
    diseases_symptoms = db.Column(db.String(500))
    surgries = db.Column(db.String(500))
    sensitivities = db.Column(db.String(500))
    radiograph_test = db.Column(db.String(500))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

class Patient(db.Model, UserMixin) :
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200),unique=True)
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    patient_more_detail =  db.relationship('PatientMoreDetail')




