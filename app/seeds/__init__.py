from flask.cli import AppGroup
from .users import seed_users, undo_users
from .sets import seed_sets, undo_sets
from .set_folder import seed_set_folder, undo_set_folder
from .ratings import seed_ratings, undo_ratings
from .folders import seed_folders, undo_folders
from .cards import seed_cards, undo_cards

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_ratings()
        undo_cards()
        undo_set_folder()
        undo_folders()
        undo_sets()
        undo_users()
    seed_users()
    seed_sets()
    seed_folders()
    seed_set_folder()
    seed_cards()
    seed_ratings()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_ratings()
    undo_cards()
    undo_set_folder()
    undo_folders()
    undo_sets()
    undo_users()
    # Add other undo functions here
