import os

class Config:
  '''
  parent class configurations
  '''

  SECRET_KEY = os.environ.get('SECRET_KEY')
  MUSIC_CHART_URL = 'https://api.deezer.com/chart/0/tracks'
  SEARCH_URL = 'https://api.deezer.com/search?q={}'

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
