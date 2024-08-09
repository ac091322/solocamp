from flask.cli import AppGroup
from app.models.db import db, environment, SCHEMA
from .users import seed_users, undo_users
from .genres import seed_genres, undo_genres
from .albums import seed_albums, undo_albums
from .albumarts import seed_albumarts, undo_albumarts
from .songs import seed_songs, undo_songs
from .shoppingcarts import seed_shoppingcarts, undo_shoppingcarts
from .wishlist import seed_wishlists, undo_wishlists
from .supportedbys import seed_supportedbys, undo_supportedbys

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup("seed")


# Creates the `flask seed all` command
@seed_commands.command("all")
def seed():
    if environment == "production":
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_shoppingcarts()
        undo_wishlists()
        undo_supportedbys()
        undo_songs()
        undo_genres()
        undo_albumarts()
        undo_albums()
        undo_users()
    seed_users()
    seed_genres()
    seed_albums()
    seed_albumarts()
    seed_songs()
    seed_supportedbys()
    seed_wishlists()
    seed_shoppingcarts()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command("undo")
def undo():
    undo_shoppingcarts()
    undo_wishlists()
    undo_supportedbys()
    undo_songs()
    undo_genres()
    undo_albums()
    undo_albumarts()
    undo_users()
    # Add other undo functions here
