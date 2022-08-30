from flask_restful import Resource, reqparse
from application.database import db
from application.models import User
from flask_restful import fields, marshal_with
from application.validation import NotFoundError, BuisnessValidationError


output_fields = {
    "user_id": fields.Integer,
    "username": fields.String,
    "email": fields.String
}

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('username')
create_user_parser.add_argument('email')




class UserAPI(Resource):
    @marshal_with(output_fields)
    def get(self, username):
        # getting the username
        print("GET method in User API: ", username)

        # querying the database
        user = db.session.query(User).filter(User.username == username).first()
        if user:
            # return a valid json
            return user

        else:
            # return 404 error
            raise NotFoundError(status_code=404)

    def put(self, username):
        print("PUT username", username)
        return {"username": username}

    def delete(self, username):
        print("DELETE username", username)
        return {"username": username, "action": "DELETE"}

    def post(self):
        args = create_user_parser.parse_args()
        username = args.get('username', None)
        email = args.get('email', None)

        if username is None:
            raise BuisnessValidationError(status_code=404, error_code='BE1001', error_message="username is required")

        if email is None:
            raise BuisnessValidationError(status_code=404, error_code='BE1002', error_message="email is required")

        if not "@" in email:
            raise BuisnessValidationError(status_code=404, error_code='BE1003', error_message="invalid email")