from flask import Flask, request, jsonify,json
from illness_backend import app,db
from illness_backend.models import User,UserSchema
from illness_backend.algorithm import Algorithm
from illness_backend.remedies import Remedies
from illness_backend.response import Response
from flask_mail  import Message
from illness_backend.verification import Verification


user_schema = UserSchema()
users_schema = UserSchema(many=True)
algo=Algorithm()
verify=Verification()
remedy=Remedies()





# endpoint to create new user
@app.route("/api/user/signup/", methods=["POST"])
def add_user():
    firstName = request.json['fname']
    lastName = request.json['lname']
    age = request.json['age']
    gender = request.json['gender']
    email = request.json['email']
    password = request.json['password']
    diabetes = request.json['diabetes']
    smoke = request.json['smoke']
    bloodPressure = request.json['bloodPressure']
    
    
    User1 = User.query.filter_by(email=email).first()
    if(User1 is None):
        new_user = User(firstName, lastName,age,gender,email,password,diabetes,smoke,bloodPressure)
    
        db.session.add(new_user)
        db.session.commit()
    
        return firstName;
    else:
        response = app.response_class(
        response="User with given email is already exist",
        status=409)
        return response


# endpoint to show all users
@app.route("/api/user/validate/", methods=["POST"])
def get_user():
    emailId = request.json['email']
    password = request.json['password']
    User1 = User.query.filter_by(email=emailId).first()
    if(User1.password==password):
        response = app.response_class(
        response=User1.firstName,
        status=200)
    else:
        response = app.response_class(
        response="user not found",
        status=404)
    return response
    

# endpoint to get user detail by id
@app.route("/api/user/getUserDetails/<email>", methods=["GET"])
def user_detail(email):
    user = User.query.get(email)
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/api/user/updateUser/", methods=["POST"])
def user_update():
    
    
    firstName = request.json['fname']
    lastName = request.json['lname']
    age = request.json['age']
    gender = request.json['gender']
    email = request.json['email']
    password = request.json['password']
    newPassword = request.json['npassword']
    diabetes = request.json['diabetes']
    smoke = request.json['smoke']
    bloodPressure = request.json['bloodPressure']
    
    
    
    user = User.query.get(email)
    
    if(password==newPassword):
        response = app.response_class(
        response="current password is same as new password ",
        status=409)
        return response
    
    if(newPassword==''):    
        user.password=password
    else:
        user.password = newPassword
        
        
    user.firstName=firstName;
    user.lastName=lastName;
    user.age=age;
    user.gender=gender;
    user.diabetes=diabetes
    user.smoke=smoke
    user.bloodPressure=bloodPressure

    db.session.commit()
    response = app.response_class(
        response="User Information Updated",
        status=200)
    return response


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

#@app.route("/api/user/updateUser/", methods=["POST"])
@app.route("/api/chat/response/", methods=["POST"])
def chat_response():
  #
        #print(request)
        req_data = request.get_json()
        x=  req_data
        print(x)
        algo.predict(x)
        verifiedIllness=verify.predict(x)
        algo.setIllness(verifiedIllness)
        remedies=get_remedies(algo.getIllness())
        predictedResponse=Response(algo.getIllness(),remedies,algo.getProbability())
        data=predictedResponse.toJSON()
        response = app.response_class(
        response=data,
        mimetype='application/json',
        status=200)
        return response
    
#@app.route("/api/user/updateUser/", methods=["POST"])
@app.route("/api/user/sendMessage/", methods=["POST"])
def store_message():
  #
        #print(request)
        req_data = request.get_json()
        x=  req_data
        print(x)
        f = open("C:\\Users\\Nirav\\Desktop\\waste\\illness_backend\\demofile.txt", "a")
        f.write("\r\n -------------------\r\n"+x+"\r\n--------------");
        return "message received!"


# endpoint to get user detail by id
@app.route("/api/user/getRemedies/<illness>", methods=["GET"])
def get_remedies(illness):
    illness=illness.lower()
    remedies=remedy.getRemedies(illness)
    return remedies


@app.route('/')
def hello_world():
        return 'Hello, World12qw'
