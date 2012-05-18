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


class Field(object):
    """Base class for Fields """
    def _description(self):
        return "This is a %(name)s type" % {'name': self.__class__.__name__}
    description = property(_description)

    def __init__(self, verbose_name=None, have_id=False, widgets=None,
                 default_value=None, validator=None, date_format=None,
                 hidden=False):
        self.name = verbose_name
        self.have_id = have_id
        self.widgets = widgets or []
        self.default_value = default_value
        self.validator = validator
        self.format = date_format
        self.hidden = hidden


class DateField(Field):
    description = "Date Field"
    pass


class BaseField(Field):
    description = "Base field"
    pass


class HashField(Field):
    pass


class GeoPointField(Field):
    pass


class GeoLineField(Field):
    pass


class GeoGeometryField(Field):
    pass
