"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)

    name = db.Column(db.String(40), nullable = False)

class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)

    title = db.Column(db.String(80), nullable = False)

    content = db.Column(db.String(5000), nullable = False)

    user_id = db.Column(db.Integer, nullable = False, db.ForeignKey("users"))


class Comment(db.model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)

    reply = db.Column(db.String(1000), nullable = False)

    post_id = db.Column(db.Integer, nullable = False, db.ForeignKey("posts"))

class Game(db.model):

    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)

    user_score1 = db.Column(db.Integer, nullable = False)

    user_score2 = db.Column(db.Integer, nullable = False)

    user_id1 = db.Column(db.Integer, nullable = False, db.ForeignKey("users"))

    user_id2 = db.Column(db.Integer, nullable = False, db.ForeignKey("users"))

