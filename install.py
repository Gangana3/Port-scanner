"""
This file is used to install the port scanning script as
a commend known by the terminal/cmd.

after installed, can be used in terminal/cmd this way:
portscan <address>

Author: Gangana3
"""
import os
from shutil import copy


SCRIPT_NAME = 'port_scanner.py'
UNIX_DEST = os.path.join(os.sep + 'usr', 'bin')
COMMAND_NAME = 'portscan'


def windows_install():
    """
    Installs the program on windows based systems
    :return: None
    """
    pass


def unix_install():
    """
    installs the program on unix based systems
    :return:
    """
    if os.path.exists(os.path.join(UNIX_DEST, COMMAND_NAME)):
        # remove previous script in case installed before
        os.remove(os.path.join(UNIX_DEST, COMMAND_NAME))
    # move the script to destination
    copy(os.getcwd() + os.sep + SCRIPT_NAME, UNIX_DEST)
    # rename the script to the name of the command
    os.rename(os.path.join(UNIX_DEST, SCRIPT_NAME), os.path.join(UNIX_DEST,
                                                                 COMMAND_NAME))
    # make the script executable
    os.system('cd {}\nchmod +x {}'.format(UNIX_DEST, COMMAND_NAME))


def main():
    try:
        if os.name == 'posix':
            # in case the system is unix based
            unix_install()
        elif os.name == 'nt':
            # in case the system is windows nt based
            windows_install()
    except os.error:
        # in case something went wrong
        if os.name == 'posix':
            print 'The installation must be run with SuperUser rights!\n' \
                  'try \'sudo installation.py\''
        elif os.name == 'nt':
            print 'The installation must be run as Administrator!\n' \
                  'Try running the file as administrator.'


if __name__ == '__main__':
    main()
