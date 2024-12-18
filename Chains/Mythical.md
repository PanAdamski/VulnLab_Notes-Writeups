# Mythical
Windows, Medium, created by **xct**

![lustrous_slide](https://github.com/user-attachments/assets/66e44d52-5012-43c7-a16b-63f931203195)

![{40E32462-459A-46DD-8D59-4B4C8C63B9F3}](https://github.com/user-attachments/assets/1f90b165-4e4c-41e2-84a6-5678e156c133)


![{556D61AB-437C-426F-8F12-0495E35B320E}](https://github.com/user-attachments/assets/2662ef07-7d16-474d-93ba-f6835b62a277)

```
10.10.194.5
53/udp  open  domain       Simple DNS Plus (generic dns response: NOTIMP)
88/udp  open  kerberos-sec Microsoft Windows Kerberos (server time: 2024-12-17 13:50:09Z)
123/udp open  ntp          NTP v3
137/udp open  netbios-ns   Microsoft Windows netbios-ns (Domain controller: MYTHICAL-US)

10.10.194.6
68/udp    open|filtered dhcpc
996/udp   open|filtered vsinet
65024/udp open|filtered unknown

10.10.194.7
53/udp  open  domain       Simple DNS Plus
88/udp  open  kerberos-sec Microsoft Windows Kerberos (server time: 2024-12-17 13:50:08Z)
123/udp open  ntp          NTP v3
```

w międzyczasie zdjążyłem zmienić IP, bo nie miałem czasu
```
10.10.185.37
3389/tcp open  ms-wbt-server Microsoft Terminal Services

10.10.185.38
22/tcp   open  ssh      OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     NetDNA-cache/2.2
7443/tcp open  ssl/http nginx 1.25.5


10.10.185.39
3389/tcp open  ms-wbt-server Microsoft Terminal Services
```

no cóż. Wygląda na to, że mamy jednego hosta do dyspozycji :D
(na host z 3389 psrawdziłem sec-nla)

```
ffuf -w ~/raft.txt -u https://10.10.185.38:7443/FUZZ -c -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36' -mc all -t 100 -k -fs 18
ffuf -w ~/raft.txt -u http://10.10.185.38/FUZZ -c -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36' -mc all -t 100 -fs 0
```

![{A39F720C-FFBE-4796-AD59-824020BC4E69}](https://github.com/user-attachments/assets/6235afcf-551c-4c06-9d5b-34a63539a2e8)

![{674639D4-3A4D-417A-9C2E-05A0476F32A9}](https://github.com/user-attachments/assets/0814e909-0bce-4b76-ab4d-a28a5777db18)

![{CBC11F08-E956-4ED4-BC73-6FE3FDC41652}](https://github.com/user-attachments/assets/4120d963-02fa-485a-a75e-2c3807f023cc)

co mi przychodzi do głowy jako pierwsze to znaleźć coś z graphqlu.

![{5A52D57A-A3EC-4A61-97D8-1FFB79A06C24}](https://github.com/user-attachments/assets/4c67ef29-2ed2-48fa-8027-0ce8b54fe6ce)

![{A792C9BD-782E-47FA-AB8D-9070B9922C9E}](https://github.com/user-attachments/assets/27937b05-ce58-4b91-80de-0727b578df53)

![{878D88C8-7AD3-4C15-9A44-104F21CD3902}](https://github.com/user-attachments/assets/34af6bc2-adbf-408f-bf21-89462dcc407b)

w logach coś mamy (tak spam screenów będzie bo to są w sumie moje notatki głównie hehe)

![{91F5C852-314F-4660-B63D-4FBA46C08C81}](https://github.com/user-attachments/assets/743ae514-56d2-4624-9180-0dc353ccc5f8)

![{E72C0801-704F-4756-B12F-D1E0FF108FC1}](https://github.com/user-attachments/assets/2749b95f-2617-4e8c-b5d4-8fc2ee377c20)

o komendy tutaj mogę wykonać to pewnie rce też by wpadło

![{277E5CB5-786E-42C8-8167-7C763A514B86}](https://github.com/user-attachments/assets/7c679c8a-5fcf-4d5d-9d55-b419db16ca3f)

e myślałem, że każdą sobie wykonam.

![{A8510227-27AD-46A3-B1C4-C15061D6437D}](https://github.com/user-attachments/assets/c724d46a-aa98-48c5-b0f8-117ce2f967c3)

```
Loaded Commands In Agent:

assembly_inject
	Usage: assembly_inject [pid] [assembly] [args]
	Description: Inject the unmanaged assembly loader into a remote process. The loader will then execute the .NET binary in the context of the injected process.
blockdlls
	Usage: blockdlls -block true|false
	Description: Block non-Microsoft DLLs from loading into sacrificial processes.
cat
	Usage: cat [file]
	Description: Print the contents of a file specified by [file]
cd
	Usage: cd [path]
	Description: Change directory to [path]. Path relative identifiers such as ../ are accepted.
cp
	Usage: cp [source] [dest]
	Description: Copy a file from one location to another.
dcsync
	Usage: dcsync -Domain [domain] -User [user]
	Description: Sync a user's Kerberos keys to the local machine.
download
	Usage: download -Path [path/to/file]
	Description: Download a file off the target system.
execute_assembly
	Usage: execute_assembly [Assembly.exe] [args]
	Description: Executes a .NET assembly with the specified arguments. This assembly must first be known by the agent using the `register_assembly` command.
execute_coff
	Usage: execute_coff -Coff [COFF.o] -Function [go] -Timeout [30] [-Arguments [optional arguments]]
	Description: Execute a COFF file in memory. This COFF must first be known by the agent using the `register_coff` command.
execute_pe
	Usage: execute_pe [PE.exe] [args]
	Description: Executes an unmanaged executable with the specified arguments. This executable must first be known by the agent using the `register_file` command.
exit
	Usage: exit
	Description: Task the implant to exit.
get_injection_techniques
	Usage: get_injection_techniques
	Description: List the currently available injection techniques the agent knows about.
getprivs
	Usage: getprivs
	Description: Enable as many privileges as we can on our current thread token.
ifconfig
	Usage: ifconfig
	Description: Get interface information associated with the target.
inject
	Usage: inject (modal popup)
	Description: Inject agent shellcode into a remote process.
inline_assembly
	Usage: inline_assembly [Assembly.exe] [args]
	Description: Executes a .NET assembly with the specified arguments in a disposable AppDomain. This assembly must first be known by the agent using the `register_assembly` command.
jobkill
	Usage: jobkill [jid]
	Description: Kill a job specified by the job identifier (jid).
jobs
	Usage: jobs
	Description: List currently executing jobs, excluding the "jobs" and "jobkill" commands.
jump_psexec
	Usage: jump_psexec hostname
	Description: Use sc to move laterally to a new host by first copying over apollo.exe.
jump_wmi
	Usage: jump_wmi hostname
	Description: Use wmiexecute to move laterally to a new host by first copying over apollo.exe.
keylog_inject
	Usage: keylog_inject [pid]
	Description: Start a keylogger in a remote process.
kill
	Usage: kill [pid]
	Description: Kill a process specified by [pid]
link
	Usage: link
	Description: Link to a new agent on a remote host or re-link back to a specified callback that's been unlinked via the `unlink` commmand.
load
	Usage: load [cmd1] [cmd2] [...]
	Description: Load one or more new commands into the agent.
ls
	Usage: ls [path]
	Description: List files and folders in a specified directory (defaults to your current working directory.)
make_token
	Usage: make_token -username domain\user -password abc123
	Description: Creates a new logon session and applies it to the agent. Modal popup for options and selecting an existing credential.
mimikatz
	Usage: mimikatz [command1] [command2] [...]
	Description: Execute one or more mimikatz commands (e.g. `mimikatz coffee sekurlsa::logonpasswords`).
mkdir
	Usage: mkdir [path]
	Description: Make a directory specified by [path]
mv
	Usage: mv [source] [dest]
	Description: Move a file from source to destination.
net_dclist
	Usage: net_dclist [domain]
	Description: Get domain controllers belonging to [domain]. Defaults to current domain.
net_localgroup
	Usage: net_localgroup [computer]
	Description: Get local groups of [computer]. Defaults to localhost.
net_localgroup_member
	Usage: net_localgroup_member [computer] [group]
	Description: Retrieve local group membership of the group specified by [group]. If [computer] is omitted, defaults to localhost.
net_shares
	Usage: net_shares [computer]
	Description: List remote shares and their accessibility of [computer]
netstat
	Usage: netstat
	Description: View netstat entries
powerpick
	Usage: powerpick [command]
	Description: Inject PowerShell loader assembly into a sacrificial process and execute [command].
powershell
	Usage: powershell [command]
	Description: Run a PowerShell command in the currently executing process.
powershell_import
	Usage: powershell_import (modal popup)
	Description: Import a new .ps1 into the agent cache.
ppid
	Usage: ppid [pid]
	Description: Change the parent process for post-ex jobs by the specified pid.
printspoofer
	Usage: printspoofer [args]
	Description: Execute one or more PrintSpoofer commands
ps
	Usage: ps
	Description: Get a brief process listing with basic information.
psinject
	Usage: psinject [pid] [command]
	Description: Executes PowerShell in the process specified by `[pid]`. Note: Currently stdout is not captured of child processes if not explicitly captured into a variable or via inline execution (such as `$(whoami)`).
pth
	Usage: pth -Domain [domain] -User [user] -NTLM [ntlm] [-AES128 [aes128] -AES256 [aes256] -Run [cmd.exe]]
	Description: Spawn a new process using the specified domain user's credential material.
pwd
	Usage: pwd
	Description: Print working directory.
reg_query
	Usage: reg_query [key]
	Description: Query registry keys and values for an associated registry key [key].
reg_write_value
	Usage: reg_write_value [key] [value_name] [new_value]
	Description: Write a new value to the [value_name] value under the specified registry key [key].

Ex: reg_write_value HKLM:\ '' 1234
register_assembly
	Usage: register_assembly (modal popup)
	Description: Import a new Assembly into the agent cache.
register_coff
	Usage: register_coff (modal popup)
	Description: Import a new COFF into the agent cache.
register_file
	Usage: register_assembly (modal popup)
	Description: Register a file to later use in the agent.
rev2self
	Usage: rev2self
	Description: Revert token to implant's primary token.
rm
	Usage: rm [path]
	Description: Delete a file specified by [path]
rpfwd
	Usage: rpfwd -Port 445 -RemoteIP 1.2.3.4 -RemotePort 80
	Description: Start listening on a port on the target host and forwarding traffic through Mythic to the remoteIP:remotePort. Stop this with the jobs and jobkill commands
run
	Usage: run [binary] [arguments]
	Description: Execute a binary on the target system. This will properly use %PATH% without needing to specify full locations.
sc
	Usage: sc
	Description: Service control manager wrapper function
screenshot
	Usage: screenshot
	Description: Take a screenshot of the current desktop.
screenshot_inject
	Usage: screenshot_inject [pid] [count] [interval]
	Description: Take a screenshot in the session of the target PID
set_injection_technique
	Usage: set_injection_technique [technique]
	Description: Set the injection technique used in post-ex jobs that require injection. Must be a technique listed in the output of `list_injection_techniques`.
shell
	Usage: shell [command] [arguments]
	Description: Run a shell command which will translate to a process being spawned with command line: `cmd.exe /C [command]`
shinject
	Usage: shinject (modal popup)
	Description: Inject shellcode into a remote process.
sleep
	Usage: sleep [seconds] [jitter]
	Description: Change the implant's sleep interval.
socks
	Usage: socks [port number]
	Description: Enable SOCKS 5 compliant proxy to send data to the target network. Compatible with proxychains and proxychains4.
spawn
	Usage: spawn (modal popup)
	Description: Spawn a new session in the executable specified by the spawnto_x86 or spawnto_x64 commands. The payload template must be shellcode.
spawnto_x64
	Usage: spawnto_x64 [path] [args]
	Description: Change the default binary used in post exploitation jobs to [path]. If [args] provided, the process is launched with those arguments.
spawnto_x86
	Usage: spawnto_x86 [path]
	Description: Change the default binary used in post exploitation jobs to [path]. If [args] provided, the process is launched with those arguments.
steal_token
	Usage: steal_token [pid]
	Description: Steal a primary token from another process. If no arguments are provided, this will default to winlogon.exe.
ticket_cache_add
	Usage: ticket_cache_add [b64Ticket] [luid]
	Description: Add a kerberos ticket to the current luid, or if elevated and a luid is provided load the ticket into that logon session instead. This modifies the tickets in the current logon session.
ticket_cache_extract
	Usage: ticket_cache_extract [service] [luid]
	Description: extract a ticket for the provided service name from the current or specified luid
ticket_cache_list
	Usage: ticket_cache_list [luid]
	Description: List all kerberos tickets in the current logon session, or if elevated list all tickets for all logon sessions, optionally while elevated a single luid can be provided to limit the enumeration
ticket_cache_purge
	Usage: ticket_cache_purge -serviceName=krbtgt/domain.com
	Description: Remove the specified ticket from the system. This modifies your current logon session tickets, so be careful if purging all.
ticket_store_add
	Usage: ticket_store_add [b64ticket]
	Description: Add a kerberos ticket to the agents internal ticket store. Tickets are injected into sacrificial processes when you're impersonating a token (make_token / steal_token). This is because you have a new logon session to put the tickets into without overriding your existing tickets. For safety, do a make_token with junk creds first.
ticket_store_list
	Usage: ticket_store_list [luid]
	Description: List all kerberos tickets in the agents ticket store, optionally a single luid can be provided to limit the items returned from the store
ticket_store_purge
	Usage: ticket_store_purge [b64ticket] [all]
	Description: Remove the specified ticket from the ticket store
unlink
	Usage: unlink (modal popup)
	Description: Unlinks a callback from the agent.
upload
	Usage: upload (modal popup)
	Description: Upload a file from the Mythic server to the remote host.
whoami
	Usage: whoami
	Description: Get the username associated with your current thread token.
wmiexecute
	Usage: wmiexecute [command] [host] [username] [passw	Description: The 'clear' command will mark tasks as 'cleared' so that they can't be picked up by agents


 ord] [domain]
	Description: Use WMI to execute a command on the local or specified remote system, can also be given optional credentials to impersonate a different user.
help
	Usage: help [command]
	Description: The 'help' command gives detailed information about specific commands or general information about all available commands.
clear
	Usage: clear { | all | task Num}
	Description: The 'clear' command will mark tasks as 'cleared' so that they can't be picked up by agents
```

z tego co rozumiem to robimy `shell <komenda cmd>`

![{13A62B1F-D0D0-4F88-A349-E6E306C2C1EC}](https://github.com/user-attachments/assets/b5de3371-0ff6-48d9-bcf5-894e0a04469c)

działa!

![{BC267AAD-AD0C-4314-9B1B-2472FA776B34}](https://github.com/user-attachments/assets/b09e8d6e-4c14-4ea3-a00a-945e16d5c2c4)

dużo w tym folderze

parę informacji zgarniam
```

USER INFORMATION
----------------

User Name              SID                                          
====================== =============================================
mythical-us\momo.ayase S-1-5-21-614429729-4048209472-3755682007-1129


GROUP INFORMATION
-----------------

Group Name                                 Type             SID                                           Attributes                                                     
========================================== ================ ============================================= ===============================================================
Everyone                                   Well-known group S-1-1-0                                       Mandatory group, Enabled by default, Enabled group             
BUILTIN\Remote Desktop Users               Alias            S-1-5-32-555                                  Mandatory group, Enabled by default, Enabled group             
BUILTIN\Users                              Alias            S-1-5-32-545                                  Mandatory group, Enabled by default, Enabled group             
BUILTIN\Pre-Windows 2000 Compatible Access Alias            S-1-5-32-554                                  Group used for deny only                                       
BUILTIN\Certificate Service DCOM Access    Alias            S-1-5-32-574                                  Mandatory group, Enabled by default, Enabled group             
NT AUTHORITY\INTERACTIVE                   Well-known group S-1-5-4                                       Mandatory group, Enabled by default, Enabled group             
CONSOLE LOGON                              Well-known group S-1-2-1                                       Mandatory group, Enabled by default, Enabled group             
NT AUTHORITY\Authenticated Users           Well-known group S-1-5-11                                      Mandatory group, Enabled by default, Enabled group             
NT AUTHORITY\This Organization             Well-known group S-1-5-15                                      Mandatory group, Enabled by default, Enabled group             
LOCAL                                      Well-known group S-1-2-0                                       Mandatory group, Enabled by default, Enabled group             
MYTHICAL-US\Backup Admins                  Group            S-1-5-21-614429729-4048209472-3755682007-1131 Mandatory group, Enabled by default, Enabled group             
Authentication authority asserted identity Well-known group S-1-18-1                                      Mandatory group, Enabled by default, Enabled group             
MYTHICAL-US\OpenVPN Administrators         Alias            S-1-5-21-614429729-4048209472-3755682007-1130 Mandatory group, Enabled by default, Enabled group, Local Group
Mandatory Label\Medium Mandatory Level     Label            S-1-16-8192                                                                                                  


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State   
============================= ============================== ========
SeMachineAccountPrivilege     Add workstations to domain     Disabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled


USER CLAIMS INFORMATION
-----------------------

User claims unknown.

Kerberos support for Dynamic Access Control on this device has been disabled.


User name                    momo.ayase
Full Name                    Momo Ayase
Comment                      
User's comment               
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            11/29/2024 7:11:38 AM
Password expires             Never
Password changeable          11/30/2024 7:11:38 AM
Password required            Yes
User may change password     No

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   12/18/2024 3:22:38 AM

Logon hours allowed          All

Local Group Memberships      *OpenVPN Administrator*Remote Desktop Users 
Global Group memberships     *Backup Admins        *Domain Users         
The command completed successfully.


```


ciekawe
- OpenVPN Administrators
- Backup Admins
- Remote Desktop Users

![{01346CC5-289F-4117-A556-B653D544639C}](https://github.com/user-attachments/assets/17a1ef9b-69e9-4bef-a573-b72c38682a60)


widzimy, że openvpn jest podpięty teraz

![{34C4DC63-7220-4524-A707-517AD6279C6F}](https://github.com/user-attachments/assets/1f30a540-30ba-4eea-9fa1-7dffbc233178)


ogólnie ładnie wygląda

cd 

![{9C4E06E8-37D5-47DA-AFCA-5681F91C9A79}](https://github.com/user-attachments/assets/6b787ad0-c536-4f84-a4e4-96b48178f709)

cat C:\_admin\cwrsync\cwrsync.cmd
```
@ECHO OFF
REM *****************************************************************
REM
REM CWRSYNC.CMD - Batch file template to start your rsync command (s).
REM
REM *****************************************************************

REM Make environment variable changes local to this batch file
SETLOCAL

REM Specify where to find rsync and related files
REM Default value is the directory of this batch file
SET CWRSYNCHOME=%~dp0

REM Make cwRsync home as a part of system PATH to find required DLLs
SET PATH=%CWRSYNCHOME%\bin;%PATH%

REM Windows paths may contain a colon (:) as a part of drive designation and 
REM backslashes (example c:\, g:\). However, in rsync syntax, a colon in a 
REM path means searching for a remote host. Solution: use absolute path 'a la unix', 
REM replace backslashes (\) with slashes (/) and put -/cygdrive/- in front of the 
REM drive letter:
REM 
REM Example : C:\WORK\* --> /cygdrive/c/work/*
REM 
REM Example 1 - rsync recursively to a unix server with an openssh server :
REM
REM       rsync -r /cygdrive/c/work/ remotehost:/home/user/work/
REM
REM Example 2 - Local rsync recursively 
REM
REM       rsync -r /cygdrive/c/work/ /cygdrive/d/work/doc/
REM
REM Example 3 - rsync to an rsync server recursively :
REM    (Double colons?? YES!!)
REM
REM       rsync -r /cygdrive/c/doc/ remotehost::module/doc
REM
REM Rsync is a very powerful tool. Please look at documentation for other options. 
REM

REM ** CUSTOMIZE ** Enter your rsync command(s) here

rsync --version
ssh -V
```

![{79985A87-0B8D-4F4F-8CFE-1E6A32C885A3}](https://github.com/user-attachments/assets/b30d5875-2c1b-40dc-abcb-433b36d06de7)

dobra nie widzę dużo. Poskanujemy trochę
- znalazłem na internetach. Nie testowałem wcześniej `https://github.com/elddy/NimScan`

- 

