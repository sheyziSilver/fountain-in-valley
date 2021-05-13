"""empty message

Revision ID: 3a2dafd3cc83
Revises: 
Create Date: 2021-05-12 18:48:15.793098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a2dafd3cc83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('pin', sa.String(length=4), nullable=True))
    op.create_unique_constraint(None, 'user', ['pin'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'pin')
    # ### end Alembic commands ###
