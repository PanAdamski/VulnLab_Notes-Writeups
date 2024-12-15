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

