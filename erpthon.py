#!/home/alex/.virtualenvs/openteam/bin/python
# -*- coding: utf-8 -*-
from erpthon.utils.functional import get_commands_list
from erpthon.exceptions import CommandError
import sys


class Main(object):

    def validate_command(self, command):
        comm_list = get_commands_list()
        if command in comm_list:
            return True
        else:
            return False

    def execute(self, command, param=None):

        if self.validate_command(command):
            module_command = 'erpthon.bin.commands.%s' % command
            __import__(module_command)
            module = sys.modules[module_command]
            c = module.Command()
            if param is not None:
                c.run(param)
            else:
                c.run()
        else:
            raise CommandError(_("somewhere are not worked..Report this bug "
                               "at http://launchpad/erpthon/bugs"))


if __name__ == '__main__':
    m = Main()
    if len(sys.argv) > 2:
        m.execute(sys.argv[1], sys.argv[2])
    else:
        m.execute(sys.argv[1])
