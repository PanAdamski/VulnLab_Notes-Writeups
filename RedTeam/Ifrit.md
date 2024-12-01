# Ifrit
Mixed, Easy, created by **xct**

Okey. My first redteam lab on vulnlab.

![{A169F024-F3BF-44AD-ACEB-1EEE31E985C0}](https://github.com/user-attachments/assets/69c76728-ec10-462f-9a09-6371c5d2cd8c)

We have intro here https://wiki.vulnlab.com/guidance/ifrit-red-team-lab

add too /etc/hosts
```
172.16.40.225 vdi02.eu-ifrit.vl
```

```
Besides reaching the main objective, your secondary goal is to complete the objective without triggering any detection. If you manage to do so, please write a message to xct.  Please do not RDP to DEV05, a user is working on a critical project there.
```

```
If you haven't regenerated your vpn pack recently, add these routes manually:

sudo ip route add 172.16.40.0/24 via 10.8.0.1 dev tun0 
sudo ip route add 172.16.41.0/24 via 10.8.0.1 dev tun0
```

```
Make sure you have good enumeration methodology that includes at least: AD, ADCS, Shares, Ports, Services, Installed Programs, Users on Machines. Good enumeration is key - both here and in real environments.
The 172.16.41.0/24 Subnet is behind a network firewall - you won't be able to reach your own attacker machine on all ports (but on some).
Not everything you see is exploitable - go for the low hanging fruits as you would on real engagements.
```

lets go!!

I run
```
nmap -Pn -T2 --top-ports 10 -v vdi02.eu-ifrit.vl
```
```
21/tcp   filtered ftp
22/tcp   filtered ssh
23/tcp   filtered telnet
25/tcp   filtered smtp
80/tcp   open     http
110/tcp  filtered pop3
139/tcp  filtered netbios-ssn
443/tcp  open     https
445/tcp  open     microsoft-ds
3389/tcp open     ms-wbt-server
```




