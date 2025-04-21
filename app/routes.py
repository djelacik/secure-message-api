from flask import Blueprint, request, jsonify
from .models import Message
from . import db

bp = Blueprint("main", __name__)

@bp.route("/send", methods=["POST"])
def send_message():
    data = request.get_json()
    content = data.get("content", "")
    msg = Message(content=content)
    db.session.add(msg)
    db.session.commit()
    return jsonify({"message": "Message received"}), 201

@bp.route("/messages", methods=["GET"])
def get_messages():
    messages = Message.query.all()
    return jsonify([{"id": m.id, "content": m.content} for m in messages])
