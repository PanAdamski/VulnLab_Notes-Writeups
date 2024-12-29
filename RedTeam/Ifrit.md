# Ifrit
Mixed, Easy, created by **xct**

![ifrit_slide](https://github.com/user-attachments/assets/e26e203b-cc12-4d1b-9e36-84a0a07e24bf)

Okey. My first redteam lab on **vulnlab**.

![{A169F024-F3BF-44AD-ACEB-1EEE31E985C0}](https://github.com/user-attachments/assets/69c76728-ec10-462f-9a09-6371c5d2cd8c)

We have intro here https://wiki.vulnlab.com/guidance/ifrit-red-team-lab

add too /etc/hosts
```
172.16.40.225 vdi02.eu-ifrit.vl
```

```
Besides reaching the main objective, your secondary goal is to complete the objective without triggering any detection. If you manage to do so, please write a message to xct.  Please do not RDP to DEV05, a user is working on a critical project there.
```

```
If you haven't regenerated your vpn pack recently, add these routes manually:

sudo ip route add 172.16.40.0/24 via 10.8.0.1 dev tun0 
sudo ip route add 172.16.41.0/24 via 10.8.0.1 dev tun0
```

```
Make sure you have good enumeration methodology that includes at least: AD, ADCS, Shares, Ports, Services, Installed Programs, Users on Machines. Good enumeration is key - both here and in real environments.
The 172.16.41.0/24 Subnet is behind a network firewall - you won't be able to reach your own attacker machine on all ports (but on some).
Not everything you see is exploitable - go for the low hanging fruits as you would on real engagements.
```

lets go!!

I run
```
nmap -Pn -T2 --top-ports 10 -v vdi02.eu-ifrit.vl
```
```
21/tcp   filtered ftp
22/tcp   filtered ssh
23/tcp   filtered telnet
25/tcp   filtered smtp
80/tcp   open     http
110/tcp  filtered pop3
139/tcp  filtered netbios-ssn
443/tcp  open     https
445/tcp  open     microsoft-ds
3389/tcp open     ms-wbt-server
```

![{A7B582AD-195C-442C-837F-5F44A970685B}](https://github.com/user-attachments/assets/eb199779-1e11-46f0-b360-353e5ffd00d9)

![{16C098F8-8659-4A66-B27B-5810AA5AFC8D}](https://github.com/user-attachments/assets/2b974673-3884-46dc-9798-9e04c2dd2f08)

I press firefox and get .rdp file

![{37D03FBD-BFA8-4926-80CA-FF1E44CCF842}](https://github.com/user-attachments/assets/00d03eec-5eb0-436f-bf6f-0b572e340643)

![{29BFE250-619C-4C54-96E2-2B01F79797FD}](https://github.com/user-attachments/assets/2e601f42-aa64-46e8-9773-e1de9cef84a3)

```
sudo apt install remmina
```

and after instalaion press .rdp file again 

![{6A2301C7-1593-4ACE-BA6F-16F942CBD6E1}](https://github.com/user-attachments/assets/a73a3f73-dc07-4ed8-8b3b-6694abac852a)

![{966758EC-3028-471A-BCD2-F0DD8094ED47}](https://github.com/user-attachments/assets/66390bb4-46e9-40ac-9ced-ab41376e6a93)

![{5A056418-E4F9-4820-9607-65C58B91C2A0}](https://github.com/user-attachments/assets/cd225e67-43ab-4b4a-94d4-b68b200acfad)

After wasting 30 minutes trying, I decided to change my strategy and... it worked

![{A0D49D73-999F-4CF2-9D79-9A0DC31E7254}](https://github.com/user-attachments/assets/0eaf6f7c-20f8-4c79-873f-0a02a6a7ad5c)

`whoami` trigger SIEM so don't use it.

teraz taka mała sztuczka, która może się przydać w penteście, ale w redteamie nie, bo triggerujemy w ten sposób SIEMa. Szukamy sobie DCka będąc na przejętym komputerze
```
nslookup _ldap._tcp.dc._msdcs.<domain>
nslookup _ldap._tcp.dc._msdcs.eu-ifrit.vl
```

![{01260CE1-8716-4201-8DA9-AF20309A68E2}](https://github.com/user-attachments/assets/88c55092-4171-4451-a8c8-8316e0c80478)

kali does not have access to the domain controller. You would need pivoting here

z takiego ogólnego rekonesansu widzimy, że administrator domenowy tutaj wpadał

![{CB8B4391-58F7-4E33-8C3B-8D498B4C0196}](https://github.com/user-attachments/assets/cbdd6fa7-f4d4-4183-bdcc-18374a970ef6)

wróciłem sobie po prawie miesiącu i kilka obserwacji od zera, na chłodno.
Po pierwsze user `Tina.Dawson` jest trochę inna niż pozostali userzy.

![{2C0CDB79-297E-42F0-BE3B-D022E1B26C4A}](https://github.com/user-attachments/assets/c1cd6ede-a8f4-4934-a203-a4ebd7c0de1d)

dla testu zapuściłem nmap i SIEM milczy hehe.
```
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: IIS Windows Server
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
135/tcp  open  msrpc         Microsoft Windows RPC
443/tcp  open  ssl/http      Microsoft IIS httpd 10.0
| ssl-cert: Subject: commonName=VDI02.eu-ifrit.vl
| Issuer: commonName=VDI02.eu-ifrit.vl
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-08-01T09:17:54
| Not valid after:  2025-01-31T09:17:54
| MD5:   d5b5:7ce7:06e1:78e5:4bc3:1ebd:9c8e:609e
|_SHA-1: 1f48:52e9:c410:f0bb:16e7:e015:341f:6f69:fec2:b0ce
|_http-title: IIS Windows Server
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
| tls-alpn: 
|_  http/1.1
|_http-server-header: Microsoft-IIS/10.0
|_ssl-date: TLS randomness does not represent time
445/tcp  open  microsoft-ds?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=VDI02.eu-ifrit.vl
| Issuer: commonName=VDI02.eu-ifrit.vl
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-12-27T13:56:50
| Not valid after:  2025-06-28T13:56:50
| MD5:   0c5b:6847:9f44:568a:424f:fd20:ab83:430f
|_SHA-1: 232e:bff0:5ef0:9fb4:02a3:e9a3:b765:b526:4e32:acf2
|_ssl-date: 2024-12-28T14:22:19+00:00; +7s from scanner time.
5357/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
```
- szczerze to nic ciekawego nie pokazał.

![{B7399B99-9CA6-4C1E-A185-E03BD606812A}](https://github.com/user-attachments/assets/838559b3-8b04-41d1-ae98-8abca240c1a2)

a ta Tina to serio wyjątkowa.

WTF?! Nie wiem co się stało, ale po miesiącu nagle RDP działa bez problemu... teraz to ja z górki mam.

![{824001E6-703B-4A9C-ACB7-2D6446A7A37E}](https://github.com/user-attachments/assets/98700c6f-b6e6-444f-aa3b-397bb3e26826)

jesteśmy w kiosk'u firefoxa.
Ctrl+O

![{26040EE4-3533-4CCC-8908-0EF0525256B8}](https://github.com/user-attachments/assets/0b0300da-e9af-4a26-bb34-40e368420f8b)

![{B4F3FA81-E55F-4478-9BE4-E5B9D7565A5C}](https://github.com/user-attachments/assets/a2d31840-f9e7-43cc-9f2a-5f5e5b5ec172)

![{2850A516-38C9-4A59-AE77-DB7072C9E6FF}](https://github.com/user-attachments/assets/685042a7-e26d-4566-a256-b064fd272de4)

![{896EC16B-7A35-4C40-B6A7-10A9A1E9229E}](https://github.com/user-attachments/assets/c608ba63-54e1-4d10-a060-bfb5a7d587f9)

![{69FFD1BB-3FBE-440C-A69A-D47E0DFAA8F4}](https://github.com/user-attachments/assets/27a5beba-e997-4c04-805b-edc5123b4945)


iiii w sumie mamy tak jakby "normalnego windowsa" już.

![{1846675F-30C4-48AC-AFBC-9638E134D59C}](https://github.com/user-attachments/assets/5d7e0fd4-9a64-4c71-985a-2efd4669ac8e)

o pierwsze informacje.

![{1B01A55E-54FB-4EF2-95B2-FBBBA697313E}](https://github.com/user-attachments/assets/b6172f3c-12d6-4a7d-beb6-862b311ed726)

w inetpub nie mamy write.

wykorzystując jedną z najprostszych metod do enumeracji userów znajdujemy hasło z opisie.. chyba ldapa.

![{BFCC1FDA-B7C8-47B9-AF63-880218DCF21F}](https://github.com/user-attachments/assets/c791ed37-b57e-4303-a4cb-4edbe5c3d9f8)

- dwóch userów takie ma
- to prawdopodbnie honeypot users :(

Fajnie byłoby jakoś sieć poskanować, ale bez wrzucania dodatkowych tooli.
- ale nie umiem tego zrobić więc chyba załaduję chisla xD

![{A70CE51F-1596-4080-8B6B-C540F5730656}](https://github.com/user-attachments/assets/fa356d46-e443-4ce0-8b9f-b9ed90bc83c5)

w sumie czułem, że jakby to tak działało to byłoby za pięknie. W takim razie sliver też odpada.
- pomyślałem o ssh, które jest wbudowane w kazdy windows serwer... tutaj nie jest

Żeby nie budzić EDRa wpisywaniem `ipconfig` zerknimy na DCka za pomocą GUI.

![{CA3DD4BD-24E7-4384-9B8C-7D4938872AAC}](https://github.com/user-attachments/assets/7e87f24d-e22f-495e-bb0f-13466086cd3a)

wiemy, że DC (dns serwer) to `172.16.41.14`.

Sprawdzam share'y na tym DCku

![{B547A980-2E71-4C93-95CA-9225C951C7C5}](https://github.com/user-attachments/assets/f21067c9-e914-4c35-b753-58ca4952f2e2)

- puste foldery

Wróciłem do tego ssh, bo coś mi mocno śmierdzi.

![{23B6C5EE-65B7-4044-9277-A9EEDFBC7C1A}](https://github.com/user-attachments/assets/87a9e61a-8e35-4677-a573-846217bdd370)

*sprawdź net view \\172.16.41.14\ jutro*

Dziiiwne. Wczoraj `ssh` nie działało, a dzisiaj działa.

![{D1CEBAF7-2A10-474B-8178-2EE33A5CDD0B}](https://github.com/user-attachments/assets/4bfbdaf7-413a-4273-8d53-a1751014fe9e)

No to zrobię sobie revproxy przez ssh łącząc się do siebie i powinno być ez.

![{F874824F-C82A-4D55-BF94-8C29D90826AD}](https://github.com/user-attachments/assets/c3c7d37d-dac3-4bc7-b5c0-7d19f7521042)

```
ssh kali@10.8.1.184 -p 2137 -R 1080 -N
```
Teraz można sieć skanować.
- zrobię to mało redteamowo, żeby zobaczyć czy EDR coś pokaże.

![{5FC56815-D54B-42B0-BF78-8D12E0DCE1B6}](https://github.com/user-attachments/assets/fd2752ae-abf4-4aac-8a44-8a26b68606e6)

![{924B9948-F51B-4B2A-AE7A-018A8D64003D}](https://github.com/user-attachments/assets/d2c1159f-2ac3-4036-8191-eb366c7b32de)

hmmmm dziwna sprawa. Coś źle zrobiłem?

doooobra. Dwie rzeczy. Pierwsza to

![{AF783357-77D7-4335-B3D6-D07BCF132DE6}](https://github.com/user-attachments/assets/94fc7023-dc06-404a-b181-1c433f7ca1a7)


a druga to.. inny range skanuję xD
172.16.41.0/24 - to prawidlowy

![{518EC699-F159-4E78-AFA9-C88110007EA7}](https://github.com/user-attachments/assets/992333ca-034b-4822-9afa-fd2d7f55a72b)

mało coś (ja kwidzę DC07 to zakładam, że 4,5,6 też istnieją. Ale zacznijmy od tego DCka z DNSów czyli .14

(przy okazji EDR aż krzyczy)

![{979D5FDA-91B6-424E-A190-9C5F2E68A2B8}](https://github.com/user-attachments/assets/4fa88a7f-f99b-46f8-b54f-7cdfbdbf1cdc)

![{9B3DE66B-E8F1-4E88-B340-9A8A822A147D}](https://github.com/user-attachments/assets/5043974c-2408-4cf0-80bf-c7eb71240970)

dobra coś się tutaj dzieje. Mamy np. `home-backups$`, których nie było widać z GUI.

![{286E646C-D916-49DF-AC0D-2A1A5D9A6B17}](https://github.com/user-attachments/assets/c38367f8-25c8-42dc-b78b-ea4978fd16dd)

ooo `.vhdx`. Zaskoczyli, nie powiem.
- zaraz analiza poleci, ale najpierw coś sobie w tle poskanuje. Zapewne mogę wysłać plik bez drażenienia EDRa tylko sharem `transfer` i tak zrobię.

![{24C2BCA0-FDE9-4A11-AC07-24C7335D3457}](https://github.com/user-attachments/assets/2a36ed4d-26c3-4704-82f8-f6c0c2af567b)

![{3B253F46-D8C5-4B20-AF05-146B92BC7C07}](https://github.com/user-attachments/assets/46015bbe-5b48-4d35-8f04-263bec22c30e)

![{6F20D867-04B7-4957-925E-A0F6647A103F}](https://github.com/user-attachments/assets/59b3e50c-b17d-49f5-aa5c-de518ec44b1f)

dll można.

![{A09E2F44-5AB2-4741-B50F-C1390DA3BA93}](https://github.com/user-attachments/assets/d386b640-fbcf-48db-a3cd-f7ebe6aa7082)

exe, msi, script nie można.


ale zerknijmy na te rulsy, bo to kurczę jednak easy i nie chce mi się wszystkie przekompilowywać na dllki.
```
<FilePathRule Id="fd686d83-a829-4351-8ff4-27c7de5755d2" Name="(Default Rule) All files" Description="Allows members of the local Administrators group to run all applications." UserOrGroupSid="S-1-5-32-544" Action="Allow"><Conditions><FilePathCondition Path="*"/></Conditions></FilePathRule>

<FilePathRule Id="a61c8b2c-a319-4cd0-9690-d2177cad7b51" Name="(Default Rule) All files located in the Windows folder" Description="Allows members of the Everyone group to run applications that are located in the Windows folder." UserOrGroupSid="S-1-1-0" Action="Allow"><Conditions><FilePathCondition Path="%WINDIR%\*"/></Conditions></FilePathRule>

<FilePathRule Id="921cc481-6e17-4653-8f75-050b80acca20" Name="(Default Rule) All files located in the Program Files folder" Description="Allows members of the Everyone group to run applications that are located in the Program Files folder." UserOrGroupSid="S-1-1-0" Action="Allow"><Conditions><FilePathCondition Path="%PROGRAMFILES%\*"/></Conditions></FilePathRule>
```
W skrócie to
- Administratorzy mogą uruchamiać dowolne pliki z każdego miejsca.
- Wszyscy użytkownicy mogą uruchamiać pliki z folderu Windows.
- Wszyscy użytkownicy mogą uruchamiać pliki z folderu Program Files.

weźmy jeszcze scripts
```
<FilePathRule Id="06dce67b-934c-454f-a263-2515c8796a5d" Name="(Default Rule) All scripts located in the Program Files folder" Description="Allows members of the Everyone group to run scripts that are located in the Program Files folder." UserOrGroupSid="S-1-1-0" Action="Allow"><Conditions><FilePathCondition Path="%PROGRAMFILES%\*"/></Conditions></FilePathRule>

<FilePathRule Id="9428c672-5fc3-47f4-808a-a0011f36dd2c" Name="(Default Rule) All scripts located in the Windows folder" Description="Allows members of the Everyone group to run scripts that are located in the Windows folder." UserOrGroupSid="S-1-1-0" Action="Allow"><Conditions><FilePathCondition Path="%WINDIR%\*"/></Conditions></FilePathRule>

<FilePathRule Id="ed97d0cb-15ff-430f-b82c-8d7832957725" Name="(Default Rule) All scripts" Description="Allows members of the local Administrators group to run all scripts." UserOrGroupSid="S-1-5-32-544" Action="Allow"><Conditions><FilePathCondition Path="*"/></Conditions></FilePathRule>
```
- Wszyscy użytkownicy mogą uruchamiać skrypty z folderu Program Files.
- Wszyscy użytkownicy mogą uruchamiać skrypty z folderu Windows.
- Administratorzy mogą uruchamiać dowolne skrypty z każdego miejsca.

W sumie to jak możemy ładować .exe z C:\Windows to... do TEMP można załadować.

Na poziomie explorera uruchamiam `C:\Windows\Temp\ADExplorer64.exe` i wszystko śmiga.

![{0A78B0B5-0553-4AA3-91C3-FEE09516F5DB}](https://github.com/user-attachments/assets/9975ff4f-6c30-44cc-a1a5-bc0913b0bc41)

![{F9DBCCB8-B3AB-4DBC-AD09-3B3CD0AA42CA}](https://github.com/user-attachments/assets/5113c11d-8840-4f1a-af85-5f67a8196061)

![{C7814BEF-7171-4063-9BA6-FA7750634622}](https://github.com/user-attachments/assets/34391d21-0179-48d3-9aa6-a76aee35d0be)

yeeeee

Zrobię sobie snapshot, żeby móc to sobie przejrzeć u siebie na linuxie.

![{71DE150F-DFCA-4726-8BEA-958A3F35AA66}](https://github.com/user-attachments/assets/3fa5e8ba-aa12-42c1-b1f7-f670bbef2175)

![{306CE012-9B18-40B2-8034-20F2FA47ED19}](https://github.com/user-attachments/assets/afb71479-5fe7-4396-ab1e-bd337f27813b)


zmieniam folder bo tam nie mamy dostępu na kopiowanie.

![{EA517D3E-5AE2-48BC-A2C7-3FB77E6677D0}](https://github.com/user-attachments/assets/466dfd61-643c-4045-80eb-e1af2e253330)

![{2A0B9619-A0E5-4FE2-B5CE-87749DBC8705}](https://github.com/user-attachments/assets/68967b31-a82d-46f7-9f80-15a744e6a3ad)

![{B7B2C5F2-0F95-4A60-812E-E5C59671CD44}](https://github.com/user-attachments/assets/ab9f9c69-57b7-4deb-9a84-3377e21844dc)

![{7126B6FF-DB54-47B4-A745-6E21DE50BE14}](https://github.com/user-attachments/assets/774286b6-4394-4e88-9ac0-ac9ffd962db2)

- coś nie działa, coś źle zrobiłem.

![{4D478990-9D24-4917-956C-38B2135CDF41}](https://github.com/user-attachments/assets/e9b2a761-bb6d-4bfc-81bf-e4be9d21d683)

może teraz

![{B28E0CD9-9355-4E13-9167-A9767A43A0F2}](https://github.com/user-attachments/assets/06615a03-642f-4d79-8aa7-dd5e61d66d8d)

nadal źle :/
- przeinstalowałem bloodhound i neo4ja, ale dalej nie idzie progres uploadu :/

![{29A3E8A8-4B5D-412A-905B-4D7989EC7656}](https://github.com/user-attachments/assets/92c732f4-1b1a-4f0a-8bcb-38227905f8b7)

Przeniosłem się na BHCE

![{7E9337B9-2650-4AA2-A1D0-ECEEA6BA402F}](https://github.com/user-attachments/assets/d128f4c3-73aa-4659-ab1e-5e66e795ec93)

![{779B90E4-C082-4323-B14C-ACDBF2D53650}](https://github.com/user-attachments/assets/017931ea-8b99-4944-966e-02452b274813)

całkiem płynnie działa.

![{289EB638-548E-40A1-9D0C-B32415ACEDA2}](https://github.com/user-attachments/assets/efcb5023-0506-4e44-8f77-bf25a90e04bd)


chwilkę przeglądania i widzimy ciekawą rzecz `WriteAccountRestrictions`.

![{0F9CA6C9-39E0-4AE2-A381-1F7B02ABCB9B}](https://github.com/user-attachments/assets/458dd0fb-145b-447a-a828-8f6918ba2a54)

![{1815691C-F10A-4159-8F76-5E33007F6A28}](https://github.com/user-attachments/assets/ed5bd8f9-11f9-4af5-9b93-feb600b4a5b8)

jednakże nie wydaje się to być prosty przypadek.

![{0C6455B2-169E-42A2-B762-F2042F0C7620}](https://github.com/user-attachments/assets/59d8a8ee-a9fb-4605-9af8-e03586e3afa9)

jeszcze sobie fake lnk stworzyłem i czas na spacerek/przerwę

![{62223086-A267-4EC0-8078-4F081CEB1E49}](https://github.com/user-attachments/assets/3e21f536-0262-49ee-ab70-b83fa2b6a1dd)

działa, bo jak wszedłem to hash od ręki
