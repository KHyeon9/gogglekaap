"""column change'

Revision ID: 52e0273bf58e
Revises: 21ebeab97f79
Create Date: 2023-08-31 19:33:27.777676

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '52e0273bf58e'
down_revision = '21ebeab97f79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
        batch_op.drop_column('create_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###