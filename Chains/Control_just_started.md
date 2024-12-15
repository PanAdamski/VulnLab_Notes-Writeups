# Control
Linux, Hard, created by **jkr**

![control_slide](https://github.com/user-attachments/assets/8f637798-e373-4b03-80e2-020092014368)

```
10.10.197.21
22/tcp  open  ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 be:fa:cf:c3:c8:b1:50:11:f2:b0:73:b8:c5:ad:3d:0b (ECDSA)
|_  256 ef:4e:d4:7e:cc:dc:d6:90:91:d8:ed:1d:7b:88:07:b4 (ED25519)
443/tcp open  ssl/http nginx 1.25.0
|_http-generator: DokuWiki
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=wiki.intra.control.vl/organizationName=Belleville/countryName=CA
| Issuer: commonName=wiki.intra.control.vl/organizationName=Belleville/countryName=CA
| Public Key type: rsa
| Public Key bits: 4096
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2023-06-30T12:30:10
| Not valid after:  2033-06-27T12:30:10
| MD5:   2c4a:9dfc:9833:4207:77d2:8a87:647d:f2c8
|_SHA-1: 9b40:025f:f961:97d7:afd4:bce5:074c:bd07:a49b:ba4e
|_http-title: start [control.vl Intranet]
|_http-server-header: nginx/1.25.0
|_http-trane-info: Problem with XML parsing of /evox/about
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=12/14%OT=22%CT=1%CU=35965%PV=Y%DS=2%DC=T%G=Y%TM=675
OS:DD9D4%P=x86_64-pc-linux-gnu)SEQ(SP=100%GCD=2%ISR=105%TI=Z%CI=Z%II=I%TS=A
OS:)SEQ(SP=105%GCD=1%ISR=106%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=105%GCD=1%ISR=108%T
OS:I=Z%CI=Z%II=I%TS=A)OPS(O1=M4D4ST11NW7%O2=M4D4ST11NW7%O3=M4D4NNT11NW7%O4=
OS:M4D4ST11NW7%O5=M4D4ST11NW7%O6=M4D4ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4
OS:B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M4D4NNSNW7%CC=Y%Q=)T1(R=Y%
OS:DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A
OS:=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%D
OS:F=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O
OS:=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=
OS:G)IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 7.535 days (since Sat Dec  7 07:27:46 2024)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1723/tcp)
HOP RTT      ADDRESS
1   32.30 ms 10.8.0.1
2   32.40 ms 10.10.179.101

Nmap scan report for 10.10.197.22
Host is up (0.033s latency).
Not shown: 65530 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 05:0f:88:bf:a3:a3:b9:f1:d7:82:fc:b1:92:19:90:ab (ECDSA)
|_  256 0b:53:d6:5d:21:4a:64:1d:69:aa:bd:01:77:87:90:cc (ED25519)
80/tcp   open  http     nginx
|_http-title: Did not follow redirect to https://10.10.197.22/
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
443/tcp  open  ssl/http nginx
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=os.control.vl/organizationName=Belleville/countryName=CA
| Issuer: commonName=os.control.vl/organizationName=Belleville/countryName=CA
| Public Key type: rsa
| Public Key bits: 4096
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2023-06-30T16:21:40
| Not valid after:  2033-06-27T16:21:40
| MD5:   c117:d1c3:d34b:c96a:95d2:3697:5b99:f57c
|_SHA-1: 5d9d:7358:f8e8:6448:6287:75e8:31be:d3a4:fb2c:8c4c
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
8443/tcp open  ssl/http nginx
| http-methods: 
|_  Supported Methods: GET
| http-title: Login to osctrl
|_Requested resource was /login
| ssl-cert: Subject: commonName=os.control.vl/organizationName=Belleville/countryName=CA
| Issuer: commonName=os.control.vl/organizationName=Belleville/countryName=CA
| Public Key type: rsa
| Public Key bits: 4096
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2023-06-30T16:21:40
| Not valid after:  2033-06-27T16:21:40
| MD5:   c117:d1c3:d34b:c96a:95d2:3697:5b99:f57c
|_SHA-1: 5d9d:7358:f8e8:6448:6287:75e8:31be:d3a4:fb2c:8c4c
|_ssl-date: TLS randomness does not represent time
8444/tcp open  ssl/http nginx
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| ssl-cert: Subject: commonName=os.control.vl/organizationName=Belleville/countryName=CA
| Issuer: commonName=os.control.vl/organizationName=Belleville/countryName=CA
| Public Key type: rsa
| Public Key bits: 4096
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2023-06-30T16:21:40
| Not valid after:  2033-06-27T16:21:40
| MD5:   c117:d1c3:d34b:c96a:95d2:3697:5b99:f57c
|_SHA-1: 5d9d:7358:f8e8:6448:6287:75e8:31be:d3a4:fb2c:8c4c
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
|_ssl-date: TLS randomness does not represent time
```

so we have some domains/subdomains
```
10.10.197.22 os.control.vl
10.10.197.21 wiki.intra.control.vl
```

```
ffuf -u https://os.control.vl/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.control.vl" -c -mc all -fs 4
ffuf -u https://wiki.intra.control.vl/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.intra.control.vl" -c -mc all  -fw 1842
ffuf -u https://wiki.intra.control.vl/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.control.vl" -c -mc all -fw 1842
ffuf -u https://os.control.vl:8443/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.control.vl" -c -mc all -fs 29

```
- nothing more

clasic time:
```
ffuf -w ~/raft.txt -u https://os.control.vl/FUZZ -c -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36' -mc all -fs 19,0,4

error                   [Status: 500, Size: 8, Words: 2, Lines: 1, Duration: 33ms]
health                  [Status: 200, Size: 3, Words: 1, Lines: 1, Duration: 31ms]
```

![{E037DD20-6707-40C2-B834-14E1B522E7AF}](https://github.com/user-attachments/assets/aa1a299f-b885-43ce-a8cc-0cd0a1425d8b)

![{E6009601-680F-445A-87D8-CAFBF8425F90}](https://github.com/user-attachments/assets/65a2ef4b-2d64-4c36-80ad-f15c247bd9d4)

![{E7A7B0D3-D33E-438A-8751-B0FD11728D76}](https://github.com/user-attachments/assets/0a0d6091-62e9-4b99-a0cb-471439c3768a)

```
ffuf -u https://cells.intra.control.vl/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.control.vl" -c -mc all -fw 1842
```

![{A33EF1FC-E703-4AA5-BE8B-5E4BDD45DF6C}](https://github.com/user-attachments/assets/0c6dfc45-9d00-473b-b435-40c69dd9cd50)

I tried a lot of combination for `Jimmy George's` user but I doesn't work.

![{7F61A056-254E-4549-BF8C-671DB08D3E3D}](https://github.com/user-attachments/assets/6a0e232d-98ab-421f-ba22-16088c1cf7db)

och maybe it is `a.larose` or other but we know format now.

![{25B3D854-4B6F-4AB0-A949-8C611C9412B2}](https://github.com/user-attachments/assets/b51fe7e8-b15b-4560-874d-794a6a7d7a4b)

sprawdzając historięmzian widizmy kilka usernameów.

![{D2B614A7-D00C-4C93-99EC-4736F849AABE}](https://github.com/user-attachments/assets/d43464bb-5e8a-4910-bcc4-482c5b51bfce)

I works for `k.dagenais`.

![{061163E8-333F-4789-9FED-5DCEAB7CEBB9}](https://github.com/user-attachments/assets/9834f31f-2e34-4de6-8c76-5350c9a870d5)

- generalnie zakładam, że trzeba tutaj utworzyć cell (cell'a/cell'e? ach ten makaronizm.. nie wychodzi zawsze) i z tego RCE machnąć. Raczej nie obstawiam czytania innych cell'i.

![{3A63BC74-E67C-460B-8341-3E291115AA7B}](https://github.com/user-attachments/assets/545c613f-2aba-4493-80df-02a8206f8094)

o nawet nie muszę od zera kombinmować. Nice.

It looks nice. [https://github.com/xcr-19/CVE-2023-32749](https://github.com/xcr-19/CVE-2023-32749)

![{B4A7E10D-3804-4544-8B6E-C64DFEBE3A18}](https://github.com/user-attachments/assets/a09ff6d1-1e75-4761-8490-1460d1edccd7)

wygląda jakby podziałało.

![{0C761423-89B6-4D32-9BC9-6E91AFE24E83}](https://github.com/user-attachments/assets/25800835-cc22-40f4-974c-7aea43df28a4)

![{4001BE20-C18C-4507-B72B-4872571C84C0}](https://github.com/user-attachments/assets/306369a4-34a5-46e7-a95d-4d31f6906eba)

![{A0748093-5D52-4780-A08C-A5961849AE92}](https://github.com/user-attachments/assets/84c56460-71a7-493a-97ca-6916f39153e3)

o have found some password

![{A6D14FF4-3854-4390-A11E-C766FE659B37}](https://github.com/user-attachments/assets/7433cf9f-78bb-400f-99b5-8eac5a9cf4f0)

okey. first flag

Tak generalnie zdziwiło mnie trochę to, że mmay uid666 i lekką enumerację robię. Dalej screeny bez celu.

![{CF9EB5EC-03D2-41F9-9F1B-F78ED8E023D9}](https://github.com/user-attachments/assets/d65cc391-1cfc-41e3-931b-e25bc75a4910)

![{8621BDA0-96D9-4557-AAB2-38493DE47FFD}](https://github.com/user-attachments/assets/1dbf7fd8-d0cb-4ff5-bd54-2dccf539221a)

![{CA0071B7-6E76-439B-BF0A-90E8AA9E3717}](https://github.com/user-attachments/assets/de4a9995-4d55-41d4-aebb-6c3e60fe6876)

szczerze nie wiem co robić xD

![{975A50C0-AD3C-4789-A2CC-D2C2AD7EB2B4}](https://github.com/user-attachments/assets/8cbad910-aac7-4d28-a5f4-87ed45c97518)

chyba możemy sobie dowolne JWT wygeenrować, ale.. i tak mamy exploit do tworzenia konta z max uprawnieniami więc chyba usless.

![{BC72BC4A-7C7B-4B5A-B407-6F8D57D15F7D}](https://github.com/user-attachments/assets/150dd82c-4572-4c87-b969-4cd746ea9634)

hasełko czy tam dwa

aaaa moment. Te redisy czy inne to są chyba na tej domence gdzie nic nie mamy. To chyba dobry trop :D
to lecimy. z `db.json` wiemy, że bazadanych jest na 5432 więc.. postgres jakby nie patrzeć.

![{D20FDAB2-7588-41DC-B426-53ADC8E912C1}](https://github.com/user-attachments/assets/2cb8fd40-071b-4f10-95c6-e191c7e05dfe)

o podziałało bez hasła wgl. TO szukamy czegoś
```
select * from admin_users;
```

![{3B376D91-1314-4C4B-937E-03EF6320514C}](https://github.com/user-attachments/assets/3a165de0-2eee-4836-a4a9-f611af26ccc8)

- łamałem 10 minut na RTX3070Ti i nie złamało się więc uznaję, że to nie o to chodzi w zadaniu.
- zatem zmienimy hasło po prostu

![{5FE0D8F4-3B6F-4770-91CE-224E07833AB8}](https://github.com/user-attachments/assets/09299e85-2331-4d4c-97cf-1ffa594e6a4f)

dobra zmieniło

![{41DEF001-9514-4A8C-B045-EFB1A1800B6C}](https://github.com/user-attachments/assets/e6df0cb6-8fe9-433c-ba5d-a6b72b4d3047)

![{291CDEE4-EEDD-499B-8AB2-CE6B4E69E783}](https://github.com/user-attachments/assets/7bfa901d-8b1c-40aa-96d8-901181e5d28c)

![{1C89B187-6CA8-4984-A73F-C2F656D3B497}](https://github.com/user-attachments/assets/92196f81-81fe-4519-aa30-33ed597a954d)

![{9B2DA7EC-0984-4672-A3BB-11A1D0F1E1C0}](https://github.com/user-attachments/assets/eec24e8d-379c-44fc-a192-dc837f4ed3fb)

no i mamy dostęp.

![{F9545C87-EC9E-45E6-BFCE-2C7AC4F7D9B0}](https://github.com/user-attachments/assets/6b2409de-96f5-46b8-8a35-4f4683a0c60e)


![{2FF34733-4E62-4EB2-888A-A150DCFB7027}](https://github.com/user-attachments/assets/0379627a-c66c-4d41-b3ca-b552779721d6)

jakieś query wykonuję sobie.

nie mam pojęcia co robię. Po prostu klikam.
W między czasie zalałem drugi sposób na zostanie adminem :D

![{B8025520-FFBA-4549-A813-A3D245D0CFFE}](https://github.com/user-attachments/assets/232a9757-ae10-4e68-9c3f-c314a7ef9cf3)

![{9879E031-D45E-4E92-BA6B-8F5D7AB2C494}](https://github.com/user-attachments/assets/8f553c91-ee89-44d0-ae02-4c26f91e7bbf)

![{E9EDA8C9-9509-4223-95FC-C3E2B7B973F0}](https://github.com/user-attachments/assets/91ccb257-ea14-48a0-89f9-523375fea5c1)

![{BA9E3727-2919-4A71-BFEC-B8D89AB6FF92}](https://github.com/user-attachments/assets/5ecb8682-4869-47c3-aab8-d6e1e7ddf4af)


dobra coś mamy. Teraz pewnie klucz prywaty roota albo usera.

![{58394931-75BD-4FEF-9028-0A876D24101C}](https://github.com/user-attachments/assets/322b35d5-097c-4a8c-9731-e2b0dc5f8d2b)

![{A5AF0251-8DED-4B0B-B293-77EECE066BF8}](https://github.com/user-attachments/assets/bf3db597-f252-4a9c-b451-bf833dd5470a)

kliknąłem i czekam

![{DAF47716-A144-4F6F-91A5-6EE7CECC1484}](https://github.com/user-attachments/assets/92dc55a3-856f-4194-b593-4b24cf59043e)

![{B816B70B-735E-4589-96FE-670641C736CD}](https://github.com/user-attachments/assets/12ac076b-a7bc-4353-af07-68c9e603007c)

![id](https://github.com/user-attachments/assets/7fd1f9b7-9320-4362-b571-5ea32f69ce69)

![{269248E8-DF09-4DC7-A0D1-9FC1FD0A0B44}](https://github.com/user-attachments/assets/d6414cf5-d455-460e-b3ff-6d2871589846)

yeeee

![{41303F29-D45A-4342-8DB0-1B479B27FBDB}](https://github.com/user-attachments/assets/c2d08d32-416a-446f-87b0-767eb4cf08e0)

o szybko poszło xD

![{3A5DE78B-849E-470E-92B9-BA3D5B145115}](https://github.com/user-attachments/assets/63149dd7-30ee-48bf-a902-b136ce8df147)

![{E581BCA8-CCD0-4DC3-96DD-FBC57E6CA276}](https://github.com/user-attachments/assets/bc653048-e57a-4d4a-bce1-c0ba43adf17f)

został root na `intra.control.vl`.
Wracamy do naszego carve files gdzie pobierałem /etc/passwd. Tym razem sprawdzimy drugiego hosta.

![{2B2C7944-B53B-4CD4-B77D-FA77285033BC}](https://github.com/user-attachments/assets/35453cb2-8e81-405c-8cc5-a648c2a58039)

![{15CA0B7E-FA87-47FB-A093-1D0ACA228D82}](https://github.com/user-attachments/assets/9df47ae0-e798-4072-938a-34f6aeeda4f5)

tym razem user to steven.

![{9A76EB41-B05C-4999-816D-84EB183A2FBA}](https://github.com/user-attachments/assets/d4a1a80c-e21d-4157-ac1d-20a9091f1d53)

próbujemy.

![{CDEF52AE-9127-479A-BE26-AE7752ABF028}](https://github.com/user-attachments/assets/5618dbbf-11eb-4a45-8113-4ca4bdb4b578)

file does not exist :/
- trochę takich natrafiłem nieistniejących.

![{CD2D0AE7-20FD-4F8D-82E7-67217773F2E5}](https://github.com/user-attachments/assets/8da8ffd2-ed6b-417b-a07c-168a68d121f3)

ech zmęczenie widzę działa... xD
ALE KOŃCU COŚ SIĘ POKAZAŁO (i turbo podobne do tego wyżej ech)

![{C98492B3-7294-4667-89A5-568BFD89D866}](https://github.com/user-attachments/assets/3d9655d2-0b9a-44e2-a6ac-870a3bcea598)

zatem czas na `/opt/provision/provision.sh`

![{80B6214D-E55D-4F8B-B753-4AEA21396AE3}](https://github.com/user-attachments/assets/36f0765c-f853-4052-9543-dd7e29202959)

Tak w duuuuzym skrócie to skrypt tworzy ograniczone środowisko uruchamiania poleceń zdalnie za pośrednictwem SSH, pozwalając jedynie na wykonanie określonych "modułów" dostępnych w wyznaczonym katalogu.

Dobra zobaczmy zatem co tam siedzi. Możemy użyć małej sztuczki (mam nadzieję) czyli wpisać query `select path from file where path LIKE '/opt/provision/modules/%%';`

![{8F3248A9-DCD5-4734-B900-1857B1AFE2AA}](https://github.com/user-attachments/assets/fe3ad01b-1cc2-4ccc-a6f8-63a58b57041e)

![{ABB20851-818F-4803-AA1D-3300B4CD1C80}](https://github.com/user-attachments/assets/37202efc-4413-41f5-949b-c503f30c42c6)

mamy 3 pliczki.
```
/opt/provision/modules/prov_df
/opt/provision/modules/prov_osqd
/opt/provision/modules/prov_uname
```

![{F84E381B-57DB-45DF-8DE4-9B7E22DFE29B}](https://github.com/user-attachments/assets/a13ac36f-b670-49ef-b58b-2b66a43d5361)

pierwszy elf

![{74051486-8313-4C7C-BCED-51B75BEBA892}](https://github.com/user-attachments/assets/cb3a99d5-110e-49b3-964f-52646b6a4872)

drugi bash

![{4B8D765D-B611-4A03-94C5-4CF0C88BA8E5}](https://github.com/user-attachments/assets/8bcb5397-05ae-4b4a-b6bf-66d374653824)

trzeci elf.

