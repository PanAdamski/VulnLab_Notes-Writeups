# Ifrit
Mixed, Easy, created by **xct**

![ifrit_slide](https://github.com/user-attachments/assets/e26e203b-cc12-4d1b-9e36-84a0a07e24bf)

Okey. My first redteam lab on **vulnlab**.

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

wróciłem sobie po prawie miesiącu i kilka obserwacji od zera, na chłodno.
Po pierwsze user `Tina.Dawson` jest trochę inna niż pozostali userzy.

![{2C0CDB79-297E-42F0-BE3B-D022E1B26C4A}](https://github.com/user-attachments/assets/c1cd6ede-a8f4-4934-a203-a4ebd7c0de1d)

dla testu zapuściłem nmap i SIEM milczy hehe.
```
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: IIS Windows Server
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
135/tcp  open  msrpc         Microsoft Windows RPC
443/tcp  open  ssl/http      Microsoft IIS httpd 10.0
| ssl-cert: Subject: commonName=VDI02.eu-ifrit.vl
| Issuer: commonName=VDI02.eu-ifrit.vl
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-08-01T09:17:54
| Not valid after:  2025-01-31T09:17:54
| MD5:   d5b5:7ce7:06e1:78e5:4bc3:1ebd:9c8e:609e
|_SHA-1: 1f48:52e9:c410:f0bb:16e7:e015:341f:6f69:fec2:b0ce
|_http-title: IIS Windows Server
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
| tls-alpn: 
|_  http/1.1
|_http-server-header: Microsoft-IIS/10.0
|_ssl-date: TLS randomness does not represent time
445/tcp  open  microsoft-ds?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=VDI02.eu-ifrit.vl
| Issuer: commonName=VDI02.eu-ifrit.vl
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-12-27T13:56:50
| Not valid after:  2025-06-28T13:56:50
| MD5:   0c5b:6847:9f44:568a:424f:fd20:ab83:430f
|_SHA-1: 232e:bff0:5ef0:9fb4:02a3:e9a3:b765:b526:4e32:acf2
|_ssl-date: 2024-12-28T14:22:19+00:00; +7s from scanner time.
5357/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
```
- szczerze to nic ciekawego nie pokazał.

![{B7399B99-9CA6-4C1E-A185-E03BD606812A}](https://github.com/user-attachments/assets/838559b3-8b04-41d1-ae98-8abca240c1a2)

a ta Tina to serio wyjątkowa.

WTF?! Nie wiem co się stało, ale po miesiącu nagle RDP działa bez problemu... teraz to ja z górki mam.

![{824001E6-703B-4A9C-ACB7-2D6446A7A37E}](https://github.com/user-attachments/assets/98700c6f-b6e6-444f-aa3b-397bb3e26826)

jesteśmy w kiosk'u firefoxa.
Ctrl+O

![{26040EE4-3533-4CCC-8908-0EF0525256B8}](https://github.com/user-attachments/assets/0b0300da-e9af-4a26-bb34-40e368420f8b)

![{B4F3FA81-E55F-4478-9BE4-E5B9D7565A5C}](https://github.com/user-attachments/assets/a2d31840-f9e7-43cc-9f2a-5f5e5b5ec172)

![{2850A516-38C9-4A59-AE77-DB7072C9E6FF}](https://github.com/user-attachments/assets/685042a7-e26d-4566-a256-b064fd272de4)

![{896EC16B-7A35-4C40-B6A7-10A9A1E9229E}](https://github.com/user-attachments/assets/c608ba63-54e1-4d10-a060-bfb5a7d587f9)

![{69FFD1BB-3FBE-440C-A69A-D47E0DFAA8F4}](https://github.com/user-attachments/assets/27a5beba-e997-4c04-805b-edc5123b4945)


iiii w sumie mamy tak jakby "normalnego windowsa" już.

![{1846675F-30C4-48AC-AFBC-9638E134D59C}](https://github.com/user-attachments/assets/5d7e0fd4-9a64-4c71-985a-2efd4669ac8e)

o pierwsze informacje.

![{1B01A55E-54FB-4EF2-95B2-FBBBA697313E}](https://github.com/user-attachments/assets/b6172f3c-12d6-4a7d-beb6-862b311ed726)

w inetpub nie mamy write.

wykorzystując jedną z najprostszych metod do enumeracji userów znajdujemy hasło z opisie.. chyba ldapa.

![{BFCC1FDA-B7C8-47B9-AF63-880218DCF21F}](https://github.com/user-attachments/assets/c791ed37-b57e-4303-a4cb-4edbe5c3d9f8)

- dwóch userów takie ma
- to prawdopodbnie honeypot users :(



