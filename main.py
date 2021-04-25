from flask import Flask, request, Response, json


app = Flask(__name__)


@app.route('/', methods=["POST"])
def main():
    print("Hello, World!")


@app.route("/calculate", methods=["POST"])
def calculate():

    request_data = request.get_json()

    a = request_data["a"]
    b = request_data["b"]

    response = {"result": a + b}

    return Response(json.dumps(response), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()