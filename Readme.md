# Port-Scanner

This is a **CLI** based port scanner for both windows and linux. After installing the port scanner 
you can scan the ports of any Device that's connected to the internet such as routers, servers, etc. 
This script uses scapy so in order to run this script, **scapy** package should be installed. 
If not installed, the installer.py will install it automatically. In addition, Python2.7 MUST be
installed on your device otherwise none of the scripts will work.



## Installation Guide

### Unix Installation

Here are the steps for installing the port scanner on Unix:

 - **step 1:** open up the terminal.
 - **step 2:** navigate to the script's directory using **cd** command.
 - **step 3:** type `sudo python2.7 install.py`.
 
### Windows Installation

Here are the steps for installing the port scanner on Windows:

 - **step1:** run the cmd as administrator
 - **step2:** navigate to the script's directory using **cd** command.
 - **step3:** type `python install.py`


## How To Use?

Well, after you installed the port scanner, you can scan the ports of every device you would like.
The whole scanning process happens in you system's **command line** (teminal/cmd). 

To run this script just type:
 - for **Unix**: `sudo portscan [ip-address/domain] [parameters]`
 - for **windows**: `portscan.py [ip-address/domain] [parameters]`
 
### Optional Parameters

The portscan script takes parameters. Here is the list of all the parameters and it's Purpose:
 - **[-s, --start]**: The port to start checking from. The script scans the ports in raising order, by default the first
port to scan is 0, if **100** is given here, so all the ports under **100** will **not** be scanned.
 - **[-l, --limit]**: The limit of the port scanning. The port specified in here will be the last port to be scanned.
By default, the limit is 65635 (the last port). let's say that the value 1024 is given here, in this case all the ports
untill the port 1024 will be scanned.
 - **[-t, --timeout]**: The timeout to mark the packet as unanswered. After the time (in seconds) that's
specified here, if the SYN packet we sent did not get a response, it will be marked as un answered and the port
we sent the packet to will be considered **closed**.

#### Examples
The following code will scan the ports from 10 to 1024 with timeout of 1 second:

User:~$ sudo portscan 192.168.13.250 --start 10--limit 1024 --timeout 1 
---------------------------->
      SCANNING STARTED!
      scanning 192.168.13.250
---------------------------->
    
=> port 22 is open!
=> port 23 is open!
=> port 53 is open!
=> port 80 is open!
=> port 155 is open!
=> port 443 is open!
            

--------------------------------------------------------------
    => Process Finished! 1024 ports were scanned!
--------------------------------------------------------------

```

To do the same thing on windows just type: `portscan.py 192.168.13.250 --start 10--limit 1024 --timeout 1`



