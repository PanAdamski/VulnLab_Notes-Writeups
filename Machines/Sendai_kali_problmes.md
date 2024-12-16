# Sendai
Windows, Medium, created by **xct**

![sendai_slide](https://github.com/user-attachments/assets/e40d25e9-96d8-497d-b23e-656c808f4f56)

```
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-12-16 13:18:40Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: sendai.vl0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: sendai.vl0., Site: Default-First-Site-Name)
3269/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sendai.vl0., Site: Default-First-Site-Name)
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2024-12-16T13:20:26+00:00; +2s from scanner time.
| ssl-cert: Subject: commonName=dc.sendai.vl
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49670/tcp open  msrpc         Microsoft Windows RPC
50534/tcp open  msrpc         Microsoft Windows RPC
50556/tcp open  msrpc         Microsoft Windows RPC
50569/tcp open  msrpc         Microsoft Windows RPC
50593/tcp open  msrpc         Microsoft Windows RPC
64006/tcp open  msrpc         Microsoft Windows RPC

53/udp  open  domain       (generic dns response: NOTIMP)
88/udp  open  kerberos-sec Microsoft Windows Kerberos (server time: 2024-12-16 13:08:38Z)
123/udp open  ntp          NTP v3
```

![{018BBB9B-F355-4B24-BB5A-35C8EA99F45E}](https://github.com/user-attachments/assets/94694495-2372-41d9-84b2-5a22eb5f2167)

ldap nic

content discovery coś tam
```
Aspnet_Client
Service
iisstart.htm
```

guest może kilkashare'ów zobaczyć oraz --rid enumerować.

![{0DF3B9B5-6038-4048-A8E7-630EA7345E9A}](https://github.com/user-attachments/assets/cd15dd56-0266-4f0d-909a-6c0c3cddedfe)

![{1C8681F8-FD18-485E-8AA7-5FE60ABB5D7A}](https://github.com/user-attachments/assets/d611944a-8898-49b7-acfa-f5919f99abf4)

ech wypada pogrzebać.

![{F9236A22-9938-476A-88BA-D1820F7E0938}](https://github.com/user-attachments/assets/5f9b7d6d-3705-468c-99e1-4464825a750b)

![{72988D48-59DF-4DB6-8B46-F759F49A075B}](https://github.com/user-attachments/assets/9bbad635-44e5-4b5a-970a-a1afa839a6ea)

```
└─$ cat incident.txt 
Dear valued employees,

We hope this message finds you well. We would like to inform you about an important security update regarding user account passwords. Recently, we conducted a thorough penetration test, which revealed that a significant number of user accounts have weak and insecure passwords.

To address this concern and maintain the highest level of security within our organization, the IT department has taken immediate action. All user accounts with insecure passwords have been expired as a precautionary measure. This means that affected users will be required to change their passwords upon their next login.

We kindly request all impacted users to follow the password reset process promptly to ensure the security and integrity of our systems. Please bear in mind that strong passwords play a crucial role in safeguarding sensitive information and protecting our network from potential threats.

If you need assistance or have any questions regarding the password reset procedure, please don't hesitate to reach out to the IT support team. They will be more than happy to guide you through the process and provide any necessary support.

Thank you for your cooperation and commitment to maintaining a secure environment for all of us. Your vigilance and adherence to robust security practices contribute significantly to our collective safety.  
```
cat security/guidelines.txt
```
Company: Sendai
User Behavior Guidelines

Effective Date: [Insert Date]
Version: 1.0

Table of Contents:

Introduction

General Guidelines

Security Guidelines

Internet and Email Usage Guidelines

Data Management Guidelines

Software Usage Guidelines

Hardware Usage Guidelines

Conclusion

Introduction:

These User Behavior Guidelines are established to ensure the efficient and secure use of information technology resources within Sendai. By adhering to these guidelines, users can contribute to maintaining a productive and secure IT environment. It is the responsibility of every employee to read, understand, and follow these guidelines.

General Guidelines:
2.1. Password Security:
a. Users must choose strong passwords that are difficult to guess.
b. Passwords should be changed regularly and not shared with others.
c. Users should never write down their passwords or store them in easily accessible locations.

2.2. User Accounts:
a. Users must not share their user accounts with others.
b. Each user is responsible for any activities carried out using their account.

2.3. Reporting Incidents:
a. Users must promptly report any suspected security incidents or unauthorized access to the IT department.
b. Users should report any IT-related issues to the IT support team for resolution.

2.4. Physical Security:
a. Users should not leave their workstations unlocked and unattended.
b. Confidential information and sensitive documents should be stored securely.

Security Guidelines:
3.1. Malicious Software:
a. Users must not download or install unauthorized software on company devices.
b. Users should regularly update their devices with the latest security patches and antivirus software.

3.2. Social Engineering:
a. Users should be cautious of phishing emails, phone calls, or messages.
b. Users must not share sensitive information or credentials through untrusted channels.

3.3. Data Backup:
a. Users should regularly back up their important files and data.
b. Critical data should be stored on secure network drives or cloud storage.

Internet and Email Usage Guidelines:
4.1. Acceptable Use:
a. Internet and email usage should be for work-related purposes.
b. Users must not access or download inappropriate or unauthorized content.

4.2. Email Etiquette:
a. Users should maintain professionalism in all email communications.
b. Users should avoid forwarding chain emails or unauthorized attachments.

4.3. Email Security:
a. Users should exercise caution when opening email attachments or clicking on links from unknown sources.
b. Confidential information must not be sent via unencrypted email.

Data Management Guidelines:
5.1. Data Classification:
a. Users must classify data according to its sensitivity level.
b. Users should handle and store sensitive data in accordance with the company's data protection policies.

5.2. Data Privacy:
a. Users must respect the privacy of personal and sensitive information.
b. Unauthorized disclosure or sharing of personal data is strictly prohibited.

Software Usage Guidelines:
6.1. Authorized Software:
a. Users must only use authorized software and adhere to licensing agreements.
b. Users should not install or use unauthorized or pirated software.

6.2. Software Updates:
a. Users should regularly update their software to benefit from the latest features and security patches.
b. Automatic updates should be enabled whenever possible.

Hardware Usage Guidelines:
7.1. Equipment Care:
a. Users should handle company hardware with care and report any damages or malfunctions promptly.
b. Users must not attempt to repair or modify company equipment without proper authorization.

7.2. Personal Devices:
a. Users should not connect personal devices to the company network without prior approval from the IT department.
b. Personal devices used for work purposes must comply with company security policies.

Conclusion:
By following these User Behavior Guidelines, Sendai employees contribute to the overall security, productivity, and effectiveness of the company's IT infrastructure. Users should regularly review these guidelines and seek clarification from the IT department whenever necessary.

Failure to comply with these guidelines may result in disciplinary action, including the suspension of IT privileges or other appropriate measures.

For any questions or concerns regarding these guidelines, please contact the IT department at [Contact Information].
```

dobra wróćmy jeszcze może

![{BBC43F39-0718-4955-9773-A17000F1EAFC}](https://github.com/user-attachments/assets/db200dca-c4f7-44ad-a270-00706e92f123)

brak

![{E4623895-F228-405B-9C3D-E9EF09D03E05}](https://github.com/user-attachments/assets/34cdbb8b-8ef1-4de2-b4c6-8b91c02afbc7)

i w końcu coś.
```
Elliot.Yates
Thomas.Powell
```


