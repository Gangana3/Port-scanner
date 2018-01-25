"""
This file is used to install the port scanning script as
a commend known by the terminal/cmd.

after installed, can be used in terminal this way:
portscan <address>

or in the cmd this way:
portscan.py <address>

HAVE FUN! :)

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
    path_var = os.environ['PATH']   # %PATH% environment variable

	if os.getcwd() in path_var:
		# in case the script's directory already in %PATH%
		return 	# quit the function

    if path_var.endswith(';'):
        setx_command = 'setx PATH "{}{};"'
    else:
        setx_command = 'sex PATH "{};{}"'

    # format the setx command
    setx_command = setx_command.format(path_var, os.getcwd())

    # execute setx command and add the script's path to %PATH%
    os.system(setx_command)

    # rename the script
    os.rename(SCRIPT_NAME, COMMAND_NAME + '.py')

    try:
        import scapy
    except ImportError:
        # in case scapy is not installed
        scapy = None
        os.system('python -m pip install scapy')     # install scapy


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

    try:
        import scapy
    except ImportError:
        # in case scapy is not installed
        scapy = None
        os.system('python2.7 -m pip install scapy')     # install scapy


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
        exit(1)

    print 'Installed successfully!'


if __name__ == '__main__':
    main()
