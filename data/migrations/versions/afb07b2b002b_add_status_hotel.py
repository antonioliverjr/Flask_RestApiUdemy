"""add status hotel

Revision ID: afb07b2b002b
Revises: 5c6453bfaac6
Create Date: 2022-03-07 10:54:47.968775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afb07b2b002b'
down_revision = '5c6453bfaac6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hotels', 'status')
    # ### end Alembic commands ###
