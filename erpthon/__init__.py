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


VERSION = (1, 0, 0, "alpha", 1)


def get_version(version=None):
    """In acconrding with PEP 386"""
    if version == None:
        version = VERSION
        if VERSION[2] == 0:
            part1 = "%s.%s" % (VERSION[0], VERSION[1])
        else:
            part1 = "%s.%s.%s" % (VERSION[0], VERSION[1], VERSION[2])

    if VERSION[3] in ('alpha', 'beta', 'rc'):
        dict_version = {'alpha': "a", 'beta': "b", 'rc': "c"}
    else:
        raise ValueError

    part2 = dict_version[VERSION[3]] + str(VERSION[4])
    return part1 + part2
