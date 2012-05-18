"""    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2012  Cresto Miseroglio Alessandro <alex179ohm@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>."""
from erpthon import settings
import redis


class ModRedis(object):
    """general class for store and manipulating data in Redis db"""
    def __init__(self, relations=None):
        self.relations = relations or None
        self.password = settings.DATA_STORE['password']
        self.db = settings.DATA_STORE['db']
        self.host = settings.DATA_STORE['host']
        self.port = settings.DATA_STORE['port']
        redis.StrictRedis(self.host, self.port, self.db, self.password)

    def test_redis(self):
        pass

    def attach(self):
        pass
