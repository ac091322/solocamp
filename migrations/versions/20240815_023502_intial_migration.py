"""intial migration

<<<<<<<< HEAD:migrations/versions/20240815_023502_intial_migration.py
Revision ID: bc1011e460b5
Revises: 
Create Date: 2024-08-15 02:35:02.968941
========
Revision ID: b9b87ec80891
Revises: 
Create Date: 2024-08-14 21:39:41.583359
>>>>>>>> wishlist-2:migrations/versions/20240814_213941_initial_migration.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:migrations/versions/20240815_023502_intial_migration.py
revision = 'bc1011e460b5'
========
revision = 'b9b87ec80891'
>>>>>>>> wishlist-2:migrations/versions/20240814_213941_initial_migration.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('profile_image', sa.String(length=255), nullable=True),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('genre', sa.String(length=20), nullable=False),
    sa.Column('price', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('description', sa.String(length=2555), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('album_arts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('album_art', sa.String(length=255), nullable=False),
    sa.Column('album_banner', sa.String(length=255), nullable=False),
    sa.Column('background_color', sa.String(length=20), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('collections',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'album_id')
    )
    op.create_table('shopping_carts',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'album_id')
    )
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('track_number', sa.Integer(), nullable=False),
    sa.Column('song_url', sa.String(length=255), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wishlists',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'album_id')
    )
    op.create_table('supported_bys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('supported_bys')
    op.drop_table('wishlists')
    op.drop_table('songs')
    op.drop_table('shopping_carts')
    op.drop_table('collections')
    op.drop_table('album_arts')
    op.drop_table('albums')
    op.drop_table('users')
    # ### end Alembic commands ###
