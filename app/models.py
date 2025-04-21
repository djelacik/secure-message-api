from . import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Message {self.id}: {self.content}>'
