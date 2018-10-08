from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    pos=db.Column(db.Integer)
    def __repr__(self):
        return '<Post {}>'.format(self.body)