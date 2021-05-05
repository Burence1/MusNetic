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
  playlists = db.relationship("Playlist", backref='user', lazy='dynamic')

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

class Favorite(db.Model):
  __tablename__='favorites'

  id = db.Column(db.Integer,primary_key=True)
  
class History(db.Model):
  __tablename__='histories'

  id= db.Column(db.Integer,primary_key=True)

class Playlist(db.Model):
  __tablename__='playlists'

  id=db.Column(db.Integer,primary_key=True)
  track_id=db.Column(db.Integer)
  title=db.Column(db.String(255))
  preview=db.Column(db.String(255))
  user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

  def save_playlist(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_playlist(cls,id):
    my_playlist=Playlist(user=current_user,track_id=id)
    return my_playlist

  def __repr__(self):
    return f"{self.track_id}"

class Genre:
  '''
  Genre class to define Music Genre objects
  '''
  def __init__(self,id,title,poster):
        self.id=id
        self.title=title
        self.poster=poster

class GenreTrack:
  '''
  Genre Track class to define track Genre objects
  '''
  def __init__(self,id,title,picture,playlist):
        self.id=id
        self.title=title
        self.picture=picture
        self.playlist = playlist

class radioTrack:
  def __init__(self,id, title, artist, album,preview):
      self.id=id
      self.title = title
      self.artist = artist
      self.album = album
      self.preview = preview

class Chart:
  '''
  Chart class that defines class objects
  '''
  def __init__(self, id, title, link, preview, picture, position,name):
    self.id = id
    self.title = title
    self.link = link
    self.preview = preview
    self.picture = picture
    self.position = position
    self.name = name


class Artist:

  def __init__(self, id, title, name, preview,picture):
    self.id = id
    self.title = title
    self.name = name
    self.preview = preview
    self.picture = picture