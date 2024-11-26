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


