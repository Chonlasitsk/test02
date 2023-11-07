from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/aon', methods=['GET'])
def aon():
    username = request.headers.get('username', None)
    usertoken = request.headers.get('token', None)
    firstname = request.args.get('firstname', default=None)
    lastname = request.args.get('lastname', default=None)
    age = request.args.get('age', default=0)
    if username != "Limpapat" or usertoken != "1234":
        return jsonify({"message" : "Fuck you"}), 401
    info = {
        "name" : f"{firstname} {lastname}",
        "age" : age
    }
    return jsonify(info)

@app.route('/registered', methods=['POST'])
def registered():
    # username = request.headers.get('username', None)
    # usertoken = request.headers.get('token', None)
    input_data = request.get_json()
    # alg....
    return jsonify(input_data)

if __name__ == '__main__':
    app.run(debug=True)
