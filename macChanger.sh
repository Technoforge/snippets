#!/usr/bin/bash

#A rather normal MAC and hostname changer written for Arch Linux.

#Set up hexadecimal array.
declare -a hx=(0 1 2 3 4 5 6 7 8 9 a b c d e f)

#Set up array of MAC vendor strings. Use only those likely to be legitimate mobile devices in your country. http://standards-oui.ieee.org
declare -a vn=(
	"48:ad:08" "2c:ab:00" "00:e0:fc" "80:38:bc" "64:a6:51" #Huawei
	"00:cd:fe" "18:af:61" "cc:44:63" "6c:72:e7" "08:74:02" #Apple
	"38:f2:3e" "38:25:6b" "30:0d:43" "60:7e:dd" "a4:51:6f" #Microsoft
	"80:7a:bf" "90:e7:c4" "7c:61:93" "2c:8a:72" "98:0d:2e" #HTC
	"4c:7f:62" "40:7a:80" "b0:5c:e5" "48:dc:fb" "6c:9b:02" #Nokia
	"6c:0e:0d" "b4:52:7d" "e0:63:e5" "00:0e:07" "00:1d:28" #Sony
	"30:96:fb" "f0:ee:10" "9c:d3:5b" "10:30:47" "38:d4:0b" #Samsung
)

#Extract wireless interface name from ip link. Or just hard code your interface name.
WIFI=$(ip link | grep -o 'wl[^:]*')

#A couple of new lines for easy reading.
echo -e '\n''\n'

#Show current hostname.
HN=$(hostname)
echo -e Your current hostname is: $HN

#Show wireless interface name.
echo -e Your wireless interface name is: $WIFI

#Get old MAC address.
MAC=$(cat /sys/class/net/$WIFI/address)

#Show old MAC address.
echo -e Your current wifi MAC address is: $MAC

#Assemble new MAC sequence.
MAC=${vn[$(($RANDOM%15))]}:${hx[$(($RANDOM%15))]}${hx[$(($RANDOM%15))]}:${hx[$(($RANDOM%15))]}${hx[$(($RANDOM%15))]}:${hx[$(($RANDOM%15))]}${hx[$(($RANDOM%15))]}

echo -e -n Attempting to disable wireless interface $WIFI...

if ! ip link set dev $WIFI down
       then
              echo -e "\e[91mFAILED.\e[39m"
              exit
       else
              echo -e "\e[32mSUCCEEDED.\e[39m"
fi

echo -e -n Attempting to generate new hostname...

if ! HN=$(shuf -n1 /usr/share/dict/cracklib-small)
       then
              echo -e "\e[91mFAILED.\e[39m"
              exit
       else
              echo -e "\e[32mSUCCEEDED.\e[39m"
fi

echo -e -n Attempting to set new hostname...

if ! hostnamectl set-hostname $HN
       then
              echo -e "\e[91mFAILED.\e[39m"
              exit
       else
              echo -e "\e[32mSUCCEEDED.\e[39m"
fi

echo -e -n Attempting to change wireless interface $WIFI MAC address...

if ! ip link set dev $WIFI address $MAC
       then
              echo -e "\e[91mFAILED.\e[39m"
              exit
       else
              echo -e "\e[32mSUCCEEDED.\e[39m"
fi

echo -e -n Attempting to enable wireless interface $WIFI...

if ! ip link set dev $WIFI up
       then
              echo -e "\e[91mFAILED.\e[39m"
              exit
       else
              echo -e "\e[32mSUCCEEDED.\e[39m"
fi

echo -e Your new hostname is: $(hostname)

echo -e Your new MAC address for wireless interface $WIFI is: $(cat /sys/class/net/$WIFI/address).

#A couple of new lines for easy reading.
echo -e '\n''\n'