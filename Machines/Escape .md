# Escape
Windows, Easy, crated by **xct & kozie**

```
3389/tcp open  ms-wbt-server Microsoft Terminal Services
```

```
xfreerdp /v:10.10.116.80 -sec-nla
```

![{D5E3213A-F14F-488F-BF11-7F9C7D3BE746}](https://github.com/user-attachments/assets/64b09469-1b7e-4321-942e-c40660e5e8e5)

![{E3CCFE8A-FF20-4382-BF46-C3E4ED2E17B8}](https://github.com/user-attachments/assets/cd1542d2-ee92-43f1-ba4a-ae80ed89f292)

(tutaj nie dalo się dobrego screen machnąć więc szybki filmik nagrałem



https://github.com/user-attachments/assets/5c1b0bef-b027-46a0-9bec-1481ea91891e

dzięki temu mam informację, że jesteśmy na jakiejś statycznej stronce. Internet explorer/firefox/edge czy coś takiego. Także pewnie możemy sobie włączyć przeglądarkę (klikamy "windows button")



https://github.com/user-attachments/assets/efa9b429-63dd-444e-86b5-0a8b1c76ba96

```
file://C:/
```

![{AAC0816D-831F-429D-8B2C-096EBBA8FB59}](https://github.com/user-attachments/assets/c5b690ab-1e0c-4b56-94b3-c44fcf1ef4c9)

![{2BE9AA03-4FD5-40C5-BAB7-ECFB782DF957}](https://github.com/user-attachments/assets/a02b35c7-b220-413b-8d2d-09b461933753)

![{1742B109-6B4D-4857-9592-09181CB663B1}](https://github.com/user-attachments/assets/74f8efec-7bd6-482e-adaf-22bf9cfb47e9)

aj we can not run it. Some applocking.
- let's try easy tricks

F2 to change filename

![{DF8BF187-787D-415E-97C3-60D50CBCB959}](https://github.com/user-attachments/assets/0c3ff6a2-bde3-49f9-a41f-f471f03345c6)

![{62B2001F-0D34-4897-9B44-2670C9523CD2}](https://github.com/user-attachments/assets/148ce97b-5aaf-455d-a0d8-bfa0ff8b2297)

run it and we got shell

![{96DBE070-59D3-4BD5-A54A-FC1A4F611CB5}](https://github.com/user-attachments/assets/639c46e9-b1c4-4211-97e0-075ef0bcd291)

cmd is locked but if we switch to powershell eveything works.

![{C60B39E9-DDBE-4AF4-87E9-4B0C95B1BD0A}](https://github.com/user-attachments/assets/52becdb0-0caa-4571-b3fd-456288ef4ea4)

we have some encrypted password in `_admin`

We need read bulletpassword. Let's download `https://www.portablefreeware.com/download.php?dd64=2025`.

![{B95739D1-1625-49D8-8FCC-BD91FF40349B}](https://github.com/user-attachments/assets/c6d975bf-b94d-4bf5-b1de-5b143f32d155)

I download `BulletsPassView.exe` to kiosk machine.
(I can't save file on system..)

![{CEA3548C-E39D-4343-A3AA-F9BB1667ACFC}](https://github.com/user-attachments/assets/12b643a3-56d0-4505-870d-3c5d302f417c)

run rdp -> manage profiles

![{7150B354-50BC-4424-9A4B-8D8216431015}](https://github.com/user-attachments/assets/19010a1d-ba91-4f4d-b029-7f0c2959dc25)

We need copy profile to Download folder if we want import it

![{7150B354-50BC-4424-9A4B-8D8216431015}](https://github.com/user-attachments/assets/1769ab1b-7a00-49f4-a3b8-989089fb0d7e)

```
copy .\profiles.xml C:\Users\kioskUser0\Downloads\
```

![{18713B65-9BFD-464E-B686-558301176FC4}](https://github.com/user-attachments/assets/40e01cb2-3627-4a02-80a5-8710aeb6777e)

![{936DCAF5-1403-44C8-9889-9B8F1AD88478}](https://github.com/user-attachments/assets/e14e7a66-f55f-4696-b4d1-06acfb95ce38)

![{48485DC0-DFC8-4EE8-A52B-707B19541BCA}](https://github.com/user-attachments/assets/ce25c531-6c43-44cf-b24c-195a57d71111)

![{5A3073CF-FACF-4DFF-BE29-87E4FB483B64}](https://github.com/user-attachments/assets/1598c1e7-2dc8-4746-9df0-1863f22e61fa)

![{EB1DA132-D067-4EF7-BADC-8DA5FD62BECB}](https://github.com/user-attachments/assets/ec7dd6bc-ddc0-46e0-94b7-0c2bff3e8f99)

we can't login into him using rdp.
- back to kioskuser0

run
```
runas /user:admin cmd.exe
```

![{639EF050-EBB9-4674-B9E4-0D5EDB0F3974}](https://github.com/user-attachments/assets/6a7b6e8e-6d09-4ff8-8309-8fe6eca1387a)

to bypass UAC run
```
start-process cmd.exe -verb runas
```

![{42A69CC2-0D18-441A-BF67-5DB2205E909D}](https://github.com/user-attachments/assets/8ee254fa-18fa-44aa-862c-349bc64c0f49)

![{89170020-3AB6-42A5-923B-3C3B7B1AFFF0}](https://github.com/user-attachments/assets/74a83d5b-0438-4eed-a2c7-09957bb6cfe4)

and user flag

![{48E2377E-BC9C-4612-B193-60B4FC60DCE2}](https://github.com/user-attachments/assets/57cb72ba-7bbd-47c9-8cdb-ba2c3a86487b)
