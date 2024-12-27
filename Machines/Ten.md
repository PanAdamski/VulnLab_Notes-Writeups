# Ten
Linux, Hard, created by **jkr**

![ten_slide](https://github.com/user-attachments/assets/a7760b71-b99f-476a-bfcc-9726742d5b23)

```
21/tcp open  ftp     Pure-FTPd
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
```

![{1B20FF0C-E42E-4EF8-A64B-942CC22D94FC}](https://github.com/user-attachments/assets/27f8029b-fcd0-42ec-ac52-3881ef7cdbe7)

Ciekawe. Nowe dla mnie


![{CFA0FD31-D280-42AF-88BB-5B060E926B66}](https://github.com/user-attachments/assets/d1876d00-e1c1-40fd-9176-c40e71382aa8)


![{7A01569B-EC0A-4460-8C2C-365F11363663}](https://github.com/user-attachments/assets/a2df3226-f14d-4e1f-92ba-7bcb73e2c820)


![{1C83905D-E940-454F-9157-FD0F298B5E0C}](https://github.com/user-attachments/assets/6b9ef36b-7e1e-4f12-a345-8a1adacfa6e4)


![{32290BD8-4A4F-4B5E-8BE0-009AD89DE748}](https://github.com/user-attachments/assets/8f48828e-e9d9-4a8d-80f1-69f0d7800bf9)


![{8586D676-AA0F-4B90-A047-83DD6A5B7551}](https://github.com/user-attachments/assets/b3cdabe8-9041-4812-b38d-1bff2df41c3d)


![{73801E37-B657-4F79-B6F1-665AB0B59F4C}](https://github.com/user-attachments/assets/56178e46-c1c8-46ec-9b74-5dd5d860002a)

fajny endpoint.


![{A76CDB18-B9A4-4DA6-B5DD-20681F0087FE}](https://github.com/user-attachments/assets/3148db33-60de-458f-8762-c57d6528238c)


![{22903816-2272-4198-A9C6-D1C6CE2DDDBB}](https://github.com/user-attachments/assets/96f51d73-b4a9-4bdc-9fd6-0329daf75e70)

hmm.. mogę tam wrzucić chyba wszystko.

![{4B3BE534-E048-42BB-8032-6995D8DA18B9}](https://github.com/user-attachments/assets/fe843c74-1120-4d3c-a5c7-b891c4ce628e)

już myślałem, że będzie za prosto xD
Ale jako, że średnio jest z tym co zrobić to pewnie trzeba poszukać innych subdomenek po prostu.


![{7E28CE6A-ACD6-483E-8359-3E7D6FD92181}](https://github.com/user-attachments/assets/a4f33165-8885-4298-b23f-7576a1c7771a)

![{9F13946D-839B-4F54-8A20-080FCE3A5736}](https://github.com/user-attachments/assets/c9f7dbeb-1845-4315-9327-f7dad9319d6a)

oooo tutaj więcej zabawy może być.


![{82E28843-2650-4DA8-A3F0-79F00DD84822}](https://github.com/user-attachments/assets/b459b790-8a3a-4931-b1e3-49f18da75f2e)

- ale mamy wejście jako `guest`.

![{1BB788C7-8A1A-41D8-9BD2-A356DCFB86DA}](https://github.com/user-attachments/assets/498cc5fd-ad6e-4234-8fbe-2af8ee548404)

ooo mamy nasz katalog roboczy. `/srv/ten-e793d83e/./` czyli po prostu `/srv/<username>`


![{BD9E2653-644F-4E13-B451-1703F015E7F1}](https://github.com/user-attachments/assets/cd463687-c00b-49b0-a795-5e7aed7afd9a)

Możemy tworzyć i wykonywać query.


![{6C441BBC-068C-4F63-B1E3-557A60D4275F}](https://github.com/user-attachments/assets/eb8d7b9f-6be7-4d38-b993-81249857340e)

Działa.
- to teraz trzeba wymyślić co tutaj zrobić. Najprostsze co mi przychodzi do głowy to rce przez zapisane pliku .php, ale to hard i pewnie nie będzie permisji.
Drugi co bym chciał zrobić to update tego co już mamy i znamy czyli nasz katalog domowy.


![{ADC177B8-AB1B-4114-9ED5-640B7259D7F2}](https://github.com/user-attachments/assets/59af5fe3-b0d0-49b7-a472-f1b9b7be3138)


![{F0E420F7-6D95-4B01-B507-2B48D38D8765}](https://github.com/user-attachments/assets/8496ca72-86c6-43ef-8ca7-eaa398b07264)

teraz mamy znacznie większą widocznośc na filesystem.


![{15145063-2A89-4BA0-946D-E020E9C2E24D}](https://github.com/user-attachments/assets/419ef771-ab07-4b68-9f6c-a11c63be58ca)

dobra mamy jakies info o userze. Wiemy, że to `tyrell` i ma uid 1000.
Ciekawe czy jak zmienimy nasze uid to się tam dostaniemy.


![{641094C2-8F5B-4BEB-BAC2-A3D6C57C927E}](https://github.com/user-attachments/assets/a7dc77cd-b281-499d-b36b-0ecdcf4313d4)


![{81C05B24-11FD-421E-9D5F-688B372084C9}](https://github.com/user-attachments/assets/552d3883-5023-4cf3-8acc-c6a6546e062f)

o udalo się :O


![{04970E18-924E-4F0C-93B6-10DA81A73D5A}](https://github.com/user-attachments/assets/9d6363b8-ff58-45a8-8a5a-dc9af6e17148)

nie możemy wejśc do .ssh, a to wydaje się niezbędne, żeby mieć shella.


![{77B1B138-40BD-40F2-BD98-82FD41FD3B03}](https://github.com/user-attachments/assets/365ad592-c0ce-4055-9641-286f3b3e87b4)

tak nie działa.


![{DD87F9B4-6C48-4605-8827-68CC48E19563}](https://github.com/user-attachments/assets/fa38dd09-6bc0-4c85-8031-92996c60cca6)


![{0288AE27-7C56-4B6A-93B7-69467884E014}](https://github.com/user-attachments/assets/bd574036-231d-4c8f-9072-2ee93def458b)

tak działa


![{F29E2D06-B84D-4CAA-B4CC-FA2BB6ACE519}](https://github.com/user-attachments/assets/feeb9687-c3a7-400a-86d0-e8f3cdd24553)

na wszelki wypadek zapisałem sobie ten plik.


![{039CEA30-5412-41E3-BB8A-7F48277C7275}](https://github.com/user-attachments/assets/18ac0f2e-1c28-41d4-9751-a29adf8018d8)


![{05CD5CE9-C2EF-4950-AA03-8163E13C6FDA}](https://github.com/user-attachments/assets/b591f60b-01e3-4780-88ef-68abe08f58ba)


![{00D35698-58E0-4B41-B5DA-2C50B3166C83}](https://github.com/user-attachments/assets/e556986f-aaf7-4509-a0b4-70b94cbad7b8)

trochę wyliczam i musiałem zobaczyć co tutaj siedzi. Jakie haslo niby jest


![{A8C2CDB5-50AF-4121-BF85-CDDEF5678619}](https://github.com/user-attachments/assets/48cff508-ce27-4dcc-8c17-966980f26d43)
