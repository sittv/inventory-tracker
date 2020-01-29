from flask import Flask, request, jsonify

from flask_restful import abort
import db

app = Flask(__name__)

try:
    db.add_user("jesse", "fooey")
except:
    pass

@app.route("/api/add_user", methods=["POST"])
def add_user():
    content = request.json
    current_login = content.get("current_login")
    name = content.get("name")
    password = content.get("password")
    assert len(password) > 4

    user_id = db.check_login(current_login)
    db.log_event(user_id, current_login, f"create user with name {name} and password {password}",
                 user_id is not None)
    if user_id is None:
        abort(403, messsage="Not authenticated")
        return

    db.add_user(name, password)
    return jsonify({"status": "good"})


@app.route("/api/get_items", methods=["GET"])
def get_items():
    return jsonify(db.get_all_items())


@app.route("/api/add_item", methods=["POST"])
def add_item():
    content: dict = request.json
    current_login = content.get("current_login")
    name = content.get("name")
    location = content.get("location")
    barcode = content.get("barcode")
    user_id = db.check_login(current_login)
    db.log_event(user_id, current_login, f"Add Item {name} @ {location} with barcode {barcode}")

    if user_id is None:
        abort(403, messsage="Not authenticated")
        return

    db.add_item(name, location, barcode)
    return jsonify({"status": "good"})

@app.route("/api/set_barcode", methods=["POST"])
def set_barcode():
    content: dict = request.json
    current_login = content.get("current_login")
    barcode = content.get("barcode")
    item_id = content.get("item_id")
    user_id = db.check_login(current_login)
    db.log_event(user_id, current_login, f"Update barcode for {item_id} with barcode {barcode}")

    if user_id is None:
        abort(403, messsage="Not authenticated")
        return

    db.set_barcode(item_id, barcode)
    return jsonify({"status": "good"})


@app.route("/api/id_checkout", methods=["POST"])
def id_checkout():
    content: dict = request.json
    current_login = content.get("current_login")
    item_id = content.get("item_id")

    user_id = db.check_login(current_login)
    db.log_event(user_id, current_login, f"Checkout item {item_id}")

    if user_id is None:
        abort(403, messsage="Not authenticated")
        return

    db.use_item(item_id, user_id)
    return jsonify({"status": "good"})


@app.route("/api/id_return", methods=["POST"])
def id_return():
    content: dict = request.json
    current_login = content.get("current_login")
    item_id = content.get("item_id")

    user_id = db.check_login(current_login)
    db.log_event(user_id, current_login, f"Return item {item_id}")

    if user_id is None:
        abort(403, messsage="Not authenticated")
        return

    db.return_item(item_id, user_id)
    return jsonify({"status": "good"})




@app.route("/api/barcode_checkout", methods=["POST"])
def barcode_checkout():
    content: dict = request.json
    current_login = content.get("current_login")
    barcode = content.get("barcode")

    user_id = db.check_login(current_login)
    db.log_event(user_id, current_login, f"Checkout item barcode {barcode}")

    if user_id is None:
        abort(403, messsage="Not authenticated")
        return

    db.use_item_barcode(barcode, user_id)
    return jsonify({"status": "good"})


@app.route("/api/barcode_return", methods=["POST"])
def barcode_return():
    content: dict = request.json
    current_login = content.get("current_login")
    barcode = content.get("barcode")

    user_id = db.check_login(current_login)
    db.log_event(user_id, current_login, f"Return item barcode {barcode}")

    if user_id is None:
        abort(403, messsage="Not authenticated")
        return

    db.return_item_barcode(barcode, user_id)
    return jsonify({"status": "good"})


if __name__ == '__main__':
    app.run(debug=True)
