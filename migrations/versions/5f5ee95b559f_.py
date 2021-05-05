"""empty message

Revision ID: 5f5ee95b559f
Revises: 6426207425a6
Create Date: 2021-05-05 20:09:43.907336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f5ee95b559f'
down_revision = '6426207425a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.add_column('playlists', sa.Column('preview', sa.String(length=255), nullable=True))
    op.add_column('playlists', sa.Column('title', sa.String(length=255), nullable=True))
    op.add_column('playlists', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'playlists', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'playlists', type_='foreignkey')
    op.drop_column('playlists', 'user_id')
    op.drop_column('playlists', 'title')
    op.drop_column('playlists', 'preview')
    op.create_table('reviews',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('track_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('review_content', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='reviews_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='reviews_pkey')
    )
    # ### end Alembic commands ###