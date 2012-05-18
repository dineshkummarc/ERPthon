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


import sys


class MetaObject(type):

    """Metaclass for data Objects """

    def __new__(cls, name, bases, dct):
        super_and_new = super(MetaObject, cls).__new__
        parents = [p for p in bases if isinstance(p, MetaObject)]
        if not parents:
            return super_and_new(cls, name, bases, dct)
        module = dct.pop('__module__', None)
        #Get new class to reach the app name and insert it in new "app_name"
        #attribute
        n_cls = super_and_new(cls, name, bases, {'__module__': module})
        if getattr(cls, 'app_name', None) == None:
            models_module = sys.modules[n_cls.__module__]
            dct['app_name'] = models_module.__name__.split('.')[-2]
        else:
            dct = {}
        #Attribute "Relations" contains all relation with other objects or
        # fields
        at_rel = dct.pop("Relations", None)
        if not at_rel:
            rel = getattr(n_cls, "Relations", None)
        else:
            rel = at_rel
        dct['Relations'] = rel
        #Attribure "Views" contains the attribute to display object properly
        # in View
        at_view = dct.pop("View", None)
        if not at_view:
            view = getattr(n_cls, "View", None)
        else:
            view = at_view
        dct['View'] = view
        return super_and_new(cls, name, bases, dct)


class DataObject(object):

    __metaclass__ = MetaObject

    def __init__(self, *args, **kwargs):
        self.id = str(self).split(':')[1]
        #n_args = len(args)

    def __repr__(self):
        return "%s:%s" % (self.__class__.__name__.lower(), id(self))
