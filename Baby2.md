# Baby2
Windows, Medium, created by **xct**

```
# Nmap 7.94SVN scan initiated Sun Dec  1 05:41:39 2024 as: /usr/lib/nmap/nmap --privileged -Pn -A -v --version-all -oA nmap -T4 --max-rate 1000 10.10.75.154
Nmap scan report for 10.10.75.154
Host is up (0.032s latency).
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-12-01 07:41:53Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: baby2.vl0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc.baby2.vl

445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: baby2.vl0., Site: Default-First-Site-Name)
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: baby2.vl0., Site: Default-First-Site-Name)
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: baby2.vl0., Site: Default-First-Site-Name)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
```

```
enum4linux -a 10.10.75.154
enum4linux -u gest -a 10.10.75.154
enum4linux -u anon -a 10.10.75.154


```

![{ACD26DCF-B17A-4D8D-9B45-5CFC17C94773}](https://github.com/user-attachments/assets/e8529218-57ab-44e6-a356-9d156109781d)

![{1DDA640F-4485-481D-BF11-1C4356607DC9}](https://github.com/user-attachments/assets/99056a91-a46e-478f-a90e-52997ec0761b)

![{FD57D9DB-5A9F-4827-AC01-DBBD3EBC842D}](https://github.com/user-attachments/assets/7492c638-c8af-49e7-92f4-0d4f01733379)

![{20D6FA63-130C-4FF7-A43E-9253465DD939}](https://github.com/user-attachments/assets/b36f7edf-09d3-46ae-b012-17e420c35825)

![{D7496CF1-F8C0-47DD-9D3D-C768BD51A6F0}](https://github.com/user-attachments/assets/a6df0381-ed8b-4382-9256-07338cf88f60)

![{B4A24654-5D54-4D7B-BEF6-122BB2F1B45D}](https://github.com/user-attachments/assets/14243871-689e-4ce9-a625-eb495533b965)

ogólnie to sporo `write` już mam

![{33BD1422-606C-4C71-A4BB-8DF3AEBEF4FF}](https://github.com/user-attachments/assets/d07649d7-e610-49f2-af5c-4753fa3e7ea8)

![{4294BC58-E631-477E-BA50-EB56831D3C9B}](https://github.com/user-attachments/assets/c77eca7d-e905-4de2-a77d-be52ebbd14e1)

![{F3A3EB27-C4B7-4626-81E4-32F2012F8D2F}](https://github.com/user-attachments/assets/fe44bea1-4705-4677-9be5-0e2a30933e8b)

![{C26B3AA0-1E6B-40BB-99A6-ED966A2E7DDC}](https://github.com/user-attachments/assets/c2c51ff9-3f51-4eeb-b143-1556e00cda03)

```
> mask ""
> recurse
> prompt
> mget *
```
- o wszystko puste

![{0113EC74-0364-4CB7-8D16-019461CDEE37}](https://github.com/user-attachments/assets/92e7a05a-256a-4c12-839d-3185a35d7825)

![{69F3A6E7-5F99-4599-8123-9699D8B2ED04}](https://github.com/user-attachments/assets/bf465f6f-c4e7-4f43-b2ea-890c2f4b9df4)

tak w solidnym skrócie to to po prostu mapuje share apps na dysk V oraz docs na L.





