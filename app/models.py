from . import db
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
  __tablename__='users'

  id=db.Column(db.Integer,primary_key=True)
  username=db.Column(db.String(255),index=True)
  email=db.Column(db.String(255),unique=True)
  password_hash=db.Column(db.String(255))
  bio=db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  reviews = db.relationship("Review", backref='user', lazy='dynamic')

  @property
  def password(self):
    raise AttributeError("cannot read password")

  @password.setter
  def password(self, password):
    self.password_hash = generate_password_hash(password)

  def password_verification(self, password):
    return check_password_hash(self.password_hash, password)

  def save_user(self):
    db.session.add(self)
    db.session.commit()

  def delete_user(self):
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return f"User {self.username}"

class Review(db.Model):
  __tablename__='reviews'

  id=db.Column(db.Integer,primary_key=True)
  track_id=db.Column(db.Integer)
  track_title=db.Column(db.String(255))
  review_content=db.Column(db.String(255))
  user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

  def save_review(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_reviews(cls, id):
    reviews = Review.query.filter_by(track_id=id).all()

  def __repr__(self):
    return f"Review {self.track_title}"