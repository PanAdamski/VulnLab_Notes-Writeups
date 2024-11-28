# Breach
Windows, Medium, created by **xct**

![breach_slide](https://github.com/user-attachments/assets/d3ba0a90-294a-4f8f-985a-fdcb98134eaf)

```
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-11-28 20:32:24Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: breach.vl0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: breach.vl0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=BREACHDC.breach.vl
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49685/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49907/tcp open  msrpc         Microsoft Windows RPC

```
```
dig @10.10.100.171 breach.vl any
dig @10.10.100.171 breach.vl axrf 
```
- nic ciekawego

```
enum4linux -u anonymous -a 10.10.100.171
enum4linux  -a 10.10.100.171
enum4linux -u guest -a 10.10.100.171
```

![{CD6EF018-BA6E-4B86-8DB9-BC259797566A}](https://github.com/user-attachments/assets/74bf33db-8fb4-4e1b-9d7d-9fb747b978ec)

![{942E308C-25DE-45F7-9EBA-007AB1554DF5}](https://github.com/user-attachments/assets/ff6afa0c-ef49-454d-8a04-1cf88e10d8e0)










