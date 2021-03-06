from flask import Flask ,jsonify, request
app = Flask(__name__)

# @app.route("/")
# def index():
#     # return "Hi"
#     return jsonify({ "about":"hi"})
#

@app.route('/', methods=['GET','POST'])
def index():
    if(request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({ "you sent": some_json }), 201
    else:
        return jsonify({ "about": "Hello" })

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiple10(num):
    return jsonify({'result':num*10})


if __name__ == '__main__':
    app.run(debug=True)
