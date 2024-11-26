# Down
Linux, easy, created by **jkr**

```
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))

```

content discovery
```
index.php               [Status: 200, Size: 739, Words: 131, Lines: 28, Duration: 41ms]
javascript              [Status: 301, Size: 319, Words: 20, Lines: 10, Duration: 33ms]
logo.png                [Status: 200, Size: 316218, Words: 1221, Lines: 1302, Duration: 30ms]
style.css               [Status: 200, Size: 1794, Words: 391, Lines: 94, Duration: 32ms]

```

![{9E33EB1D-9707-4937-9EF2-6EA655AA4930}](https://github.com/user-attachments/assets/db5bda03-fb26-4aa3-adbb-e232ae84f28b)

after `127.0.0.1`
![{1579F62C-B6CB-43FF-A893-5E7CFEAEA8E0}](https://github.com/user-attachments/assets/c50bb7cd-64cd-4029-b099-54d018c20e30)

after $myIP
![{2B5B9E9C-A794-42D0-B35F-790527A9ECDE}](https://github.com/user-attachments/assets/677ef688-d94d-4268-a31e-72741961a424)

![{871C0607-30D4-425A-AE4D-088C5229395F}](https://github.com/user-attachments/assets/28099b93-14e3-4edd-88ee-e7c0a9c24d98)

It is simple curl.

![{FB556318-4023-453F-A04D-EDA88CEA30BD}](https://github.com/user-attachments/assets/e6f886ab-33f9-476f-8cd4-c40d6de50338)

We can read a index.php file

![{E102ADD5-A3D1-4000-892A-966B2C516D2C}](https://github.com/user-attachments/assets/4f61e047-d99b-4164-830d-b9297e8746a4)

Interesting

![{46FFFC04-6770-4E14-BA30-892BCE3029EF}](https://github.com/user-attachments/assets/d755a62a-1ea2-4505-a905-6b9023075191)

```
<?php
if ( isset($_GET['expertmode']) && $_GET['expertmode'] === 'tcp' ) {
  echo '<h1>Is the port refused, or is it just you?</h1>
        <form id="urlForm" action="index.php?expertmode=tcp" method="POST">
            <input type="text" id="url" name="ip" placeholder="Please enter an IP." required><br>
            <input type="number" id="port" name="port" placeholder="Please enter a port number." required><br>
            <button type="submit">Is it refused?</button>
        </form>';
} else {
  echo '<h1>Is that website down, or is it just you?</h1>
        <form id="urlForm" action="index.php" method="POST">
            <input type="url" id="url" name="url" placeholder="Please enter a URL." required><br>
            <button type="submit">Is it down?</button>
        </form>';
}

if ( isset($_GET['expertmode']) && $_GET['expertmode'] === 'tcp' && isset($_POST['ip']) && isset($_POST['port']) ) {
  $ip = trim($_POST['ip']);
  $valid_ip = filter_var($ip, FILTER_VALIDATE_IP);
  $port = trim($_POST['port']);
  $port_int = intval($port);
  $valid_port = filter_var($port_int, FILTER_VALIDATE_INT);
  if ( $valid_ip && $valid_port ) {
    $rc = 255; $output = '';
    $ec = escapeshellcmd("/usr/bin/nc -vz $ip $port");
    exec($ec . " 2>&1",$output,$rc);
    echo '<div class="output" id="outputSection">';
    if ( $rc === 0 ) {
      echo "<font size=+1>It is up. It's just you! 😝</font><br><br>";
      echo '<p id="outputDetails"><pre>'.htmlspecialchars(implode("\n",$output)).'</pre></p>';
    } else {
      echo "<font size=+1>It is down for everyone! 😔</font><br><br>";
      echo '<p id="outputDetails"><pre>'.htmlspecialchars(implode("\n",$output)).'</pre></p>';
    }
  } else {
    echo '<div class="output" id="outputSection">';
    echo '<font color=red size=+1>Please specify a correct IP and a port between 1 and 65535.</font>';
  }
} elseif (isset($_POST['url'])) {
  $url = trim($_POST['url']);
  if ( preg_match('|^https?://|',$url) ) {
    $rc = 255; $output = '';
    $ec = escapeshellcmd("/usr/bin/curl -s $url");
    exec($ec . " 2>&1",$output,$rc);
    echo '<div class="output" id="outputSection">';
    if ( $rc === 0 ) {
      echo "<font size=+1>It is up. It's just you! 😝</font><br><br>";
      echo '<p id="outputDetails"><pre>'.htmlspecialchars(implode("\n",$output)).'</pre></p>';
    } else {
      echo "<font size=+1>It is down for everyone! 😔</font><br><br>";
    }
  } else {
    echo '<div class="output" id="outputSection">';
    echo '<font color=red size=+1>Only protocols http or https allowed.</font>';
  }
}
?>
```

looks toooooo easy

![{3B659E73-81D8-4D7E-ADE5-B12E7FDC3CC8}](https://github.com/user-attachments/assets/a607849d-d89d-42d2-bb06-9e142eca657e)

![{9BB5610A-CE83-4850-ACC1-E71FCD097105}](https://github.com/user-attachments/assets/a989bc4d-9944-4871-a127-68f4fecb6911)

yes...

![{85766C77-537A-4549-AC42-04C3ADACBCE3}](https://github.com/user-attachments/assets/86d3827a-8178-42e9-a93c-02e1484e68c8)

![{ACC7E384-6768-4D78-8D3E-B9A0345BC48F}](https://github.com/user-attachments/assets/43be3378-d99a-42a8-a3f0-af8d6090f61e)

`user_aeT1xa.txt` is userflag

It looks interesting

![{2A5D77A7-FB75-4CF0-BA9A-94E99714330D}](https://github.com/user-attachments/assets/9e32fc01-1333-49be-ad32-86a743ab43b9)

```
import cryptocode

secret = "e9laWoKiJ0OdwK05b3hG7xMD+uIBBwl/v01lBRD+pntORa6Z/Xu/TdN3aG/ksAA0Sz55/kLggw==*xHnWpIqBWc25rrHFGPzyTg==*4Nt/05WUbySGyvDgSlpoUw==*u65Jfe0ml9BFaKEviDCHBQ=="
wordlist = "/usr/share/wordlists/rockyou.txt"

with open(wordlist, "r", encoding="latin-1") as file:
    for password in file:
        if decrypted := cryptocode.decrypt(secret, password.strip()):
            print(f"[+] Password: {password.strip()}\nData: {decrypted}")
            break
    else:
        print("[-] Password not found.")

```
run the code and we got password

![{05A27722-6BB5-40F4-B0DA-8FF309C7821C}](https://github.com/user-attachments/assets/a5512d65-8f34-402d-ab1d-811b4cffdb74)


