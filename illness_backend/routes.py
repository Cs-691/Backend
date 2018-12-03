from flask import Flask, request, jsonify
from illness_backend import app,db
from illness_backend.models import User,UserSchema
from illness_backend.algorithm import Algorithm



user_schema = UserSchema()
users_schema = UserSchema(many=True)

# endpoint to create new user
@app.route("/api/user/signup/", methods=["POST"])
def add_user():
    firstName = request.json['fname']
    lastName = request.json['lname']
    age = request.json['age']
    gender = request.json['gender']
    email = request.json['email']
    password = request.json['password']
    
    
    User1 = User.query.filter_by(email=email).first()
    if(User1 is None):
        new_user = User(firstName, lastName,age,gender,email,password)
    
        db.session.add(new_user)
        db.session.commit()
    
        return email+str(age);
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
        response="user found",
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

    db.session.commit()
    response = app.response_class(
        response="Password Updated",
        status=200)
    return response


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)


@app.route("/api/chat/response/<message>", methods=["GET"])
def chat_response(message):
  #  user = User.query.get(message)
        c=Algorithm()
        x=[]
        x.append('extra_marital_contacts')
        x.append('shivering')
        x.append('joint_pain')
        x.append('visual_disturbances')
        x.append('irritability')
        x.append('depression')
        x.append('stiff_neck')
        x.append('excessive_hunger')
        illness=c.predict(x)
        response = app.response_class(
        response=illness,
        status=200)
        return response

@app.route('/')
def hello_world():
        chat_response("as")
        return 'Hello, World12qw'
