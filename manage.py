import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db

from seed import seed_db


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def seed():
    seed_db()

if __name__ == '__main__':
    manager.run()