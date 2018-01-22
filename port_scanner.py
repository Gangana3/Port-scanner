#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------

                    PORT SCANNER

        This code provides a convinient CLI
        based port-scanner. The user gives the IP
        which he wants to scan and this script scans
        all the ports in the ip given.

        The computer MUST be connected
        to the internet in order to use this
        script.


        ===============ALERT================
        This script should NOT be use
        for inapropiate purposes, The script
            writer does not take any
        responsebility for unethical actions.
        =====================================


        © All rights reserved
-------------------------------------------------------

Version: 1.0.0
Author: Gangana3
"""
import re
import socket
import thread
import argparse
from scapy.all import *

DESCRIPTION = """
######################## PORT SCANNER #############################
            
          Welcome to the port scanner. Using this script
          enables you to scan a specific ip address' open
          ports. 
            
                            HAVE FUN
                            
###################################################################
"""
timeout = 0.5  # time to wait to syn+ack response
address = '127.0.0.1'  # address to scan the ports on


def is_connected():
    """
    returns whether the computer is connected to the internet
    :return:
    """
    con_socket = socket.socket()
    try:
        con_socket.connect(('www.google.com', 443))
        return True  # in case managed to create connection
    except socket.error:
        # in case connection failed
        return False


def is_ip(host_address):
    """
    returns whether the given address is an ip or not (maybe a domain)
    :param host_address: address
    :return: whether the given address is ip or not
    """
    # IPv4 Address regex
    ip_regex = re.compile(r'\d{0,3}\.\d{0,3}\.\d{0,3}.\d{0,3}')

    if ip_regex.match(host_address):
        # in case the address matches the regex
        return True
    else:
        # in case the address does not match the regex
        return False


def is_port_open(port):
    """
    returns whether the port is free or not
    :param port: port number
    :return: whether the port is free or not
    """
    syn_packet = IP(dst=address) / TCP(sport=RandShort(), dport=port, flags='S')
    response_packet = sr1(syn_packet, timeout=timeout, verbose=False)
    if response_packet:
        # in case response packet is not None
        if response_packet.getlayer(TCP).flags & 0b100 != 0:
            # in case Reset flag is set
            return False
        else:
            # in case Reset flags is not set
            return True
    else:
        # in case response packet is None
        return False


def main():
    # make sure that user is connected to the internet
    if not is_connected():
        # in case user is not connected to the internet
        print 'In order to use this script you MUST be connected to the ' \
              'internet!'
        exit(1)

    num_of_ports = 2 ** 16

    # initialize the argument parser
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('address', help='The address to scan ports in.',
                        action='store')
    parser.add_argument('-l', '--limit', help='Maximum port to check',
                        action='store', default=num_of_ports, type=int)
    parser.add_argument('-s', '--start', help='Port to start scanning from',
                        action='store', default=0, type=int)
    parser.add_argument('-t', '--timeout',
                        help='Timeout between each port scan', action='store',
                        default=1, type=float)
    args = parser.parse_args()

    # assign global variables
    global address
    global timeout
    address = args.address
    timeout = args.timeout

    print """
---------------------------->
      SCANNING STARTED!
---------------------------->
    """

    ports_scanned = 0  # counter
    try:
        # start scanning
        for i in xrange(args.start, args.limit):
            if is_port_open(i):
                # in case current port is open
                print '=> port {} is open!'.format(i)
            ports_scanned += 1
    except KeyboardInterrupt:
        pass
    finally:
        print """
--------------------------------------------------------------
    => Process Finished! {} ports were scanned!
--------------------------------------------------------------
        """.format(ports_scanned)


if __name__ == '__main__':
    main()
