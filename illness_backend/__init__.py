from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS







app = Flask(__name__, instance_relative_config=True)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/test2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='false'
db = SQLAlchemy(app)
ma = Marshmallow(app)
db.init_app(app)



from illness_backend import routes