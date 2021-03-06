"""empty message

Revision ID: 75e613e4f1ac
Revises: 599281e22889
Create Date: 2021-09-02 20:21:05.004485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75e613e4f1ac'
down_revision = '599281e22889'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
