from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os
from flask_debugtoolbar import DebugToolbarExtension

from app import app, db


##helloas
migrate = Migrate(app, db)
manager = Manager(app)

toolbar = DebugToolbarExtension(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()