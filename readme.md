# Wake-on-LAN and System Control Scripts for a linux machine.

This repository contains two Python scripts designed to facilitate remote control of a computer via network commands. The scripts allow for waking up a computer from sleep mode, putting it to sleep, shutting it down, and sending magic packets for Wake-on-LAN functionality.

## Prerequisites

- Python 3.x installed on your system.
- A linux server (the one receiving commands) and another to act as the client (the one sending commands).
- Ensure the target computer supports Wake-on-LAN and that this feature is enabled in its BIOS settings.
- Network connectivity between the client and server computers.
- pip install wakeonlan


Clone the reporsitory on both machines.

## Scripts Overview

### listen.py

This script listens for incoming UDP messages on a specified port. Based on the content of the message, it performs actions such as:

- Putting the system to sleep (`sleep`)
- Shutting down the system (`shutdown`)
- Waking up the system (`wake`)

before anything you'll have to enable WOL on the server machine. To do this open terminal on the server machine and run :

`sudo apt install ethtool`

then find your ethernet interface name by running:

`ifconfig`

# FOR debian:

`sudo nano /etc/nnetwork/interfaces`

### add the last two lines:

```
source /etc/network/interfaces.d/*

auto lo
iface lo inet loopback

allow-hotplug enp8s0
iface enp8s0 inet dhcp
    post-up /usr/sbin/ethtool -s enp8s0 wol g
    post-down /usr/sbin/ethtool -s enp8s0 wol g
```

change enp8s0 to your interface name.

# For ubuntu:

by adding a file to /etc/netplan, named /etc/netplan/50-wol.yaml

the contents of the file are: (fill in your own mac-address).

```
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    enp8s0:
      match:
        macaddress: XX:XX:XX:XX:XX:XX
      wakeonlan: true
      dhcp4: yes
```

change enp8s0 to your interface name.

https://askubuntu.com/questions/1405533/how-to-automatically-enable-wake-on-lan-for-a-network-interface-on-ubuntu-20-04

# To run `listen.py`, on boot of the computer create a systemd service file:

```
[unit]
Description=Sleep using packet

[service]
Type=simple
User=root
WorkingDirectory=<YOUR WORKING DIRECTORY>
ExecStart= python listen.py

[install]
WantedBy=network-online.target
```

Change the "WorkingDirectory=/home/ubuntu" to the directory where `listen.py` is located.

https://www.shubhamdipt.com/blog/how-to-create-a-systemd-service-in-linux/

## Usage

run `remote.py` on the client machine:

Enter 1 for WAKE,
2 for SLEEP 
0 for SHUTDOWN
q to Quit
