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




