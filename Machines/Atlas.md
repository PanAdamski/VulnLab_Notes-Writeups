# Atlas
Windows, Hard, created by **sec77**

```
21/tcp   open  ftp           FileZilla ftpd 1.7.2
22/tcp   open  ssh           OpenSSH for_Windows_8.1 (protocol 2.0)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
8080/tcp open  http          Apache Tomcat (language: en)
```

Anonymous FTP access gave as some files


![{398CE59A-F067-42A9-A797-FF2D2E9DB759}](https://github.com/user-attachments/assets/1a66ccba-4435-49a1-924f-e77fdeccc813)

![{2C6F21E0-C1A8-453D-AA9A-F6EDC10C8728}](https://github.com/user-attachments/assets/0c68af88-64a5-4489-bbf6-19b9c20c6191)

We are starting with decompling file and check for interestign staff.

![{9289EB11-D621-4E93-91B9-E390DEA59E91}](https://github.com/user-attachments/assets/a12b2481-7b1c-49f7-96de-0b4a60b38eea)

I will put here some interesting parts.

![{CA96665D-FCF3-4C1B-BEC2-9F04D553E63A}](https://github.com/user-attachments/assets/0a376b67-0f6c-4e97-9e9f-b5481a6ef6ea)

![{E01CF072-62E8-4CA1-B6D0-106EA0576D69}](https://github.com/user-attachments/assets/8c9e9d24-fde9-435c-a504-752081ff9481)

![{A5B010EE-C20D-439C-8949-4BB1C8F276BF}](https://github.com/user-attachments/assets/a0aa147f-8571-4978-ab33-91d283614117)

Jesteśmy pewni, że coś się dzieje z plikami xml. Wiemy o dwóch plikach `employee_template.xml` oraz `mapping.xml`. And now.. Time for AI. I hate JAVA.

Or.. do it blind. We are sure this is some parsing, some java and... vulnerable machine. So let's try it without understanding a code (yeah I know this is stupid).

Start with
```
git clone https://github.com/mbechler/marshalsec
sudo apt update
sudo apt install maven -y
mvn clean package -DskipTests # (this take a while)
```


