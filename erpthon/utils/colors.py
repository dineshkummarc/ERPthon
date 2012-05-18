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


colors = {'black': '0', 'red': '1', 'green': '3', 'yellow': '4',
              'blue': '5', 'purple': '6', 'cyan': '7', 'white': '8'}
fg = '3'
bg = '4'

options = {'none': '0', 'bold': '1', 'underline': '4'}

text_reset = '0'


def colorize(text, fg='', bg='', opt='none'):

    RESET = '\x1b[%sm' % text_reset
