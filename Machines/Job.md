# Job
Windows, Hard, created by **xct** 

```
25/tcp   open  smtp          hMailServer smtpd
80/tcp   open  http          Microsoft IIS httpd 10.0
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
```


klasiczek
```
enum4linux -u guest -a 10.10.95.68
enum4linux -u anonymous -a 10.10.95.68
enum4linux -a 10.10.95.68
```
- nic

content discovery
```
ASPNET_CLIENT           [Status: 301, Size: 156, Words: 9, Lines: 2, Duration: 32ms]
ASSETS                  [Status: 301, Size: 149, Words: 9, Lines: 2, Duration: 32ms]
CSS                     [Status: 301, Size: 146, Words: 9, Lines: 2, Duration: 34ms]
Index.html              [Status: 200, Size: 3261, Words: 863, Lines: 59, Duration: 38ms]
JS                      [Status: 301, Size: 145, Words: 9, Lines: 2, Duration: 31ms]

```

![{EED96F89-7507-4BD3-AD41-56EC1B8764D3}](https://github.com/user-attachments/assets/43c8f624-86d1-4974-8743-e7c6b9c6aa8b)

dobra wygląda jak jedna z dwóch opcji
- rce przez makro w phishingu (nie realistyczne i w 2024 nierealne)
- netntlmsteal przez maila

ale to vulnlab to zacznę od ciężej wersji :D

z tego biorę payload `https://0xdf.gitlab.io/2020/02/01/htb-re.html`

![{AD4E8866-C9F3-47EC-BC83-4F94406CC9E0}](https://github.com/user-attachments/assets/3c38b90c-aab3-4abc-bf61-b33efcec9780)

![{1169DD4A-13CF-4060-9103-3063E102E370}](https://github.com/user-attachments/assets/b204b108-c5c0-4d25-b00e-1f492c369293)

- nie ważne co robię nie dostaję zwrotki :/

### Powrót po 2-3 tygodniach.

Może by tak prostego makro spróbować.

![{E4F2CD0E-9DE2-4D6B-8431-ABE254835023}](https://github.com/user-attachments/assets/c51889b6-9c13-4d14-88d5-b23bd5c1fa18)

![{C9BC890F-DBED-4739-AFFC-2682274F8CB0}](https://github.com/user-attachments/assets/2ebd53a8-3aa6-4732-85f6-685020b343bb)

- nie weszło. Próbuję zrobić makro w libreoffice.

![{9343434C-EC09-48C4-A6EC-6BA906531292}](https://github.com/user-attachments/assets/dccd47d0-9138-4226-a720-d5b5be34eed2)

![{9ED6101C-C040-4D8B-9F90-C98FE87A410D}](https://github.com/user-attachments/assets/1406cba9-d2b1-4f79-b759-e1c056315dc1)

![{4EE7CADA-4B30-4A8E-AE13-00C83B259323}](https://github.com/user-attachments/assets/d1b05b18-7852-4ced-a9fd-c818ed390a04)

- jak dla mnie to coś jest zepsute. Zero reakcji nawet na http request






