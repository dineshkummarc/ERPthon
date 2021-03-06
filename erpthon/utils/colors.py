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


foreground = {'black': '30', 'red': '31', 'green': '32', 'yellow': '33',
              'blue': '34', 'purple': '35', 'cyan': '36', 'white': '37'}
background = {'black': '40', 'red': '41', 'green': '42', 'yellow': '43',
              'blue': '44', 'purple': '45', 'cyan': '46', 'white': '47'}

options = {'none': '0', 'bold': '1', 'underscore': '4', 'blink': '5',
           'reverse': '7'}

TEXT_RESET = '0'


def colorize(text, fg='', bg='', opt='none', reset=True):
    """
    Colorize text in shell.

    reset style and color text if no arguments are given.

    Args:
    -----
    :param string text: the text you want to custom
    :param string fg: foreground color (default is '')
    :param string bg: backgorund color (default is '')
    :param string opt: decorate text options (default is 'none')
    :param bool reset: set to false if you want to set the style permanent,
                   (default is True).

    USAGE:
    ------
    colorize('blue bold text', fg='blue', opt='bold')
    colorize('backgournd green colored text', bg='green')
    colorize() or colorize(opt='reset') #reset style text

    AVAILABLE COLORS:
    -----------------
    black, red, green, yellow, blue, purple, cyan, white

    AVAILABLE OPTIONS:
    ------------------
    reset, none, bold, uderscore, blink, reverse

    :rtype: ASCII string
    :returns: ASCII text with code for customize it in unix shell.
    """
    reset = '\x1b[%sm' % TEXT_RESET
    style_list = []

    if opt == 'reset' or text == "":
        return reset
    if opt:
        for k, v in options.iteritems():
            if k == opt:
                style_list.append(options[v])
    if fg:
        style_list.append(foreground[fg])
    if bg:
        style_list.append(background[bg])
    if reset:
        text = text + reset

    text = ('\x1b[%sm' % ';'.join(style_list)) + text
    return text

_fg = ''
_bg = ''


def make_style(text, fg, bg, opt):
    """
    Make custom style for text.

    USAGE:
    bold_red = make_style(fg='red', opt=bold)
    bold_red("i want bold red text")

    PARAMS:
    :param string fg: foreground color
    :param string bg: backgorund color
    :param string opt: options like 'none', 'bold' ...

    for available colors and options read :py:func: `colorize`
    """
    global _fg
    global _bg
    _fg = fg
    _bg = bg
    return lambda text: colorize(text, fg, bg, opt)
