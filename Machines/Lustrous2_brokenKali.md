# Lustrous2
Windows, Hard, created by **xct**

![lustrous2_slide](https://github.com/user-attachments/assets/685f71ad-a8f6-4fd4-8bda-8a65f2371c58)


```
21/tcp   open  ftp
53/tcp   open  domain
80/tcp   open  http
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl
5357/tcp open  wsdapi

53/udp  open  domain       Simple DNS Plus
88/udp  open  kerberos-sec Microsoft Windows Kerberos (server time: 2024-12-27 14:52:43Z)
123/udp open  ntp          NTP v3
```

![{EC0FE614-B501-42EF-AAF0-ED794F86318A}](https://github.com/user-attachments/assets/a247c3ed-2832-4acb-8d1b-9333b06fdbcf)

- brak ftp anonymous login
- brak guest i null smb session/shares/rid
- brak anonymous ldap information
- noooo ciekawe, bo pomysły się kończą.

![{14D5A3F8-2A50-4253-981A-24D5250C2A48}](https://github.com/user-attachments/assets/6f128a24-e491-4b7d-82ea-14f5354b7e5a)

![{259DE282-01B5-4C4B-B0B9-BAACFA93862E}](https://github.com/user-attachments/assets/1b9ff9dd-36a4-4f26-ba82-2e1ddfbf92cb)

aha gpt pomógł.

Trochę nie chciało mi się tego klikać to w GUI machnąłem (tak.. wiem, że wstyd).

![{6EA18278-EC58-48FD-95E2-9157DB9EDED0}](https://github.com/user-attachments/assets/9501b2ca-7108-4a8b-a97e-7aba1aa21f0e)

![{9D0F0D40-0A9C-4C74-BAF9-653D86EC5F39}](https://github.com/user-attachments/assets/4cdd8fc6-d876-41e9-8992-40bee06bdc22)

![{E72EF236-6B15-486D-AD16-713AD4EE45D8}](https://github.com/user-attachments/assets/d035a0a0-cac2-4f45-8dbd-897c20af6528)

w sumie.. nic tu nie ma.

![{4F8E6350-ABFE-4771-9B81-57B114A779AB}](https://github.com/user-attachments/assets/e4a4966d-0844-4df4-8e14-185920df1f82)

dooobra. Chodzi o liste userów z folderów. Już wszystko jasne.

![{B03BBE21-C27F-43D0-B00A-FA0F164D2E1D}](https://github.com/user-attachments/assets/d931cae7-6f50-4bed-be37-44408ceaddbb)

mamy liste 71 userów.

![{0BECA9AC-60F6-4BE0-BAD2-1EE700FD28B4}](https://github.com/user-attachments/assets/7501b713-09c1-4150-bd13-3ebc5e439c80)

![{A31D2EEE-70E6-4CE2-A3E4-4657F509756F}](https://github.com/user-attachments/assets/a0c143df-eca3-41e8-8149-e1da28914137)

![{E14FECD2-0C3B-4501-BA96-5E7E2C7ED86E}](https://github.com/user-attachments/assets/80c8e058-7569-4906-9b89-3eceab0888f9)

![{8F7FE5EA-4B81-40E2-8E1D-A197841D47C7}](https://github.com/user-attachments/assets/80451c8d-4b4f-4b86-9106-b0dbf2a7101b)

O NTLM wyłączony. Zaskoczyli.

```
nxc ldap 10.10.76.174 -u users.txt  -p passwords.txt -k
```
- niesamowicie mi laguje... nie mam pojęcia czemu

![{3F28714C-DDE8-44EF-B410-07C8DCE2EA8B}](https://github.com/user-attachments/assets/db676467-ad3d-43e7-b1b7-ce1446f22df8)

Chyba godzinę później (musiałem zresetować maszynę aż, bo w połowie padło)

Skróciłem listę i tak.
tylko jeden user miał fail.
```
LDAPS       10.10.117.46    636    LUS2DC.Lustrous2.vl [-] Lustrous2.vl\Thomas.Myers:Lustrous2024 
```

![{C5F9A9AA-C871-4F0D-BA00-0C97B0C0810B}](https://github.com/user-attachments/assets/954d3cf4-15b4-4196-8fde-541883586b13)


