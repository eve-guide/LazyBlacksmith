# -*- encoding: utf-8 -*-
from . import db


class IndustryIndex(db.Model):

    solarsystem_id = db.Column(db.Integer, db.ForeignKey('solar_system.id'), primary_key=True)
    activity = db.Column(db.Integer, primary_key=True, autoincrement=False)
    cost_index = db.Column(db.Numeric(precision=20, scale=19, decimal_return_scale=19, asdecimal=False), nullable=True)