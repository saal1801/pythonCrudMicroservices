from flask import Flask, render_template, make_response, jsonify, request

myPython = Flask(__name__)

PORT = 3200

INFO = {
    "courses": {
        "java": "Java",
        "python": "Python",
        "go": "GO",
    },
    "books": {
        "jaba": "Java basics",
        "pyfun": "Python fundamentals",
        "goba": "Go basics",
    },
    "schools": {
        "sch1": "School 1",
        "sch2": "School 2",
        "sch3": "School 3",
    }
}


@myPython.route("/")
def home():
    return "<h1>this is home!</h1>"



@myPython.route("/json")
def get_all_info():
    return make_response(jsonify(INFO), 200)



@myPython.route("/json/<collection>", methods=["POST"])
def add_collection(collection):
    body = request.get_json()

    if collection in INFO:
        return make_response(jsonify({"error": "collection already exist"}), 400)

    INFO.update({collection: body})

    return make_response(jsonify({"success": "collection created"}), 200)



@myPython.route("/json/<collection>/<member>", methods=["POST"])
def add_member(collection, member):
    body = request.get_json()

    if member in INFO[collection]:
        return make_response(jsonify({"error": "member already exist"}), 400)

    INFO[collection].update(body)
    return make_response(jsonify({"success": "collection created"}), 200)



@myPython.route("/json/<collection>/<member>", methods=["PUT"])
def update_info(collection, member):
    body = request.get_json()
    if collection in INFO:
        print(body)
        INFO[collection][member] = body["new"]
        return make_response(jsonify({"res": INFO[collection]}), 200)
    return make_response(jsonify({"error": "not found"}), 404)



@myPython.route("/json/<collection>/<member>", methods=["DELETE"])
def delete_member(collection, member):
    if member in INFO[collection]:
        del INFO[collection][member]
        return make_response(jsonify(INFO[collection]), 200)
    return make_response(jsonify({"error": "not found"}), 404)


if __name__ == "__main__":
    print("Server is running in port %s" % (PORT))
    myPython.run(host='localhost', port=PORT)