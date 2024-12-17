# Mythical
Windows, Medium, created by **xct**

![lustrous_slide](https://github.com/user-attachments/assets/66e44d52-5012-43c7-a16b-63f931203195)

![{40E32462-459A-46DD-8D59-4B4C8C63B9F3}](https://github.com/user-attachments/assets/1f90b165-4e4c-41e2-84a6-5678e156c133)


![{556D61AB-437C-426F-8F12-0495E35B320E}](https://github.com/user-attachments/assets/2662ef07-7d16-474d-93ba-f6835b62a277)

```
10.10.194.5
53/udp  open  domain       Simple DNS Plus (generic dns response: NOTIMP)
88/udp  open  kerberos-sec Microsoft Windows Kerberos (server time: 2024-12-17 13:50:09Z)
123/udp open  ntp          NTP v3
137/udp open  netbios-ns   Microsoft Windows netbios-ns (Domain controller: MYTHICAL-US)

10.10.194.6
68/udp    open|filtered dhcpc
996/udp   open|filtered vsinet
65024/udp open|filtered unknown

10.10.194.7
53/udp  open  domain       Simple DNS Plus
88/udp  open  kerberos-sec Microsoft Windows Kerberos (server time: 2024-12-17 13:50:08Z)
123/udp open  ntp          NTP v3
```

w międzyczasie zdjążyłem zmienić IP, bo nie miałem czasu
```
10.10.185.37
3389/tcp open  ms-wbt-server Microsoft Terminal Services

10.10.185.38
22/tcp   open  ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     NetDNA-cache/2.2
7443/tcp open  ssl/http nginx 1.25.5


10.10.185.39
3389/tcp open  ms-wbt-server Microsoft Terminal Services
```

no cóż. Wygląda na to, że mamy jednego hosta do dyspozycji :D
(na host z 3389 psrawdziłem sec-nla)

```
ffuf -w ~/raft.txt -u https://10.10.185.38:7443/FUZZ -c -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36' -mc all -t 100 -k -fs 18
ffuf -w ~/raft.txt -u http://10.10.185.38/FUZZ -c -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36' -mc all -t 100 -fs 0
```



