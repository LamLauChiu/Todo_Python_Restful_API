from flask import Flask ,jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# @app.route('/', methods=['GET','POST'])
# def index():
#     if(request.method == 'POST'):
#         some_json = request.get_json()
#         return jsonify({ "you sent": some_json }), 201
#     else:
#         return jsonify({ "about": "Hello" })
#
# @app.route('/multi/<int:num>', methods=['GET'])
# def get_multiple10(num):
#     return jsonify({'result':num*10})
class HelloWorld(Resource):
    def get(self):
        return{ "about": "Hi" }
    def post(self):
        some_json = request.get_json()
        return {"you sent": some_json}, 201


class Multi(Resource):
    def get(self, num):
        return { 'resukt': num*10}

api.add_resource(HelloWorld,'/')
api.add_resource(Multi, '/multi/<int:num>')


if __name__ == '__main__':
    app.run(debug=True)
