# Lustrous
Windows, Medium, created by **xct**

![lustrous_slide](https://github.com/user-attachments/assets/2a572276-9322-44d1-8382-1f8b102c876e)

```
Nmap scan report for 10.10.214.133
Host is up (0.032s latency).
Not shown: 65511 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
21/tcp    open  ftp           Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_12-26-21  11:50AM       <DIR>          transfer
| ftp-syst: 
|_  SYST: Windows_NT
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-12-17 09:23:12Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: lustrous.vl0., Site: Default-First-Site-Name)
443/tcp   open  ssl/http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
| ssl-cert: Subject: commonName=LusDC.lustrous.vl
| Subject Alternative Name: DNS:LusDC.lustrous.vl
| Issuer: commonName=LusDC.lustrous.vl
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-12-26T09:46:02
| Not valid after:  2022-12-26T00:00:00
| MD5:   ab7f:dbe0:a374:2b3b:2329:81ee:fa00:8bb6
|_SHA-1: 6317:3ae3:9a2d:e8a4:fe27:69e0:01b6:1dbc:3868:5a1a
|_http-title: Not Found
| tls-alpn: 
|_  http/1.1
|_http-server-header: Microsoft-HTTPAPI/2.0
|_ssl-date: TLS randomness does not represent time
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: lustrous.vl0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=LusDC.lustrous.vl
| Issuer: commonName=LusDC.lustrous.vl
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-12-16T08:52:52
| Not valid after:  2025-06-17T08:52:52
| MD5:   ba62:6668:7073:374f:1c45:56c0:df2c:079c
|_SHA-1: bbd2:c1c8:26bb:33ea:62d7:bea0:5017:9690:5237:2366
|_ssl-date: 2024-12-17T09:25:02+00:00; +1s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
65083/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
65084/tcp open  msrpc         Microsoft Windows RPC
65123/tcp open  msrpc         Microsoft Windows RPC
65139/tcp open  msrpc         Microsoft Windows RPC

53/udp  open  domain       Simple DNS Plus
|_dns-recursion: Recursion appears to be enabled
88/udp  open  kerberos-sec Microsoft Windows Kerberos (server time: 2024-12-17 08:56:35Z)
123/udp open  ntp          NTP v3
```

```
Nmap scan report for 10.10.214.134
Host is up (0.032s latency).
Not shown: 65529 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=LusMS.lustrous.vl
| Issuer: commonName=LusMS.lustrous.vl
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-12-16T08:52:50
| Not valid after:  2025-06-17T08:52:50
| MD5:   0e56:6477:8d4c:3f27:dbe1:75f9:7f89:bcd8
|_SHA-1: fde8:b37b:68c8:1b96:b183:31bc:b57e:e0f3:b8ae:7800
|_ssl-date: 2024-12-17T09:25:00+00:00; -1s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49669/tcp open  msrpc         Microsoft Windows RPC
```

to po kolei portami. 

### FTP

![{4CC75F64-AD6F-4F74-B68C-ED91ACD88568}](https://github.com/user-attachments/assets/c45e8609-d156-4b18-b8ba-31bc9c8e8fd2)

dało nam trzech userów
```
ben.cox
rachel.parker
tony.ward
wayne.taylor
```

![{87FD9CAC-4B98-405F-AE24-76CEE5A7DF07}](https://github.com/user-attachments/assets/1be07cb8-998f-480c-b0d6-db72e1874bc9)

Ben ma pliczek z `users.csv`, ale wygląda on bardziej na grupy.

![{37D51DFB-3F93-49F1-926B-3329DA71616D}](https://github.com/user-attachments/assets/8bdeffeb-1fd1-4f55-bd5b-3dc6886e3712)

pozostali nie mają nic.

### LDAP

![{AF486A5E-A795-4627-B2B3-C5812CF27C27}](https://github.com/user-attachments/assets/8259d0d1-6710-47b2-93a1-c6dc6383abfb)

### SMB

![{A0309FF9-3052-440A-A1DE-C1B1F14350B1}](https://github.com/user-attachments/assets/16499e34-d16c-4ada-a36b-a532e0dbe988)

ciekawe jest to, że jeden ma smb signing na False.

HMMM
To może asproasting

![{C8A61CEE-0A6D-4C1E-BD8F-6D3895A87482}](https://github.com/user-attachments/assets/ead77d13-9085-41cf-acec-16ca8dec6bec)

bingo. Niby to było oczywiste, ale nie pomyślałem od razu.

![hash](https://github.com/user-attachments/assets/1b5ece3c-1089-44d8-8fbb-183b333485e8)

![{B0CF3875-5F6F-4EDF-A25A-A6746CD52EF5}](https://github.com/user-attachments/assets/74661ada-4816-4d04-810e-376501fd62b5)

trochę enumeracji po shareach, ale nic ciekawego.


