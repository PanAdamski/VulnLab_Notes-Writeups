# Lock
Windows, Easy, created by **xct & kozie**

```
80/tcp   open  http          Microsoft IIS httpd 10.0
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
3000/tcp open  ppp?
5357/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

```
klasyczkiem
```
enum4linux -u guest -a 10.10.96.142
enum4linux  -a 10.10.96.142
enum4linux -u anon -a 10.10.96.142
```
Mam pewność, że to będzie 80 albo 3000

80
```
.git                    [Status: 500, Size: 1208, Words: 70, Lines: 30, Duration: 65ms]
CHANGELOG.TXT           [Status: 200, Size: 46, Words: 6, Lines: 4, Duration: 34ms]
spnet_Client           [Status: 301, Size: 157, Words: 9, Lines: 2, Duration: 39ms]
Assets                  [Status: 301, Size: 150, Words: 9, Lines: 2, Duration: 32ms]
Index.html              [Status: 200, Size: 16054, Words: 3024, Lines: 347, Duration: 37ms]
```

300
```
admin                   [Status: 303, Size: 38, Words: 3, Lines: 3, Duration: 69ms]
administrator           [Status: 200, Size: 16425, Words: 1256, Lines: 358, Duration: 56ms]
explore                 [Status: 303, Size: 41, Words: 3, Lines: 3, Duration: 39ms]
favicon.ico             [Status: 301, Size: 58, Words: 3, Lines: 3, Duration: 39ms]
issues                  [Status: 303, Size: 38, Words: 3, Lines: 3, Duration: 47ms]
milestones              [Status: 303, Size: 38, Words: 3, Lines: 3, Duration: 37ms]
notifications           [Status: 303, Size: 38, Words: 3, Lines: 3, Duration: 80ms]
robots.txt              [Status: 404, Size: 19, Words: 4, Lines: 2, Duration: 40ms]
sitemap.xml             [Status: 200, Size: 279, Words: 4, Lines: 3, Duration: 2200ms]
v2                      [Status: 401, Size: 50, Words: 1, Lines: 2, Duration: 34ms]

```

![{C9B7B8FB-A101-4939-90F5-F844D652D639}](https://github.com/user-attachments/assets/214eb86e-b553-43ea-bd22-c583ff12b2da)


dobra po krótje zabawie z sitemapą mamy kilku userów
```
ellen.freeman
Administrator
```
aaaa bo to gitea xD

![{7EBA3569-C481-4A0E-AD38-74E2956E63DD}](https://github.com/user-attachments/assets/c28d4a7d-0296-48ac-a196-86203dccde6a)

tak wygląda skrypcik
```
import requests
import sys
import os

def format_domain(domain):
    if not domain.startswith(('http://', 'https://')):
        domain = 'https://' + domain
    return domain

def get_repositories(token, domain):
    headers = {
        'Authorization': f'token {token}'
    }
    url = f'{domain}/api/v1/user/repos'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Failed to retrieve repositories: {response.status_code}')

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <gitea_domain>")
        sys.exit(1)

    gitea_domain = format_domain(sys.argv[1])

    personal_access_token = os.getenv('GITEA_ACCESS_TOKEN')
    if not personal_access_token:
        print("Error: GITEA_ACCESS_TOKEN environment variable not set.")
        sys.exit(1)

    try:
        repos = get_repositories(personal_access_token, gitea_domain)
        print("Repositories:")
        for repo in repos:
            print(f"- {repo['full_name']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
- nie da się zrobić konta więc w ciemno strzelam, że chodzi albo o historię pliku albo o unięty plik.

![{2B393A4B-CEC9-4CFF-98C6-78B75A9E436D}](https://github.com/user-attachments/assets/d6535f61-0221-4a29-a969-a0292a1277aa)

hehe

po krótkiej zabawie widzimy, że istnieje jeszcze drugie repo. Fajnie byłoby je pobrać

![{223D5DAF-5891-4146-9B09-766044404FDC}](https://github.com/user-attachments/assets/3a54af6d-d8b2-4a3e-b411-7a0e93424077)

a tutaj ciekawostka, bo może nie kazdy wie, że tokenu można używać jak hasła

![{533492F4-69D6-402C-8881-AD4731F6AD68}](https://github.com/user-attachments/assets/52fe0f3f-a2f7-4061-8694-76539f91df0e)

![{9928FE26-128B-4EA7-A8DC-23B2200BEAF8}](https://github.com/user-attachments/assets/9796f3b3-19aa-43b9-ba4c-fe6bf11513c3)

chwilę się pobawiłem i nic ciekawego nie znalazłem w plikach 

![{B9E016C7-A01D-4B76-B3C5-2D12970BE15C}](https://github.com/user-attachments/assets/7071dcb4-b0e7-4750-997a-8c3ee54ea88b)

- ale mamy dostęp do repo i możemy pushować zmiany więc... 

![{CA3E1183-26FC-4F69-8A2D-3EA52C252B15}](https://github.com/user-attachments/assets/21add37a-0362-4f52-9b98-f19bb8830986)

więc apka na .net może być pomocna w rev shellu

![{A13B7168-175A-46CA-9F26-B8594313D275}](https://github.com/user-attachments/assets/04d9c78a-5f41-48b8-abe8-ec2436c02aa3)

![{9D53880D-0BA1-44B3-8918-7CA1A5861BE5}](https://github.com/user-attachments/assets/4f5b4129-b8d6-46af-8ee9-898c6507407c)

plik jest, ale komendy wykonać nie mogę :/
- spróbuję innego z neta
https://raw.githubusercontent.com/borjmz/aspx-reverse-shell/refs/heads/master/shell.aspx

![{5D5A4F11-D9A5-4113-B91E-FA4DBCBE75F0}](https://github.com/user-attachments/assets/8635cea5-224f-476b-91de-ce5bad423e4a)

![{2CAE331A-BD98-40FD-A0AD-FB2D139BF6A6}](https://github.com/user-attachments/assets/78688311-8ab1-4363-a62d-d5ec3aacb3c4)

udało się!

tak na szybko
```
Group Name                             Type             SID                                                           Attributes                                        
====================================== ================ ============================================================= ==================================================
Everyone                               Well-known group S-1-1-0                                                       Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                          Alias            S-1-5-32-545                                                  Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\BATCH                     Well-known group S-1-5-3                                                       Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                          Well-known group S-1-2-1                                                       Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users       Well-known group S-1-5-11                                                      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization         Well-known group S-1-5-15                                                      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account             Well-known group S-1-5-113                                                     Mandatory group, Enabled by default, Enabled group
BUILTIN\IIS_IUSRS                      Alias            S-1-5-32-568                                                  Mandatory group, Enabled by default, Enabled group
LOCAL                                  Well-known group S-1-2-0                                                       Mandatory group, Enabled by default, Enabled group
IIS APPPOOL\DefaultAppPool             Well-known group S-1-5-82-3006700770-424185619-1745488364-794895919-4004696415 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication       Well-known group S-1-5-64-10                                                   Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Mandatory Level Label            S-1-16-8192                                                                                                     


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                        State   
============================= ================================== ========
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process Disabled
SeAuditPrivilege              Generate security audits           Disabled
SeChangeNotifyPrivilege       Bypass traverse checking           Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set     Disabled

```

o ssh ma, ale port off :( (tak wiem, że pewnie lokalnie lata i mogę sobie pivotoać, ale to usless w takim wypadku)

![{58DD6B55-93FB-40C2-9F4D-AAC8561FF298}](https://github.com/user-attachments/assets/f7ae75ff-28ed-4a5a-9130-c2a90ff08787)

w `.git-credentials` mam hasło naszego usera
- nie wejdzie po rdp, bo grupy nie mamy
- Ale i tak spróbowałem

![{B2D44A8B-3E14-4C47-8845-D87604E33D12}](https://github.com/user-attachments/assets/e713fa45-ee14-4e4d-b505-4697137fab79)

w `c:\Users\ellen.freeman\Documents` mamy `config.xml` z jakimś potensznym AESem.

![{E2DBF80C-E63E-4DC4-B219-B231527B3350}](https://github.com/user-attachments/assets/1c881e1d-e5fb-4498-b93d-44b7feb5c6c6)

pierwszy z góry ładuję.

![{EDA6AE8D-549B-4986-A044-0B38341930B5}](https://github.com/user-attachments/assets/a345a0be-04e6-44b5-a09d-1e9b37504a6a)

i mamy usera kolejnego
- po rdp ma wjazd

![{A71C153B-214E-403F-90CB-B3CAC8FADAF3}](https://github.com/user-attachments/assets/6632cc07-2dd5-4f90-a473-ff86d0bb4833)


