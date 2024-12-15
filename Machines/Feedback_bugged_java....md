# Feedback
Linux,Easy, created by **xct**
![feedback_slide](https://github.com/user-attachments/assets/c7f34a5d-01b3-43cb-b7ad-db1a8ee62b82)

```
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
8080/tcp open  http    Apache Tomcat 9.0.56
```
```
ffuf -w ~/raft.txt  -u http://10.10.103.197:8080/FUZZ -c -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36' -mc all -fw 68,66

RELEASE-NOTES.txt       [Status: 200, Size: 6898, Words: 862, Lines: 175, Duration: 41ms]
docs                    [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 35ms]
examples                [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 68ms]
favicon.ico             [Status: 200, Size: 21630, Words: 19, Lines: 22, Duration: 35ms]
feedback                [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 43ms]
host-manager            [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 33ms]
index.jsp               [Status: 200, Size: 11136, Words: 4198, Lines: 199, Duration: 60ms]
manager                 [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 39ms]
```

Jak maszynka nazywa się `Feedback` i mamy katalog `feedback` to tam idę xd

![{E26EDA92-67DA-4483-95DD-8CAADE33A353}](https://github.com/user-attachments/assets/39262a51-0055-4ec4-ac66-ec82c9974d83)

![{C5D0A5A1-CCEB-4596-BC09-453794CF5593}](https://github.com/user-attachments/assets/78059483-8324-4bae-8be5-f57ba132d024)

Przy okazji 2021 rok wydania to trochę mi śmierdzi i czuję, że wiem jaka tam siedzi podatność
![{DCA91D6A-F144-49A2-ACAA-8F4A0A3082CA}](https://github.com/user-attachments/assets/f22f5b76-e24c-4950-bb43-1dba1de48f6f)

![{FFA53A71-3A52-4FCB-8648-80BE324A501B}](https://github.com/user-attachments/assets/e952a117-e2cb-40fd-bd1e-e1a4141388a7)

Bingo
- teraz przygotować exploit, a wiem, że w 2024 są z tym lekkie problemy.. (ja spróbuję z tym https://github.com/cybereason/Logout4Shell.git)

![{7D472CEE-78C0-4F4B-8A72-FEC16E3F9E22}](https://github.com/user-attachments/assets/5b0ef247-be6f-471d-b5df-10f0b9265e2f)

zaczyna się...

kolejna próba [https://github.com/kozmer/log4j-shell-poc](https://github.com/kozmer/log4j-shell-poc)

![{18F81C88-8232-44B6-9B55-99DBFD8FCCEA}](https://github.com/user-attachments/assets/6229c2c0-baf4-4d9f-8559-50f0b5d8e426)

trzeba znaleźć staszą javę

![{49292569-82B7-4BBF-8C25-E2039685826E}](https://github.com/user-attachments/assets/1f3b2aec-99ce-49f8-b6bb-820ec8bddff6)

![{302ECB26-A8B8-4FE0-85E0-F53A2792C70E}](https://github.com/user-attachments/assets/494c4c26-cf8b-42ca-a42a-6f88b4636a80)

![{2FE8DED2-A475-4169-A53A-5B351909E96F}](https://github.com/user-attachments/assets/b56599a9-64b8-40dc-a1d9-bf4982b2fc10)

`library initialization failed - unable to allocate file descriptor table - out of memory`??????????



