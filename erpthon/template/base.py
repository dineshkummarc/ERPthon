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

from jinja2.environment import TemplateStream
from erpthon.exceptions import TemplateError

base_type_views = ('search', 'form', 'map', 'graph')


class BaseView(object):

    def __init__(self, source):
        self.errors = {}
        self.type = base_type_views or None
        if self.type not in base_type_views:
            self.errors['type'] = TemplateError("Type views missing")
            self.type = None
