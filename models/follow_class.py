# coding: utf-8

import time
from pony.orm import *
from ._base import db, SessionMixin, ModelMixin
import models as m
import config

config = config.rec()

class FollowClass(db.Entity, SessionMixin, ModelMixin):
    user_id = Required(int)
    name = Required(unicode)

    follow_count = Required(int, default=0)

    created_at = Required(int, default=int(time.time()))
    active = Required(int, default=int(time.time()))

    description = Optional(unicode)

    def __str__(self):
        return self.id

    def __repr__(self):
        return '<FollowClass>: %s>' % self.id
