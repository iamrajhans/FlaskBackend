"""empty message

Revision ID: 59b25a9d6e7b
Revises: 0f23ce52e7cd
Create Date: 2017-02-09 23:23:20.802173

"""

# revision identifiers, used by Alembic.
revision = '59b25a9d6e7b'
down_revision = '0f23ce52e7cd'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request_referral',
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.Column('from_user', sa.String(length=255), nullable=False),
    sa.Column('to_user', sa.String(length=255), nullable=False),
    sa.Column('request_type', sa.String(length=255), nullable=False),
    sa.Column('referral_id', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column(u'users', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column(u'users', 'email',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.alter_column(u'users', 'last_name',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.alter_column(u'users', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column(u'users', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column(u'users', 'user_id',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(u'users', 'user_id',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column(u'users', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column(u'users', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column(u'users', 'last_name',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.alter_column(u'users', 'email',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.alter_column(u'users', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_table('request_referral')
    ### end Alembic commands ###
