# Trusted
Windows, Easy, created by **r0BIT**


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



