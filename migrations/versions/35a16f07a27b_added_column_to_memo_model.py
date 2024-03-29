"""Added column to memo model

Revision ID: 35a16f07a27b
Revises: 3aaa7b9f8bdf
Create Date: 2023-09-08 16:50:07.974158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35a16f07a27b'
down_revision = '3aaa7b9f8bdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('memo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_deleted', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('memo', schema=None) as batch_op:
        batch_op.drop_column('is_deleted')

    # ### end Alembic commands ###
