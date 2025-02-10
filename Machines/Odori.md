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

```
modprobe nbd
qemu-nbd --connect=/dev/nbd0 /root/file02.vmdk
mkdir /mnt/1
mkdir /mnt/2
dislocker-fuse -V /dev/nbd0p3 -u /mnt/1
mount -o ro /mnt/bitlocker/dislocker-file /mnt/2
```
Wersja na windowsa wjeżdża bo mi się pomysły kończą.


