from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if (request.method == 'POST'):
	    some_json = request.get_json()
	    return jsonify({'you sent': some_json})
    return jsonify({"about": "Hello World!"})

if __name__ == "__main__":
    app.run()