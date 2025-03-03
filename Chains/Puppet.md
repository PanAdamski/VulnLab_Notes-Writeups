# Puppet
Windows, Medium, xct

```
10.10.139.37
10.10.139.38
10.10.139.39
```

only `10.10.139.39` has usfull open ports. 
```
21/tcp    open  ftp            vsftpd 3.0.5
22/tcp    open  ssh            OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
8140/tcp  open  ssl/http       WEBrick httpd 1.7.0 (Ruby 3.0.2 (2021-07-07); OpenSSL 3.0.2)
8443/tcp  open  ssl/https-alt?
31337/tcp open  ssl/Elite?
```

10.10.139.38 - File01.puppet.vl
```
3389/tcp open  ms-wbt-server Microsoft Terminal Services
```

10.10.139.37 - DC01.puppet.vl
```
3389/tcp open  ms-wbt-server Microsoft Terminal Services
```

![{444455A9-A503-49B9-A2DA-229ED810F68A}](https://github.com/user-attachments/assets/f7b81256-537c-49b7-b8a2-126647f1de10)

nla:true x2

anonymous ftp access

![{1F203B69-4246-4E4C-B539-5AA23BEA783F}](https://github.com/user-attachments/assets/6798f4b8-d59b-4f92-8528-5ca6a448bca0)

![{B413F07A-A561-444F-B125-00A09A8E0E0D}](https://github.com/user-attachments/assets/332652e6-1f5a-4d1f-9e0b-f6249514bd3c)

![{31470D5A-CF0A-4829-8185-9AF95422B9FF}](https://github.com/user-attachments/assets/23c11a9c-a737-4f99-8d67-5e8510bc6839)

btw some curiosity. How to dump certyfikate from json form

![{F4FD4747-2712-4E84-A696-04ACFF1796E9}](https://github.com/user-attachments/assets/767b351f-0e54-4a1b-ad83-126ed53df366)

lets try something with this sliver.

1st redirect the local host to the host from which we downloaded this binary
```
sudo socat TCP-LISTEN:31337,reuseaddr,fork TCP:10.10.139.39:31337
```

![image](https://github.com/user-attachments/assets/368dc10b-0dce-416c-bb73-07f66a9f0bfd)

we got some interesting informations.
```
use ccfa3216
interactive
<some random commands>
```

![{8FD3D819-757C-4106-809C-BED8157ED193}](https://github.com/user-attachments/assets/53946193-e8ec-4b48-99f5-94d5888073e3)







