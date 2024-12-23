# Unintended 
Linux, Medium, created by **kavigihan**

```
10.10.129.101
10.10.129.102
10.10.129.103
```

```
PORT      STATE SERVICE      VERSION
22/tcp    open  ssh          OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
53/tcp    open  domain       (generic dns response: NOTIMP)
88/tcp    open  kerberos-sec (server time: 2024-04-25 17:54:13Z)
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Samba smbd 4.6.2
389/tcp   open  ldap         (Anonymous bind OK)
445/tcp   open  netbios-ssn  Samba smbd 4.6.2
464/tcp   open  kpasswd5?
636/tcp   open  ssl/ldap     (Anonymous bind OK)
3268/tcp  open  ldap         (Anonymous bind OK)
3269/tcp  open  ssl/ldap     (Anonymous bind OK)
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC


22/tcp   open  ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
80/tcp   open  ssl/http Werkzeug/3.0.1 Python/3.11.8
8200/tcp open  http     Duplicati httpserver


21/tcp open  ftp     pyftpdlib 1.5.7
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
```

ports shows as domain+subdomain

![{55525783-2357-494E-90A3-3C70FBB62648}](https://github.com/user-attachments/assets/a417773e-69aa-45e6-956b-1c4607ebe43a)

![{3C3D308F-88CD-4337-B530-E7876D00E14D}](https://github.com/user-attachments/assets/6374a3fe-bd60-41ce-999f-4a9ba6fb3dca)

o i mamy dwie subdomenki dodatkowo.

![{EF9D76A1-7DE2-4A65-87D4-179C951961EA}](https://github.com/user-attachments/assets/3406ef65-7d74-477e-8752-418e90541770)

I found gitea and some commits

![{C62A5609-C641-494C-B28C-0915CB20DE61}](https://github.com/user-attachments/assets/5e0151c7-710e-4a2b-b568-a77e73546f96)

![{C26D7A2E-B44F-4E9C-A064-2FC1FB7F912C}](https://github.com/user-attachments/assets/41e1dd48-33cf-4ec9-881a-4f1a8b4c7c54)

oooo

![{80DC0829-9754-4A80-8685-657D04C660B7}](https://github.com/user-attachments/assets/8a53d6de-9aed-4b0d-acfc-01f5aa365eca)

mamy dwa usernamy
```
ratul
nanee
```

![{FBD21D94-853D-47DE-A0A1-06CEF11C64A1}](https://github.com/user-attachments/assets/b922d524-471b-46a3-a9a7-7a686b88fad0)

o i hasełko do mysqla

![{B4A078D3-B0D6-4434-90C7-ED2B53B9D45A}](https://github.com/user-attachments/assets/d86c434b-7d2d-4aa0-8fc0-bd380f7a66ec)

![{6F3513E4-12B3-41D3-ADC7-CE7FA20821B8}](https://github.com/user-attachments/assets/a223974a-4e7e-40cc-b69a-1190ba00b99f)

jezu ile tego się zrobiło

![{F8F484C8-6A09-41B1-872F-0212EE1954DB}](https://github.com/user-attachments/assets/cfdf0367-52c2-4d45-a82a-79c56b65685e)

![{DF219167-3855-4399-A8BA-06546587B4E2}](https://github.com/user-attachments/assets/4fb9c733-d3fb-48b0-a6ce-1c364d4a371e)

creds works from 2nd host. We can't login but I think pivoting i available.

![{80F73198-4969-43B0-8E89-D5A0FA44A9FA}](https://github.com/user-attachments/assets/6aa70951-66c8-47bb-ade7-9af3d318ce6c)

Fast check for new ports running localy.
```
proxychains4 -q nmap -Pn -v 10.10.129.101 10.10.129.102 10.10.129.103 -p- -T4
```
Ale tak na logikę to tam powinno lokalnie mysql siedzieć.

![{2845988A-B052-4019-92C5-A3B69369FFB7}](https://github.com/user-attachments/assets/854c384d-c0b9-4f56-8c88-cb929cc6ce23)

NIE ROZUMIEM czemu nmap nie pokazuje mi otwartego 3306, a łączę się tam

![{0533AC8E-4D1B-488D-B558-43463CBC8F2F}](https://github.com/user-attachments/assets/917b3fe1-c7ef-4481-b872-2876d61028a7)

we have two hashes.

![{D1BCA209-29CE-4F7D-AD67-69D4D8EE10AD}](https://github.com/user-attachments/assets/d7c7ad14-8bcb-44f4-b65f-9a2c27ce2afb)

mamy też jakieś prywatne repo.


![{DE5ED2DD-3322-41C9-87BD-3D47FCE946FA}](https://github.com/user-attachments/assets/e9d2a637-b25f-4a52-adf6-6fdfd2ea8d92)

![{70F92C6C-C219-49CB-BB91-F087892041FB}](https://github.com/user-attachments/assets/e13b978a-9567-47be-9424-4b8393ceb69c)


widzimy drugie repo od razu

![{6A957D28-F679-492E-B0AB-7A628C7C0A11}](https://github.com/user-attachments/assets/8bfbb572-f568-4172-a16c-5db08a2e145f)

![{B2DDFDEC-3C9B-4B7F-A2C5-3E2AA7F0215E}](https://github.com/user-attachments/assets/6edbbfb8-6667-413b-b8b7-dfb002807eb5)

![{BC3A774B-3721-4DE4-8204-AEDEFDD7434F}](https://github.com/user-attachments/assets/5aeae477-7fc4-4b0b-9604-e65d83c0c447)


![{2B9896C8-1F5A-4725-9BB1-67A62C55F61A}](https://github.com/user-attachments/assets/91e2e4b9-ae72-4a40-9fbf-825e4d7702bf)

miałem nadzieję, że jeszcze gdzieś wejdzie, ale nie udalo się

![{C49D3BBC-4BB0-43A6-B68F-85CE7A99E1F1}](https://github.com/user-attachments/assets/b2508eca-e25a-4ce8-9253-26497e65f725)

o jeszcze tak spróbowałem i weszło. Nice

![{5D472F65-BFBE-4AE6-A39B-6AEC650739F1}](https://github.com/user-attachments/assets/eaeea655-9256-4356-a622-80e7c28b0873)

ooo pierwsza flaga.

![{6F23BAB2-1944-4459-8866-C9FBD3E8D15B}](https://github.com/user-attachments/assets/42283634-28fd-40df-880d-d4ad36cd4e2f)

wstępnie nic ciekawego u innych userów.

![{B9979DEE-0810-48A3-B445-5C9E056BF54E}](https://github.com/user-attachments/assets/04445f92-6eb2-4981-acdf-d5cb4dcc6895)

o jednak klasyka nie weszła

Chwilkę błądziłęm, ale ogarnąłem, że da się zalogować do chata usernamem `uan@unintended.vl`

![{2414CDD5-C0FF-4ACD-961E-481AA8F7791D}](https://github.com/user-attachments/assets/a9fe4e12-554b-44b7-bf08-24d2ed28e636)

![{078BB8D2-20FC-40B5-A20C-0509BBECBB9A}](https://github.com/user-attachments/assets/8889e123-3145-4f2f-9cdf-cb2383064009)

dobra to w sumie szybki bruteforce powinien być.

![{6249FA55-C772-45E4-B664-EB318815DBB5}](https://github.com/user-attachments/assets/4cf885e0-c7b5-44dd-a1a8-9340cf4094bc)

![{20687F96-D54C-4DED-B7BC-52889DB3333C}](https://github.com/user-attachments/assets/c18e5d64-72c4-4856-b544-bc5db5de072e)

![{D9DE04D3-92E9-40AC-A3F0-B901F60FAAA8}](https://github.com/user-attachments/assets/e3cbd979-2ef0-4171-80f5-b688e0d5f7e6)

yeee

![{4BA2CC69-E8F8-4D17-B62E-B1A5447FF0C4}](https://github.com/user-attachments/assets/8ccbe41e-c533-41cc-b86d-22b9c24ca3a9)

jakieś hasełko mamy.
- nawet działa :D

![{28FCFB24-1FC4-41DE-BD50-CE4C5D1657B7}](https://github.com/user-attachments/assets/3b50d3e0-3c22-4551-8860-24f4c61668b6)

grupa docker? No to sekalacja od ręki.

![{9306FE97-545E-4212-94A6-5E6C076D33C7}](https://github.com/user-attachments/assets/379a7197-58c5-40c0-8549-8d2126b7d3e4)

![{1C76F01D-FB22-410A-BA96-75BE612B4634}](https://github.com/user-attachments/assets/623522ac-62d0-419a-b9c9-cc1fe65ab2ec)

![{2BCB699D-14C0-4EC4-849B-D6385F1117B3}](https://github.com/user-attachments/assets/2fe85b4b-3255-4a82-81af-ee86ce2ea6a6)

server.py contain new password.

fast escalation and go next

![{558BFEA1-71A6-4671-B3AB-CD85B89D4BE7}](https://github.com/user-attachments/assets/985efc13-0ce5-4b17-91af-fd746b8a0a54)

![{97CFF9EF-4445-4374-B05D-5A5963AA0689}](https://github.com/user-attachments/assets/f0d7dc12-7316-46c2-a2bc-bca77bdd1080)

nasz nowy user ma dostęp do ciekawych rzeczy.
- dump and extract

![{137AA45F-C165-46E5-B365-D3762F19CBC8}](https://github.com/user-attachments/assets/005adb94-865e-4624-9be0-b64920c8181a)

tutaj musiałem trochę doczytać. SAM.ldb może być ciekawy z tego zrozumiałem

![{C40F40BE-E48D-4B42-9C6F-F9A4FCE0415D}](https://github.com/user-attachments/assets/0a34796f-6c9a-40ec-a125-5ac0645c135e)

`https://wiki.samba.org/index.php/LDB` tutaj znalazłem ciekawe toole.

![{9322D699-CD74-41C3-8426-78EA1CC7FDCD}](https://github.com/user-attachments/assets/fecd7496-661d-4d29-90c6-5be1e4bf9018)

i oczywiście u mnie musi nie działać.


coś mi nie działają toole :/
- właśnie widzę, że -H to połączenie do URL, a ludzie robili normalnie tym toole z takimi switachami... ech (btw celujemy w `unicodePwd`)

https://samba.tranquil.it/doc/en/samba_fundamentals/about_password_hash.html
- 30 minut zabawy, ale trzeba było doinstalować `samba-dsdb-modules`. Pełna komenda wszystkiego co potrzebowałem
```
sudo apt-get install samba-dsdb-modules python3-ldb python3-samba ldb-tools
```

![{6B93B602-47BC-48B8-AD93-C9BD067C2676}](https://github.com/user-attachments/assets/cb20828f-a63e-4ec2-8cd0-9133856ac02c)

![{8C7F5BD1-095E-45EF-8483-AC2DE0E4545C}](https://github.com/user-attachments/assets/1daf7996-8bdf-476f-bbe3-0e10df117824)

- uncracable (using rockyou)

![{4A11CEDE-B6E6-4F34-B5BD-73CAD4C00317}](https://github.com/user-attachments/assets/51a864ba-ca8a-4d4b-9899-ec9dedf128a2)

hmmmmmmmm

![{E4F3991B-135F-449B-B611-E496DB0C5041}](https://github.com/user-attachments/assets/a4cff72b-bede-47b9-9305-2720f7817d61)

![{477A0C2B-3120-49F8-A5A4-068A2DC0D943}](https://github.com/user-attachments/assets/8fa08cde-0caa-4f9b-878c-140c8c40f0f4)

ech przegapiłem jakiegoś usera xD

- dobra własnie sobie uświadomiłem, że nic nie zrobiliśmy z portem 8200 na hoście nr 2. Pewnie tam siedzi flaga

![{64011D13-AD9B-4612-9E33-40675A2A3042}](https://github.com/user-attachments/assets/edc19d7a-2da5-4057-bd34-cc8e88119f44)

[https://medium.com/@STarXT/duplicati-bypassing-login-authentication-with-server-passphrase-024d6991e9ee](https://medium.com/@STarXT/duplicati-bypassing-login-authentication-with-server-passphrase-024d6991e9ee)
chyba tego użyjemy

widzimy jak to się tworzy ([https://github.com/duplicati/duplicati/issues/5197](https://github.com/duplicati/duplicati/issues/5197))
```
$.ajax({
	url: './login.cgi',
	type: 'POST',
	dataType: 'json',
	data: {'get-nonce': 1}
})
.done(function(data) {
	var saltedpwd = CryptoJS.SHA256(CryptoJS.enc.Hex.parse(CryptoJS.enc.Utf8.parse($('#login-password').val()) + CryptoJS.enc.Base64.parse(data.Salt)));

	var noncedpwd = CryptoJS.SHA256(CryptoJS.enc.Hex.parse(CryptoJS.enc.Base64.parse(data.Nonce) + saltedpwd)).toString(CryptoJS.enc.Base64);

	$.ajax({
		url: './login.cgi',
		type: 'POST',
		dataType: 'json',
		data: {'password': noncedpwd }
	})
```

i cośw tym stylu musimy dostać
```
var noncedpwd = CryptoJS.SHA256(CryptoJS.enc.Hex.parse(CryptoJS.enc.Base64.parse(data.Nonce) + saltedpwd)).toString(CryptoJS.enc.Base64);
```

wszystko opisane w instrukcji i jasne

![{C60E7127-0765-48D0-A2C0-B9E4EBEB11F9}](https://github.com/user-attachments/assets/7ddd1b1b-5ba8-4044-a7a2-c873cd83bcb9)

ale zanim to zrobimy musimy się trochę cofnąć i znaleźć duplicati db `2. Open Duplicati DB using any tool (like sqlite)`

![{5F9EC9E4-B547-4E6E-A526-2C5E071560DD}](https://github.com/user-attachments/assets/3167c7be-6036-498c-a7a5-060ed7fd5d7f)

mam (login on ftp as ftp_admin and dump it)

![{1CA7CE01-ADF7-4F18-B6F2-1E6A48F8A701}](https://github.com/user-attachments/assets/38201156-056c-4793-bcb6-9d533a2c5888)

![{DD2ED1F4-EA4C-4EC7-BF06-C1511A8B8FB2}](https://github.com/user-attachments/assets/8b951c87-32d3-48c9-ac1a-6cef30f38042)


