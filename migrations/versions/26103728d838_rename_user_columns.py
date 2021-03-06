"""rename user columns

Revision ID: 26103728d838
Revises: 1985707745ef
Create Date: 2017-01-03 21:35:41.138000

"""

# revision identifiers, used by Alembic.
revision = '26103728d838'
down_revision = '1985707745ef'

import sqlalchemy as sa

from alembic import op
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('eve_user', sa.Column('access_token_expires', sa.DateTime(timezone=True), nullable=True))
    op.drop_column('eve_user', 'access_token_expires_in')
    op.drop_column('eve_user', 'access_token_expires_on')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('eve_user', sa.Column('access_token_expires_on', mysql.DATETIME(), nullable=True))
    op.add_column('eve_user', sa.Column('access_token_expires_in', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('eve_user', 'access_token_expires')
    # ### end Alembic commands ###
