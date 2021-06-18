#!/usr/bin/bash

echo "Hello $(hostname)";
if [ "$UID" -ne 0 ]; then
    echo "Must be root to run this script."
    exit $E_NOTROOT
fi
pwd
rm res*
rm final_*
# rm output
echo "[+] Trying name resolution";
host $1 &> /dev/null
if [ $? -eq 0 ]; then
    echo "got it !!"
else
    echo "[-] name resolution error"
    exit 2
fi
echo "[+] Trying UDP traceroute for: " + $1;
traceroute -U $1 > res.udp
if [ $(fgrep "* * *" res.udp | wc -l) -eq 0 ]; then
    cat res.udp;
    echo "[+] complete";
    exit 1;
else
    echo "[+] Trying ICMP traceroute: " + $1;
    traceroute -I $1 > res.icmp
    if [ $(fgrep "* * *" res.icmp | wc -l) -eq 0 ]; then
        cat res.icmp; 
        echo "[+] complete";
        exit 1;
    else
        echo "[+] Trying TCP traceroute "+ $1;
        traceroute -T $1 > res.tcp
       if [ $(fgrep "* * *" res.tcp | wc -l) -eq 0 ]; then
            cat res.tcp;
            echo "[+]complete"
            exit 1;
        else
           cat res.tcp
	   echo "[+]complete"
	   # echo "[-] some error might trying checking your permission and your network"
            exit 1;
         fi
    fi
fi


