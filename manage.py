from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Playlist,Favorite
from flask_migrate import Migrate,MigrateCommand

app = create_app('production')

manager = Manager(app)
migrate= Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
  '''
  run unittests
  '''
  import unittest
  tests=unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def shell_context():
  return dict(app=app,db=db, User=User,Playlist=Playlist,Favorite=Favorite)

if __name__=='__main__':
  manager.run()