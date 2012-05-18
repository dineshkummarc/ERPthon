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
from erpthon.utils.translation import get_erpthon_path, get_locale_path
import os
import unittest


class testErpthonUtils(unittest.TestCase):

    def setUp(self):
        self.erpthon_path = get_erpthon_path()

    def test_erpthon_path(self):
        path = "/home/alex/Devel/erpthon"
        self.assertEqual(self.erpthon_path, path)

    def test_locale_path(self):
        locale_path = os.path.join(self.erpthon_path, 'locale')
        self.assertEqual(get_locale_path(), locale_path)

if __name__ == "__main__":
    unittest.main()
