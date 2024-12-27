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

### problemy z kalim. Wrócić
