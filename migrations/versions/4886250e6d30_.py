"""empty message

Revision ID: 4886250e6d30
Revises: None
Create Date: 2014-09-27 13:34:38.262000

"""

# revision identifiers, used by Alembic.
revision = '4886250e6d30'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('page_domain', sa.String(length=255), nullable=True),
    sa.Column('subscribe', sa.Integer(), nullable=True),
    sa.Column('profile', sa.String(length=1024), nullable=True),
    sa.Column('genre', sa.String(length=255), nullable=True),
    sa.Column('join_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###
