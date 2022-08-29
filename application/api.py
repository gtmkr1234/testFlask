from flask_restful import Resource


class UserAPI(Resource):
    def get(self, username):

        return {"username": username}
    def put(self, username):
        print("PUT username", username)
        return {"username": username}
    def delete(self, username):
        print("DELETE username", username)
        return {"username": username, "action": "DELETE"}
    def post(self):
        print("POST")
        return {"action": "POST"}

