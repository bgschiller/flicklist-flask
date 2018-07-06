from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    movies = db.relationship('Movie', backref='owner', lazy=True)
    
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    watched = db.Column(db.Boolean)
    rating = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, owner):
        self.name = name
        self.watched = False
        self.owner = owner
        # line above *also* does "self.owner_id = owner.id"

    def __repr__(self):
        return '<Movie %r>' % self.name
