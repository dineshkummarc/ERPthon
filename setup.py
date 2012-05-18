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

from distutils.core import setup
from babel.messages import frontend

setup(name='erpthon',
      version='1.0a1',
      description='werp framework tools',
      author='Alessandro Cresto Miseroglio',
      author_email='alex179ohm@gmail.com',
      mantainer='Alessandro Cresto Miseroglio',
      mantainer_email='alex179ohm@gmail.com',
      packages=['erpthon', 'erpthon.app', 'erpthon.bin',
                'erpthon.bin-commands', 'erpthon.data', 'erpthon.db',
                'erpthon.template', 'erpthon.utils'],
      license='AGPL',
      cmdclass={'compile_catalog': frontend.compile_catalog,
                'extract_messages': frontend.extract_messages,
                'init_catalog': frontend.init_catalog,
                'update_catalog': frontend.update_catalog
                })
