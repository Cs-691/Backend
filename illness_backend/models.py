from datetime import datetime
from illness_backend import db,ma



class User(db.Model):
    __tablename__ = 'user'
    
    firstName = db.Column(db.String(80))
    lastName = db.Column(db.String(80))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(80))
    email = db.Column(db.String(120),primary_key=True)
    password = db.Column(db.String(120))
    diabetes= db.Column(db.String(120))
    smoke= db.Column(db.String(120))
    bloodPressure= db.Column(db.String(120))
 
    def __init__(self, firstName, lastName,age,gender,email,password,diabetes,smoke,bloodPressure):
        self.firstName = firstName
        self.lastName = lastName
        self.age=age
        self.gender=gender
        self.email=email
        self.password=password
        self.diabetes=diabetes
        self.smoke=smoke
        self.bloodPressure=bloodPressure
        
    def __repr__(self):
        return f"User('{self.firstName}', '{self.lastName}', '{self.email}')"

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('firstName', 'lastName','age','gender','email','password','diabetes','smoke','bloodPressure')



