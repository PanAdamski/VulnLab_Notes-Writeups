# Unintended 
Linux, Medium, created by **kavigihan**

```
10.10.129.101
10.10.129.102
10.10.129.103
```

```
PORT      STATE SERVICE      VERSION
22/tcp    open  ssh          OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
53/tcp    open  domain       (generic dns response: NOTIMP)
88/tcp    open  kerberos-sec (server time: 2024-04-25 17:54:13Z)
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Samba smbd 4.6.2
389/tcp   open  ldap         (Anonymous bind OK)
445/tcp   open  netbios-ssn  Samba smbd 4.6.2
464/tcp   open  kpasswd5?
636/tcp   open  ssl/ldap     (Anonymous bind OK)
3268/tcp  open  ldap         (Anonymous bind OK)
3269/tcp  open  ssl/ldap     (Anonymous bind OK)
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC


22/tcp   open  ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
80/tcp   open  ssl/http Werkzeug/3.0.1 Python/3.11.8
8200/tcp open  http     Duplicati httpserver


21/tcp open  ftp     pyftpdlib 1.5.7
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
```

ports shows as domain+subdomain

![{55525783-2357-494E-90A3-3C70FBB62648}](https://github.com/user-attachments/assets/a417773e-69aa-45e6-956b-1c4607ebe43a)

![{3C3D308F-88CD-4337-B530-E7876D00E14D}](https://github.com/user-attachments/assets/6374a3fe-bd60-41ce-999f-4a9ba6fb3dca)

o i mamy dwie subdomenki dodatkowo.

![{EF9D76A1-7DE2-4A65-87D4-179C951961EA}](https://github.com/user-attachments/assets/3406ef65-7d74-477e-8752-418e90541770)

I found gitea and some commits

![{C62A5609-C641-494C-B28C-0915CB20DE61}](https://github.com/user-attachments/assets/5e0151c7-710e-4a2b-b568-a77e73546f96)

![{C26D7A2E-B44F-4E9C-A064-2FC1FB7F912C}](https://github.com/user-attachments/assets/41e1dd48-33cf-4ec9-881a-4f1a8b4c7c54)

oooo

![{80DC0829-9754-4A80-8685-657D04C660B7}](https://github.com/user-attachments/assets/8a53d6de-9aed-4b0d-acfc-01f5aa365eca)

mamy dwa usernamy
```
ratul
nanee
```

![{FBD21D94-853D-47DE-A0A1-06CEF11C64A1}](https://github.com/user-attachments/assets/b922d524-471b-46a3-a9a7-7a686b88fad0)

o i hasełko do mysqla

![{B4A078D3-B0D6-4434-90C7-ED2B53B9D45A}](https://github.com/user-attachments/assets/d86c434b-7d2d-4aa0-8fc0-bd380f7a66ec)

![{6F3513E4-12B3-41D3-ADC7-CE7FA20821B8}](https://github.com/user-attachments/assets/a223974a-4e7e-40cc-b69a-1190ba00b99f)

jezu ile tego się zrobiło

![{F8F484C8-6A09-41B1-872F-0212EE1954DB}](https://github.com/user-attachments/assets/cfdf0367-52c2-4d45-a82a-79c56b65685e)

![{DF219167-3855-4399-A8BA-06546587B4E2}](https://github.com/user-attachments/assets/4fb9c733-d3fb-48b0-a6ce-1c364d4a371e)

creds works from 2nd host. We can't login but I think pivoting i available.

![{80F73198-4969-43B0-8E89-D5A0FA44A9FA}](https://github.com/user-attachments/assets/6aa70951-66c8-47bb-ade7-9af3d318ce6c)

Fast check for new ports running localy.
```
proxychains4 -q nmap -Pn -v 10.10.129.101 10.10.129.102 10.10.129.103 -p- -T4
```
Ale tak na logikę to tam powinno lokalnie mysql siedzieć.

![{2845988A-B052-4019-92C5-A3B69369FFB7}](https://github.com/user-attachments/assets/854c384d-c0b9-4f56-8c88-cb929cc6ce23)

NIE ROZUMIEM czemu nmap nie pokazuje mi otwartego 3306, a łączę się tam

![{0533AC8E-4D1B-488D-B558-43463CBC8F2F}](https://github.com/user-attachments/assets/917b3fe1-c7ef-4481-b872-2876d61028a7)

we have two hashes.

![{D1BCA209-29CE-4F7D-AD67-69D4D8EE10AD}](https://github.com/user-attachments/assets/d7c7ad14-8bcb-44f4-b65f-9a2c27ce2afb)

mamy też jakieś prywatne repo.


![{DE5ED2DD-3322-41C9-87BD-3D47FCE946FA}](https://github.com/user-attachments/assets/e9d2a637-b25f-4a52-adf6-6fdfd2ea8d92)

![{70F92C6C-C219-49CB-BB91-F087892041FB}](https://github.com/user-attachments/assets/e13b978a-9567-47be-9424-4b8393ceb69c)


widzimy drugie repo od razu

![{6A957D28-F679-492E-B0AB-7A628C7C0A11}](https://github.com/user-attachments/assets/8bfbb572-f568-4172-a16c-5db08a2e145f)

![{B2DDFDEC-3C9B-4B7F-A2C5-3E2AA7F0215E}](https://github.com/user-attachments/assets/6edbbfb8-6667-413b-b8b7-dfb002807eb5)

![{BC3A774B-3721-4DE4-8204-AEDEFDD7434F}](https://github.com/user-attachments/assets/5aeae477-7fc4-4b0b-9604-e65d83c0c447)


![{2B9896C8-1F5A-4725-9BB1-67A62C55F61A}](https://github.com/user-attachments/assets/91e2e4b9-ae72-4a40-9fbf-825e4d7702bf)

miałem nadzieję, że jeszcze gdzieś wejdzie, ale nie udalo się

![{C49D3BBC-4BB0-43A6-B68F-85CE7A99E1F1}](https://github.com/user-attachments/assets/b2508eca-e25a-4ce8-9253-26497e65f725)

o jeszcze tak spróbowałem i weszło. Nice

![{5D472F65-BFBE-4AE6-A39B-6AEC650739F1}](https://github.com/user-attachments/assets/eaeea655-9256-4356-a622-80e7c28b0873)

ooo pierwsza flaga.

![{6F23BAB2-1944-4459-8866-C9FBD3E8D15B}](https://github.com/user-attachments/assets/42283634-28fd-40df-880d-d4ad36cd4e2f)

wstępnie nic ciekawego u innych userów.
