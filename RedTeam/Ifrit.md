![{6A2301C7-1593-4ACE-BA6F-16F942CBD6E1}](https://github.com/user-attachments/assets/8d243ec9-a526-4471-8d77-a7238581df00)# Ifrit
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

![{A7B582AD-195C-442C-837F-5F44A970685B}](https://github.com/user-attachments/assets/eb199779-1e11-46f0-b360-353e5ffd00d9)

![{16C098F8-8659-4A66-B27B-5810AA5AFC8D}](https://github.com/user-attachments/assets/2b974673-3884-46dc-9798-9e04c2dd2f08)

I press firefox and get .rdp file

![{37D03FBD-BFA8-4926-80CA-FF1E44CCF842}](https://github.com/user-attachments/assets/00d03eec-5eb0-436f-bf6f-0b572e340643)

![{29BFE250-619C-4C54-96E2-2B01F79797FD}](https://github.com/user-attachments/assets/2e601f42-aa64-46e8-9773-e1de9cef84a3)

```
sudo apt install remmina
```

and after instalaion press .rdp file again 

![{6A2301C7-1593-4ACE-BA6F-16F942CBD6E1}](https://github.com/user-attachments/assets/a73a3f73-dc07-4ed8-8b3b-6694abac852a)

![{966758EC-3028-471A-BCD2-F0DD8094ED47}](https://github.com/user-attachments/assets/66390bb4-46e9-40ac-9ced-ab41376e6a93)

![{5A056418-E4F9-4820-9607-65C58B91C2A0}](https://github.com/user-attachments/assets/cd225e67-43ab-4b4a-94d4-b68b200acfad)

After wasting 30 minutes trying, I decided to change my strategy and... it worked

![{A0D49D73-999F-4CF2-9D79-9A0DC31E7254}](https://github.com/user-attachments/assets/0eaf6f7c-20f8-4c79-873f-0a02a6a7ad5c)

`whoami` trigger SIEM so don't use it.

teraz taka mała sztuczka, która może się przydać w penteście, ale w redteamie nie, bo triggerujemy w ten sposób SIEMa. Szukamy sobie DCka będąc na przejętym komputerze
```
nslookup _ldap._tcp.dc._msdcs.<domain>
nslookup _ldap._tcp.dc._msdcs.eu-ifrit.vl
```

![{01260CE1-8716-4201-8DA9-AF20309A68E2}](https://github.com/user-attachments/assets/88c55092-4171-4451-a8c8-8316e0c80478)

kali does not have access to the domain controller. You would need pivoting here

z takiego ogólnego rekonesansu widzimy, że administrator domenowy tutaj wpadał

![{CB8B4391-58F7-4E33-8C3B-8D498B4C0196}](https://github.com/user-attachments/assets/cbdd6fa7-f4d4-4183-bdcc-18374a970ef6)


