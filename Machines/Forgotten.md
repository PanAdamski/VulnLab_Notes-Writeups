# Forgotten]
Linux, Easy, created by **xct**


```
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.56
```

```
feroxbuster -u http://10.10.108.172/ -w ~/raft.txt -t 100
                                                                                                                                                                                                                                            
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.108.172/
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
404      GET        9l       31w      275c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
403      GET        9l       28w      278c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
301      GET        9l       28w      315c http://10.10.108.172/survey => http://10.10.108.172/survey/
302      GET        0l        0w        0c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
[##########>---------] - 15m   366733/696322  3h      found:1       errors:9038   
🚨 Caught ctrl+c 🚨 saving scan state to ferox-http_10_10_108_172_-1735293545.state ...
[##########>---------] - 15m   366733/696322  3h      found:1       errors:9038   
[####################] - 7m    348160/348160  832/s   http://10.10.108.172/ 
[#>------------------] - 11m    18558/348160  29/s    http://10.10.108.172/survey/  
```

![{F6FC27C2-8756-4247-ACAC-4F8D3916FF06}](https://github.com/user-attachments/assets/728be240-443c-400b-9abb-8e2f9a205bc9)

![{F1EE42C5-6278-46C8-B29D-22046C171F69}](https://github.com/user-attachments/assets/04cf668f-502f-42f9-aa46-f904fcd223cc)


tutaj wygląda na coś co się nam może przydać.

Zacznę od tego

![{C2FCBC62-B4CC-4BCD-9993-F2FB701EF028}](https://github.com/user-attachments/assets/d2174b8f-4e78-4494-b48a-a4dc1be6563b)

Zaczynamy od tego

![{85D651ED-29FE-4A3A-BB5F-BC9DA58FCF9A}](https://github.com/user-attachments/assets/446bec77-b412-4794-bcd1-5b3727a18ffd)

![{E8EF22A7-D742-4E5F-85E0-B3230E6AF4E7}](https://github.com/user-attachments/assets/f75ff2f7-7729-46cd-a9b1-ab5110458fd1)

![{9931C449-87AD-41C5-BD38-15C31EEAB20F}](https://github.com/user-attachments/assets/f13270a5-6cba-4b88-8b05-e2dba758acc5)

![{B9056906-BB44-4A79-8069-1A38D932337C}](https://github.com/user-attachments/assets/0966f7f6-6b98-4fbb-bd1c-1b7709bdae0c)

![{BEC01712-CE7E-40BC-A1B0-8E184A5B49AE}](https://github.com/user-attachments/assets/329c8f82-600a-47ce-9314-e1b1a46f1581)

![{AFCDD89A-4661-4103-A4AD-FA646FCD0E58}](https://github.com/user-attachments/assets/df63b90f-75be-4fc8-aa2c-f22a0453e078)

jeżeli dostajemy taki błąd jak na screenie to trzeba zresetować usługę mysql. (screen z wiresharka)

![{982AB966-1281-46C4-94DA-0EE9F16EFAD7}](https://github.com/user-attachments/assets/48c18708-d6bc-47c8-8c5d-7b6d385fe1b9)

Nie chciało działać na root to zmieniłem tak jak na screenie i działa.

![{ACAE6736-CA7A-4ADE-9F8F-799DC609C870}](https://github.com/user-attachments/assets/9421240d-c913-48d9-a277-f40bb04bbbf1)

![{01B1B18E-DC8B-4246-A510-5FC8E2FBD3A4}](https://github.com/user-attachments/assets/b52fc046-cbc7-4640-94ac-9e19b1981428)

![{87A6E210-35D3-4FAC-8D40-4F4965E619A6}](https://github.com/user-attachments/assets/eef90a25-69b5-4e27-957a-c0bee2daddfe)

![{5B43D316-02C9-449B-AB0C-29C8C4B19214}](https://github.com/user-attachments/assets/842f6a41-423f-41d4-ab89-1da9bec79f8a)

to ukryte hasło to `password`

![{E4E2DBDF-28E5-4BF6-B453-6F345596FF08}](https://github.com/user-attachments/assets/1c2c205a-2e78-4715-a179-e5a3b9a3ad58)

o nawet to piszą.

![{A65D38A5-624A-435C-BA0F-49CF252F0C7E}](https://github.com/user-attachments/assets/3e40e61b-5572-4cac-be51-978162b495af)

dobra mamy u siebie tą całą bazę teraz.

![{D7CA506F-30A0-4E95-B3BA-17055266D52B}](https://github.com/user-attachments/assets/67806672-a9c9-49f6-b83f-e5e819cdace9)

![{6F88F0CB-2417-49D4-BA7B-CBD67F0E4F57}](https://github.com/user-attachments/assets/8aa3c562-cff0-4131-9d45-d15c2c8f76a3)

![{601A4944-C243-45C5-A1ED-E7B8CF17B4F9}](https://github.com/user-attachments/assets/cea4be9d-a18a-4539-be50-ad2f829afee8)

![{2C6C3231-8000-42B7-9EF6-A3D2675503EE}](https://github.com/user-attachments/assets/1313f62a-5c6a-49db-a65e-213d966a2609)

![{22B7D09B-FB0F-4F81-9DEC-718CFE57364F}](https://github.com/user-attachments/assets/018f78ef-d2f0-4272-bc39-d24dd1e7d260)

![{DD6A21C1-E959-4701-8C9A-E132C90B7F61}](https://github.com/user-attachments/assets/9c9397ff-b974-443d-a63b-1f34da997e24)

![{F653AE77-3F1B-45EE-9C1D-92863874227D}](https://github.com/user-attachments/assets/0af073a0-ea97-4fe7-b1cc-5e5d4c2edaf6)

Jak widzimy jesteśmy na dockerze i mamy grupę sudo.

w `env` mamy nasze hasło. Mamy uprawnienia `    (ALL : ALL) ALL` więc od ręki root.

![{94AD37EE-9C4E-4F42-9FE5-1C7ABAA77398}](https://github.com/user-attachments/assets/55f4aa4b-68d7-4f0f-ab24-cce1f3250d6a)

a ciągle bez flagi.

![{F168CE3C-1CB1-46BE-BEEF-3BFB0CFB90E9}](https://github.com/user-attachments/assets/03e7b782-1b37-484e-aaeb-6f7059e5cea0)

a jednak. To hasło z `env` pasuje do usera więc mamy usera.

![{FAF1ED40-CB9C-4511-B169-6A0B83392192}](https://github.com/user-attachments/assets/3a0480fb-b9f1-4721-ae17-f13956ef34c9)

![{79DB54BA-D27F-4CB0-B011-B216692CED32}](https://github.com/user-attachments/assets/2412af37-f370-4cbe-ae59-df45488e356f)

eskalacja to wydaje się być spacerek.

![{93BCA575-9F6B-42E6-ACEE-33C32BBB1F0C}](https://github.com/user-attachments/assets/abea8687-383f-4a9e-a693-3a1a95d74f0c)

![{5A66AF45-6226-46EF-B004-06FC6C139751}](https://github.com/user-attachments/assets/821c9a68-2e8c-42d7-8c8a-a0ca0b1485cc)


FINISH
