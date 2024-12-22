# Redelegate
Windows, Hard, created by **geiseric**


```
21/tcp    open  ftp           Microsoft ftpd
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-12-22 10:58:02Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: redelegate.vl0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
1433/tcp  open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: redelegate.vl0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=dc.redelegate.vl
| Issuer: commonName=dc.redelegate.vl
5357/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49672/tcp open  msrpc         Microsoft Windows RPC
49675/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49676/tcp open  msrpc         Microsoft Windows RPC
49932/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
51931/tcp open  msrpc         Microsoft Windows RPC
51944/tcp open  msrpc         Microsoft Windows RPC
51945/tcp open  msrpc         Microsoft Windows RPC

53/udp   open          domain       (generic dns response: SERVFAIL)
88/udp   open          kerberos-sec Microsoft Windows Kerberos (server time: 2024-12-22 10:58:34Z)
123/udp  open          ntp          NTP v3
137/udp  open|filtered netbios-ns
138/udp  open|filtered netbios-dgm
500/udp  open|filtered isakmp
4500/udp open|filtered nat-t-ike
5353/udp open|filtered zeroconf
```

![{A3D43BF8-CF3E-441B-B864-290B3C4E2542}](https://github.com/user-attachments/assets/4db50091-29e1-4c63-b555-b34e9097e136)

![{805898F8-B934-4BCF-86AF-87CEA7BE8B0D}](https://github.com/user-attachments/assets/60b40c8e-4013-44e4-99f2-b1613691059b)

jakieś hasełko mamy

![{99F1E6FF-C98C-4F70-B8C4-431F862FDAB5}](https://github.com/user-attachments/assets/4c133add-7772-463f-8fc9-d1e3ee893549)

usernameów tak nie wyciągniemy

![{AEF8DC68-DD44-41EC-9455-21255917FD18}](https://github.com/user-attachments/assets/9081151a-224f-4df1-82ef-dc95ac6a8529)

tak też nie

![{75709C42-4A6E-44F4-8885-784CAD8FA5CB}](https://github.com/user-attachments/assets/eee6f596-9a3b-4462-af42-975101bff2a8)

ani tak.

![{642FAFF3-E7D8-4964-8488-D72F30FB31C5}](https://github.com/user-attachments/assets/171a13c1-cba2-44a5-b921-9d8141fe6510)

też pusto

![{DAD2659C-D06A-403C-9178-8E7672F612C9}](https://github.com/user-attachments/assets/25e96066-3cfb-4175-8503-2e3fb068ee41)

to lecimy z listą bez keepassa.

Jestem leniwy więc posłuzyłem się GPT

![{A5C21B18-3668-40B8-8315-334F0991153D}](https://github.com/user-attachments/assets/2c72f134-4b36-4353-8875-80de5b7de846)

ale gpt jak to gpt potrafi zepsuć więc poprawka.

![{D14FEC53-901B-4FEA-87EF-AA08446920D7}](https://github.com/user-attachments/assets/916e3612-a5e7-4526-ba3d-d3d07df0670c)

![{CD92CC7D-8D94-4531-AB91-FDE8A6FD0827}](https://github.com/user-attachments/assets/0bf99c39-2a94-4031-b4ce-47d35008b7cc)

jeszcze mamy `fall`, które coraz mocniej zyskuje na popularności to dodam (poprzednie nie weszły)

![pass](https://github.com/user-attachments/assets/28b7aab8-dcf1-4925-b432-918f88ace630)

![{577F136C-E254-402A-8EE1-65EE7A8110F5}](https://github.com/user-attachments/assets/d543718d-f324-4471-8f3b-0fcd6f690b3e)

to pobieram wszystko i testujemy.

w sumie 7 haseł z czego 6 meeeega silnych

![{67DFB193-A037-41E8-B62F-9CC5543D1108}](https://github.com/user-attachments/assets/28dd9056-70d7-4ce4-9b51-283cb663cb15)

dobra mssql działa to lecimy

chyba klasyczkiem polecaimy.
```
SELECT DEFAULT_DOMAIN();
SELECT SUSER_SID('REDELEGATE\Domain Admins')
```

![{AB95BE11-DB13-4471-A262-4ED547B6CC73}](https://github.com/user-attachments/assets/1db67aa4-2609-415e-98d9-30bf112d37f0)

https://www.netspi.com/blog/technical-blog/network-penetration-testing/hacking-sql-server-procedures-part-4-enumerating-domain-accounts/



