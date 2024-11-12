from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app) 
api = Api(app)

class UserModel(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)
    nim = db.Column(db.Integer, unique=True, nullable=False)
    

    def repr(self): 
        return f"User(name = {self.name}, email = {self.email}),address = {self.address}, nim = {self.nim})"

user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_args.add_argument('email', type=str, required=True, help="Email cannot be blank")
user_args.add_argument('address', type=str, required=True, help="Address cannot be blank")
user_args.add_argument('nim', type=int, required=True, help="nim cannot be blank")


userFields = {
    'id':fields.Integer,
    'name':fields.String,
    'email':fields.String,
    'address':fields.String,
    'nim':fields.Integer
}

class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all() 
        return users 
    
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args["name"], email=args["email"], address=args["address"], nim=args["nim"])
        db.session.add(user) 
        db.session.commit()
        users = UserModel.query.all()
        return users, 201
    
class User(Resource):
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first() 
        if not user: 
            abort(404, message="User not found")
        return user 
    
    @marshal_with(userFields)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first() 
        if not user: 
            abort(404, message="User not found")
        user.name = args["name"]
        user.email = args["email"]
        user.address = args["address"]
        user.nim = args["nim"]
        db.session.commit()
        return user 
    
    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first() 
        if not user: 
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users

class nama(Resource):
    @marshal_with(userFields)
    def get(self, name):
        user = UserModel.query.filter_by(name=name).first() 
        if not user: 
            abort(404, message="User not found")
        return user 
    
    @marshal_with(userFields)
    def patch(self, name):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(name=name).first() 
        if not user: 
            abort(404, message="User not found")
        user.name = args["name"]
        user.email = args["email"]
        user.address = args["address"]
        user.nim = args["nim"]
        db.session.commit()
        return user 
    
    @marshal_with(userFields)
    def delete(self, name):
        user = UserModel.query.filter_by(name=name).first() 
        if not user: 
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users

class email(Resource):
    @marshal_with(userFields)
    def get(self, email):
        user = UserModel.query.filter_by(email=email).first() 
        if not user: 
            abort(404, message="User not found")
        return user 
    
    @marshal_with(userFields)
    def patch(self, email):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(email=email).first() 
        if not user: 
            abort(404, message="User not found")
        user.name = args["name"]
        user.email = args["email"]
        user.address = args["address"]
        user.nim = args["nim"]
        db.session.commit()
        return user 
    
    @marshal_with(userFields)
    def delete(self, email):
        user = UserModel.query.filter_by(email=email).first() 
        if not user: 
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users

class alamat(Resource):
    @marshal_with(userFields)
    def get(self, address):
        user = UserModel.query.filter_by(address=address).all() 
        if not user: 
            abort(404, message="User not found")
        return user 
    
    @marshal_with(userFields)
    def patch(self, address):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(address=address).first() 
        if not user: 
            abort(404, message="User not found")
        user.name = args["name"]
        user.email = args["email"]
        user.address = args["address"]
        user.nim = args["nim"]
        db.session.commit()
        return user 
    
    @marshal_with(userFields)
    def delete(self, address):
        user = UserModel.query.filter_by(address=address).first() 
        if not user: 
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users

class nim(Resource):
    @marshal_with(userFields)
    def get(self, nim):
        user = UserModel.query.filter_by(nim=nim).first() 
        if not user: 
            abort(404, message="User not found")
        return user 
    
    @marshal_with(userFields)
    def patch(self, nim):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(nim=nim).first() 
        if not user: 
            abort(404, message="User not found")
        user.name = args["name"]
        user.email = args["email"]
        user.address = args["address"]
        user.nim = args["nim"]
        db.session.commit()
        return user 
    
    @marshal_with(userFields)
    def delete(self, nim):
        user = UserModel.query.filter_by(nim=nim).first() 
        if not user: 
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users


api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')
api.add_resource(nama, '/api/users/name/<string:name>')
api.add_resource(alamat, '/api/users/address/<string:address>')
api.add_resource(email, '/api/users/email/<string:email>')
api.add_resource(nim, '/api/users/nim/<int:nim>')

@app.route('/')
def home():
    return '<h1>Flask REST API</h1>'

if __name__ == '__main__':
    app.run(debug=True)