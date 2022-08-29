from flask_restful import Resource
from application.database import db
from application.models import User
from flask_restful import fields, marshal_with


output_fields={
    "user_id" : fields.Integer,
    "username" : fields.String,
    "email" : fields.String
}

class UserAPI(Resource):
    def get(self, username):
        #getting the username
        print("GET method in User API: ", username)

        #querying the database
        user = db.session.query(User).filter(User.username==username).first()
        if user:
            #return a valid json
            return user

        else:
            #return 404 error
            return '', 404

    def put(self, username):
        print("PUT username", username)
        return {"username": username}
    def delete(self, username):
        print("DELETE username", username)
        return {"username": username, "action": "DELETE"}
    def post(self):
        print("POST")
        return {"action": "POST"}

