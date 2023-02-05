
from datetime import datetime
from flaskblog import db,login_manager 
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True ,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True,cascade="all, delete-orphan")
    likes = db.relationship('Like', backref='user', lazy=True,cascade="all, delete-orphan")


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"



class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(20))
    FollowedBy=db.Column(db.String(20))
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    meme_file = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # author = db.Column(db.String(20), db.ForeignKey('username',ondelete="CASCADE"), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True,cascade="all, delete-orphan")
    likes = db.relationship('Like', backref='post', lazy=True,cascade="all, delete-orphan")

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}','{self.meme_file}','{self.comments}')"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id',ondelete="CASCADE"), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id',ondelete="CASCADE"), nullable=False)
    


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id',ondelete="CASCADE"), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id',ondelete="CASCADE"), nullable=False)
    