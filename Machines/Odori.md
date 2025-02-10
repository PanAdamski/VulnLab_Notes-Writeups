# Odori
Linux, Medium	xct

```
22/tcp  open  ssh         OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
139/tcp open  netbios-ssn Samba smbd 4.6.2
445/tcp open  netbios-ssn Samba smbd 4.6.2
```

![{F0EA47E8-74C0-4F05-AFC3-66C0742D8B7C}](https://github.com/user-attachments/assets/1680490b-6ebb-49e7-8d59-fa07a5f7a8c0)

okey. Wszystko wygląda na to, że mamy pobrać sobie ten obraz 20GB
![{E7E51137-9AF9-4B8D-A504-36E2BD07D7C4}](https://github.com/user-attachments/assets/70909176-7283-459d-9bc2-2e3cb6bad019)

No to 15 minutek pobierania

Po dwóch godzinach "zabawy" odkryłem kilka rzeczy
- nie wiem czemu, ale zrobię tego na linuxie
- Dysk jest zaszyfrowany bitlockerem i haslo to 123456789 albo 1234567890


spróbuję to zrobić tak jak umiem xD

```
qemu-img convert -O vpc file02.vmdk file02.vhd
```
Konwersja vmdk na vhd

![{1AF20659-F2E9-40BF-AF70-ECF96840E4C8}](https://github.com/user-attachments/assets/b66c40fe-0f39-4809-9aff-dc1bdb151757)

przeniesienie na windowsa i sprawdzamy

![{9DEFDD77-8E43-4021-A9DF-59E07B2B768D}](https://github.com/user-attachments/assets/948f3d4f-fbca-44cb-8411-01eaf95ba571)

![{EBD7D001-1A71-41C7-9E81-5078E7F06F83}](https://github.com/user-attachments/assets/4dfa4f99-c9e1-430d-a120-bc8798227d85)

![{02F44934-2AFF-42AD-8C9F-A9A3D789908F}](https://github.com/user-attachments/assets/067e2ed0-e297-4098-a2d5-a2848d27c6f5)

![{18EF58B5-1AAA-4BD1-B93B-B91EE89BDBA8}](https://github.com/user-attachments/assets/88a5838f-3235-4214-a4be-5cfc8da27c08)

![{3D90C6A2-D475-4A73-8878-D7F10EDF1BC5}](https://github.com/user-attachments/assets/fb39ce28-6b82-49b4-ba8d-100988a6e566)

JEEEEEEEEE

![{88FEF937-4243-474C-9546-9B2726EBB5C3}](https://github.com/user-attachments/assets/9da2b4ce-cb22-45e8-aea7-451d9b3288b6)

dobra czas przejrzeć wszystko, ale zacząłbym od SAM i SYSTEM, żeby hasha wyciągnąc i mieć potencjalnie usera/admina

![{64ADB616-89B2-46B1-8294-7B49AD1D1607}](https://github.com/user-attachments/assets/479d3acb-e95f-4ea3-abc8-a96b5b864d01)

na pulpicie admina mamy pierwszą flagę

![sam](https://github.com/user-attachments/assets/612863cd-29d4-4346-b70b-d649142cc6da)

gained credentials give us the same privileges as a NULL or guest account

Znajdujemy jakiś skrypt do backupu

![{48A61C38-B922-465B-A754-DC281DA7C527}](https://github.com/user-attachments/assets/21b838db-afad-4475-b4a5-dcf79efa8e7f)


![{E71099BE-4825-46BB-9329-31479BB95333}](https://github.com/user-attachments/assets/91ab60ec-b3df-4130-9134-59bcf452b847)

Wygląda na to, że musimy celować w usera svc_backup i w port 22. Czyli nasze hashe trzeba złamać albo znaleźć inny sposób od odszyforwanie.

Albo opcja trzecia. Możemy sprawdzić zapisane dane uwierzytelniające zaplanowanych zdarzeń.

![{19602951-08F4-4BD7-86A0-399946FE68A4}](https://github.com/user-attachments/assets/2498211f-f33a-4cef-947c-41d5de6ee1e9)

Uwaga trzeba pokazać ukryte pliki.

No to lecimy z odszyfrowaniem. W tym przypadku bardziej opłaca się użyć pypykatza, a niżeli secretdumpa.
```
pypykatz registry --sam SAM --security SECURITY SYSTEM
```
Bo to da nam np. `LSA DPAPI secret`

Kolejne 2 godziny zmarnowane na pythona...
Zrozumiałem, że mogę to mimikatzem zrobić (w teorii).

![{4A1D31A2-EA11-467D-AD3D-C1A7CCB59EFD}](https://github.com/user-attachments/assets/c4848e25-bac9-455c-98e8-07b32572f8a6)

tutaj dużo

![{F883E559-0C8E-4CAE-AAE2-0CDBC3C20342}](https://github.com/user-attachments/assets/11a5e7fa-d5d9-4c47-907d-03ab96c9956c)

tutaj mniej, ale nie ma credsów... coś robię źle.

![{82DD61F6-7618-47F4-9F30-D78A2E3D96B3}](https://github.com/user-attachments/assets/4f31319b-1f08-4209-9ffd-3cdc9161e474)

I coraz gorzej...

```
modprobe nbd
qemu-nbd --connect=/dev/nbd0 /root/file02.vmdk
mkdir /mnt/1
mkdir /mnt/2
dislocker-fuse -V /dev/nbd0p3 -u /mnt/1
mount -o ro /mnt/bitlocker/dislocker-file /mnt/2
```
Wersja na windowsa wjeżdża bo mi się pomysły kończą.

![{962C9F06-6907-47E9-B7BB-DBB736EEE32C}](https://github.com/user-attachments/assets/6cf7667a-46de-459f-add3-155f30709088)

uzyskuję pełne SID Administratora i svc_backup.

- zmarnowałem kolejne 2h. Okazało się, że wystarczy dodać 0x przed wartość masterkey.....

![pass](https://github.com/user-attachments/assets/a9faf1ba-4866-494a-a3ca-6f8f0d82b0d5)

Generalnie tutaj jest co trzeba zrobić.
Wartości uzsykujemy z plików, które są na screenach wyżej oraz z pypykatza
```
pypykatz registry --sam SAM --security SECURITY SYSTEM
```

Widzieliśmy, że tam sftp było łączenie, ale port 22 otwarty to może się uda zwyczają sesję nawiązac.

![{35B83CF9-DA90-4C6E-A7AE-1B5AC35F8762}](https://github.com/user-attachments/assets/0addc2fc-3433-429d-b5be-b82258424434)


Długi lag, który nigdy się nie kończy. Kolejne opcje to socksproxy machnać albo po prostu połączyć się po sftp.

![{D3AAC3C9-0736-4AC5-B841-FADD4FC2A1CE}](https://github.com/user-attachments/assets/a996fd84-32fd-4596-8f89-ad2b0bb5c12c)

Wrzuciłem edytowane `authorized_keys` nie wiem na co licząc ale chyba na magię xD

![{2BF46F91-814F-43C6-B417-627ADF169F9B}](https://github.com/user-attachments/assets/e68bc5b4-200e-4fdb-baf7-d385fa5eeadb)

No to nie ma prawa podziałać bo i tak nie udaje się nam połączyć hasłem.


![{E423F775-416F-43B0-9AF9-E672ECC0149C}](https://github.com/user-attachments/assets/7d16aa0c-2e0c-40a9-aa6f-517b6eebec4e)

klasycznie coś siedzi w opt (może obejdzie się bez socksproxy).

![{D0E3AE9B-B040-4E69-9B86-F9CF62628F88}](https://github.com/user-attachments/assets/dcf2c40f-369c-43cc-b3c1-421f56a34489)

pobieramy wszystko.

cat restrict 
```
#!/bin/bash

/usr/lib/openssh/sftp-server -d $1

```

cat app.py 
```
import os
from datetime import datetime, timedelta
from helper import tar_and_move_files

backup_dir = '/backup'
archive_dir = '/archive'
threshold_date = datetime.now() - timedelta(days=3*365)

def scan_and_archive_files():
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    for root, dirs, files in os.walk(backup_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_mod_time < threshold_date:
                print(f'Moving {file_path} to archive...')
                tar_and_move_files(file_path, archive_dir)
            else:
                print(f'{file_path} is not old enough to archive.')

if __name__ == '__main__':
    scan_and_archive_files()
```

cat helper.py
```                                  
import os
import subprocess
from datetime import datetime

def tar_and_move_files(file_path, archive_dir):
    current_date = datetime.now().strftime('%Y-%m-%d')
    tar_filename = os.path.join(archive_dir, f'{current_date}_{os.path.basename(file_path)}.tar.gz')
    subprocess.Popen(["/usr/bin/tar", "-czf", tar_filename, "-C", os.path.dirname(file_path), os.path.basename(file_path)])
    os.remove(file_path)

```

Odwiedzamy foldery ze skryptów.

![{0B933718-A553-4DD2-ACC9-FC76A13DDEFD}](https://github.com/user-attachments/assets/b616440b-b420-4455-b0b9-c2e1cb747f69)

backup to folder, który mieliśmy dostępny od początku na guest/null sesji smb.

Uruchomienie pełnego shella jest dośc proste. wystarczy do pliku restrict dodać bash albo sh. Wysłać plik i mamy pełnego shella

![{0B19199D-8956-4CF6-91A7-CC91AAA4E296}](https://github.com/user-attachments/assets/dde6d9aa-44cf-4927-bf07-6a31bcdd06ec)

![{486F6995-07D0-4392-92D0-64BC91695BB1}](https://github.com/user-attachments/assets/5aeff763-2b06-4fde-abac-16eae863b8bd)




Po dłuższej analizie doszedłem do wniosku, że w celu eskalacji trzeba delikatnie zmanipulować plikiem helper.cpython-310.pyc, który jest w `/opt/archiver/__pycache__/`

Ta manipulacja plikiem pamięci podręcznej pozwoli nam "przenieść plik starszy niż 3 lata" za pomocą funkcji `subprocess.Popen` wywołując binarkę `/usr/bin/tar`. Wystarczy, że lekko ją podmienimy.
```
sed -i 's|/usr/bin/tar|/tmp/bin/tar|g' helper.cpython-310.pyc
```

i teraz powinnien korzystać z naszego "pliku binarnego".

![{35B250B8-1D0D-4331-838C-081CFE14A1DA}](https://github.com/user-attachments/assets/001d7464-c95a-40b6-b57c-dc0d68f64f7b)

![{85461A27-913A-473D-8D3C-2C7345A300BA}](https://github.com/user-attachments/assets/c0d46fcf-3d7c-4a1c-9b88-bd9af4ad1765)

tworzymy wystarczająco stary plik, żeby ztrigoerować crona i.. jesteśmy rootem :D

![{63512F17-37C0-4942-B077-CB1C7B3099FB}](https://github.com/user-attachments/assets/9afd2e07-aaf0-4997-ad5f-98980b780506)

![{DA7B2CF3-44B5-45BB-8379-6D2B677A9792}](https://github.com/user-attachments/assets/a2769b3d-c054-4a7a-bb5a-de6943b1e6f9)

FINISH!!!
