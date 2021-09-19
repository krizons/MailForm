"""sender  table

Revision ID: a9d45952d9a7
Revises: 
Create Date: 2021-09-19 16:40:14.494896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9d45952d9a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mail_task',
    sa.Column('heading', sa.String(), nullable=False),
    sa.Column('subtitle', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('path_doc', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mail_task')
    # ### end Alembic commands ###
