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

