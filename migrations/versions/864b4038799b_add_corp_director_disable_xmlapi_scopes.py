"""add_corp_director_disable_xmlapi_scopes

Revision ID: 864b4038799b
Revises: 2c467ca0efe2
Create Date: 2018-05-03 11:12:45.381657

"""

# revision identifiers, used by Alembic.
revision = '864b4038799b'
down_revision = '2c467ca0efe2'

import sqlalchemy as sa

from alembic import op
from lazyblacksmith.models import TokenScope
from lazyblacksmith.models import User
from lazyblacksmith.models import db


def upgrade():
    op.add_column('user', sa.Column('is_corp_director', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('corporation_id', sa.BigInteger(), nullable=True))
    User.query.update({'is_corp_director': False})
    TokenScope.query.filter_by(scope='characterAssetsRead').update({'valid': False})
    TokenScope.query.filter_by(scope='corporationAssetsRead').update({'valid': False})
    db.session.commit()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_corp_director')
    TokenScope.query.filter_by(scope='characterAssetsRead').update({'valid': True})
    TokenScope.query.filter_by(scope='corporationAssetsRead').update({'valid': True})
    db.session.commit()
    # ### end Alembic commands ###
