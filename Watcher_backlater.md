# Watcher
Linux	Medium	created by **DarkCaT & whatev3n**

```
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-title: Did not follow redirect to http://watcher.vl/
```

szukamy sub domenek
```
ffuf -u http://watcher.vl/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -H "Host: FUZZ.watcher.vl" -c -mc all -fs 4991
zabbix                  [Status: 200, Size: 3946, Words: 199, Lines: 33, Duration: 217ms]
```


