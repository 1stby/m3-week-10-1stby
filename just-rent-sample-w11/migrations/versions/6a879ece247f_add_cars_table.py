"""add cars table

Revision ID: 6a879ece247f
Revises: f441d7cf8d3f
Create Date: 2024-04-07 21:12:44.075446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a879ece247f'
down_revision = 'f441d7cf8d3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('seats', sa.Integer(), nullable=False),
    sa.Column('door_count', sa.Integer(), nullable=False),
    sa.Column('fuel_price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars')
    # ### end Alembic commands ###
