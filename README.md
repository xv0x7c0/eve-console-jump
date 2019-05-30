# eve-console-jump

EVE-ng VMs console ports are attributed dynamically each time a VM boots. This script connects to EVE-ng server, reads the database where console ports/VMs are stored, connects via SSH to the EVE-ng server and then locally telnet to the VMs console.

This basically avoids using EVE-ng browser based console.

# Prerequisites

## EVE-ng mysqld connection

EVE-ng mysqld accepts only local connections by default. This script MUST be able to connect to mysqld to read the appropriate tables. Since your setup is different than mine, DYODD and setup your stuff accordingly.

## EVE-ng read-only user

A special read-only user MAY be configured on mysqld, just to be able to read the console ports table. As an example :

```
grant select on eve_ng_db.console to 'username'@'network/netmask' identified by 'password';
```

## EVE-ng SSH connection

EVE-ng accepts SSH connections for administrative purpose from the root user. Local account with lesser privileges can be added. Up to you.

# Usage

## List available VMs 

```
$ eve-console-jump -e eve.mydomain -u myuser -p mypasswd
 0| LAB1: XR5
 1| LAB1: XR4
 2| LAB1: XR1
 3| LAB1: XR3
 4| LAB1: R1
 5| LAB1: R5
 6| LAB1: R4
 7| LAB1: R2
 8| LAB2: XR2
 9| LAB2: R6
10| LAB2: XR6
11| LAB2: R3
```

## Connect to a specific VM

```
$ eve-console-jump -e eve.mydomain -u myuser -p mypasswd -i 0
Connecting to XR5...
 - ssh -t myuser@eve.mydomain "telnet localhost 53111"
 Trying 127.0.0.1...
 Connected to localhost.
 Escape character is '^]'.

 IMPORTANT: READ CAREFULLY
 Welcome to the Demo Version of Cisco IOS XRv (the "Software").
 [...]
```

# EVE-ng

Take a look at it here : [EVE-ng](https://www.eve-ng.net).
