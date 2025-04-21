from flask import Blueprint, request, jsonify
from . import db
from .models import Message

main = Blueprint('main', __name__)

@main.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    message = Message(content=data['content'])
    db.session.add(message)
    db.session.commit()
    return jsonify({'message': 'Message saved'}), 201

@main.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([{'id': m.id, 'content': m.content} for m in messages])
