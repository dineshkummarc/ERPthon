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

import os
import sys
from erpthon.bin.commands import get_commands_path


def get_addons_list(curr_dir):
    if 'addons' in os.listdir(curr_dir):
        return os.path.join(os.path.abspath(curr_dir), "addons")
    else:
        return curr_dir


def get_commands_list():
    _list = os.listdir(get_commands_path())
    return [i.split('.')[0] for i in _list if not i.startswith('_') and
            i.endswith('.pyc')]


def import_setting():
    pass
