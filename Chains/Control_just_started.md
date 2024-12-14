# Control
Linux, Hard, created by **jkr**

![control_slide](https://github.com/user-attachments/assets/8f637798-e373-4b03-80e2-020092014368)

```
10.10.179.101
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

Nmap scan report for 10.10.179.102
Host is up (0.033s latency).
Not shown: 65530 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 05:0f:88:bf:a3:a3:b9:f1:d7:82:fc:b1:92:19:90:ab (ECDSA)
|_  256 0b:53:d6:5d:21:4a:64:1d:69:aa:bd:01:77:87:90:cc (ED25519)
80/tcp   open  http     nginx
|_http-title: Did not follow redirect to https://10.10.179.102/
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
10.10.179.102 os.control.vl
10.10.179.101 wiki.intra.control.vl
```

