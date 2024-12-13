# Cicada
Windows, medium, created by **xct**

```
# Nmap 7.94SVN scan initiated Fri Dec 13 07:28:33 2024 as: /usr/lib/nmap/nmap --privileged -Pn -v -p- --version-all -oA nmapFULL --max-rate 1500 -A 10.10.69.106
Increasing send delay for 10.10.69.106 from 0 to 5 due to 23 out of 76 dropped probes since last increase.
Increasing send delay for 10.10.69.106 from 5 to 10 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 10.10.69.106 from 10 to 20 due to 11 out of 11 dropped probes since last increase.
Nmap scan report for 10.10.69.106
Host is up (0.031s latency).
Not shown: 65509 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
|_http-server-header: Microsoft-IIS/10.0
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-12-13 07:08:06Z)
111/tcp   open  rpcbind       2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: cicada.vl0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC-JPQ225.cicada.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC-JPQ225.cicada.vl
| Issuer: commonName=cicada-DC-JPQ225-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-09-13T10:42:50
| Not valid after:  2025-09-13T10:42:50
| MD5:   2b54:f7f1:53c6:0241:c432:c868:1d86:5ec7
|_SHA-1: eef8:12f9:0a11:c0d5:16c1:c499:9abf:3341:4419:6a2b
|_ssl-date: TLS randomness does not represent time
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: cicada.vl0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=DC-JPQ225.cicada.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC-JPQ225.cicada.vl
| Issuer: commonName=cicada-DC-JPQ225-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-09-13T10:42:50
| Not valid after:  2025-09-13T10:42:50
| MD5:   2b54:f7f1:53c6:0241:c432:c868:1d86:5ec7
|_SHA-1: eef8:12f9:0a11:c0d5:16c1:c499:9abf:3341:4419:6a2b
2049/tcp  open  nlockmgr      1-4 (RPC #100021)
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: cicada.vl0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC-JPQ225.cicada.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC-JPQ225.cicada.vl
| Issuer: commonName=cicada-DC-JPQ225-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-09-13T10:42:50
| Not valid after:  2025-09-13T10:42:50
| MD5:   2b54:f7f1:53c6:0241:c432:c868:1d86:5ec7
|_SHA-1: eef8:12f9:0a11:c0d5:16c1:c499:9abf:3341:4419:6a2b
|_ssl-date: TLS randomness does not represent time
3269/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: cicada.vl0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC-JPQ225.cicada.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC-JPQ225.cicada.vl
| Issuer: commonName=cicada-DC-JPQ225-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-09-13T10:42:50
| Not valid after:  2025-09-13T10:42:50
| MD5:   2b54:f7f1:53c6:0241:c432:c868:1d86:5ec7
|_SHA-1: eef8:12f9:0a11:c0d5:16c1:c499:9abf:3341:4419:6a2b
|_ssl-date: TLS randomness does not represent time
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2024-12-13T07:11:07+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=DC-JPQ225.cicada.vl
| Issuer: commonName=DC-JPQ225.cicada.vl
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-09-12T15:21:57
| Not valid after:  2025-03-14T15:21:57
| MD5:   e356:22df:9b7a:d588:46f6:a65e:3788:73e1
|_SHA-1: d206:e12e:961c:9184:3789:b9fd:c616:4942:c661:7ae7
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49678/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49681/tcp open  msrpc         Microsoft Windows RPC
59509/tcp open  msrpc         Microsoft Windows RPC
59549/tcp open  msrpc         Microsoft Windows RPC
60829/tcp open  msrpc         Microsoft Windows RPC
60939/tcp open  msrpc         Microsoft Windows RPC
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2022 (89%)
Aggressive OS guesses: Microsoft Windows Server 2022 (89%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 0.031 days (since Fri Dec 13 07:26:57 2024)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: Host: DC-JPQ225; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2024-12-13T07:10:32
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

53/udp   open  domain?
| fingerprint-strings: 
|   DNS-SD: 
|     _services
|     _dns-sd
|     _udp
|_    local
123/udp  open  ntp?
| ntp-info: 
|_  receive time stamp: 2024-12-13T06:39:01
2049/udp open  nlockmgr 1-4 (RPC #100021)

```

![{61F2BAD8-A7E1-4153-AD80-D6CE33900DF0}](https://github.com/user-attachments/assets/57944127-7eae-4f8a-8eb6-a137e6047acb)

hmmmmmmmm
Basic smb enum got me nothing.
- lt's check 2049

szybka akcja

![{F4FE0B05-6112-49F2-97CA-29F6E4719475}](https://github.com/user-attachments/assets/9fde1524-5f51-4e0c-81e3-57c60a1b5175)

I also checked there folders recursively.

![{C42F4FD1-D972-48A5-9BB8-226C53B69D14}](https://github.com/user-attachments/assets/8be20f4a-9485-43f6-9d32-3ef4d432fbc1)

![{46CF211A-84ED-474B-B6BC-A4F022F8772D}](https://github.com/user-attachments/assets/d17b1293-27cc-4d16-ac0e-6223996ca27c)

![{246CCE62-D1EA-4A12-B737-C71A55476489}](https://github.com/user-attachments/assets/1da26cc8-9ddb-40b9-9330-30ae231b61f0)

looks like her password :D
- but it failed so I will try this

![{416736C0-E495-4B6A-AEEE-11FEBE2B01CA}](https://github.com/user-attachments/assets/f3d9201d-6cdf-468c-9194-971583d57941)

![{7A60C5A5-E6B4-4F40-B628-139EE9A92771}](https://github.com/user-attachments/assets/4da72408-1d62-4059-a48b-827902726db3)

echo co oni znowu wymyślili...

aaaaaaa dobra. Ogarnąłem po chwili o co chodzi. 

![{E5C7176B-CEA9-4605-8B12-25E76D9BDBEF}](https://github.com/user-attachments/assets/4a59c030-5ff2-4009-8c28-b1c63759832e)

`STATUS_NOT_SUPPORTED` mówi nam o tym, że NTLM jest wyłączony. Wystarczy `-k` dodać.

![{BF17CF0D-C470-460F-9B93-A55A4734AB32}](https://github.com/user-attachments/assets/2cdef5e4-1a92-4fdf-8c3c-a3fb1cebbd12)

![{BE2E09EF-CB3F-4A28-B61C-31DB2BFE149E}](https://github.com/user-attachments/assets/0cbf9731-add5-49c0-9c82-817a3b2e59e0)

```
export KRB5CCNAME=rosie.powell.ccache
```

![{4B04A3F4-C7FA-439A-952A-E8847438C06D}](https://github.com/user-attachments/assets/cb755ea3-0b97-4702-b68a-bdce8115f7c7)

![{018B35AB-00EB-4197-B7CE-2223CA219A96}](https://github.com/user-attachments/assets/8945654f-7da0-4d41-bdc6-e2d1110ff057)

zatem mamy ECS8.

Dobra lekki resarch i Nazwa CICADA8-research wygląda jakby to miało być powiązane :D
[https://github.com/CICADA8-Research/RemoteKrbRelay.git](https://github.com/CICADA8-Research/RemoteKrbRelay.git)

