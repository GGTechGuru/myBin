#! /usr/bin/python3
# TBC

from datetime import datetime
import psutil
import socket
import time


while True:

	msg_off=str(datetime.now() +  ": Turning off wifi (insecure). CONNECT USB/ethernet"

        # lsof -a -i4 -i6 -itcp | egrep -i 'ameritrade|fidelity|schwab|turbotax|intuit' >> /tmp/netMonDebug

        nc = psutil.net_connections()
        for conn in nc:
            raddr_ip = conn.raddr.ip
            try:
                host_str = socket.gethostbyaddr(str(raddr_ip)

                for tether_host in TETHER_HOSTS:
                    if tether_host in host_str:
                        found_hosts.append(host_str)
            except:
                pass


        if len(found_hosts) > 0:
            # echo "FOUND_SITE==${FOUND_SITE}" >> /tmp/netMonDebug
            # ... etc.

	# if [ $? == 0 ]
	if [ "$FOUND_SITE" == "0" ]
	then
		# xmessage -nearmouse -timeout 4 ${msg_off}
		echo ${msg_off} >> /tmp/netMonDebug

		date >> /tmp/netMonDebug
		echo >> /tmp/netMonDebug

		nmcli radio wifi off

        else
		echo "Did not enter first IF block" >> /tmp/netMonDebug

	fi

	nmcli con show --active | grep -i ethernet  >> /tmp/netMonDebug
	if [ $? == 0 ]
	then
		# xmessage -nearmouse -timeout 4 ${msg_off}
		echo ${msg_off} >> /tmp/netMonDebug

		date >> /tmp/netMonDebug
		echo >> /tmp/netMonDebug

		nmcli radio wifi off

	fi

	time.sleep(10)

