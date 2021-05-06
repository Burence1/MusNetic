import os

class Config:
  '''
  parent class configurations
  '''

  SECRET_KEY = os.environ.get('SECRET_KEY')
  GENRE_API_BASE_URL = 'https://api.deezer.com/genre'
  PLAYLIST_API_BASE_URL = 'https://api.deezer.com/radio'
  TRACK_API_BASE_URL = 'https://api.deezer.com/radio/{}/tracks'
  MUSIC_CHART_URL = 'https://api.deezer.com/chart/0/tracks'
  SEARCH_URL = 'https://api.deezer.com/search?q={}'
  UPLOADED_PHOTOS_DEST ='app/static/photos'
  
  # email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  CLOUD_NAME = os.getenv('CLOUD_NAME')
  API_KEY = os.getenv('API_KEY')
  API_SECRET = api_secret = os.getenv('API_SECRET')


  @staticmethod
  def init_app(app):
    pass

class ProdConfig(Config):
  '''
  Config child class for production configurations
  '''
  pass

class DevConfig(Config):
  '''
  Config child class for development configurations
  '''

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://burens:Hawaii@localhost/music'

  DEBUG=True

config_options={
  'production':ProdConfig,
  'development':DevConfig
}
