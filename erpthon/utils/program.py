""" ERPthon. The werp framework written in python.
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

import os
from erpthon.utils.functional import get_commands_list


def validate_command(command):
    """
    """
    comm_list = get_commands_list()
    if command in comm_list:
        return True
    else:
        return False


def parse_param(param):
    """
    """
    _list = get_commands_list()
    if param in _list:
        return param
