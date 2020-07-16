from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Number(db.Model):
    _id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    number_from = db.Column(db.String(200), nullable=False)
    number_to = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Number(_id={self._id}, user_id={self.user_id}"
