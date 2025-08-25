# DEADFACE CTF 2022
## Escalation

> Created by: syyntax
>
> Somehow, the attacker was able to gain root access to the web server. We believe the attacker leveraged an existing file to gain root access. What file was modified to allow the attacker to gain root on the web server?
>
> Submit the name of the file and the name of the variable used to store the added command. Example: flag{backdoor.exe_var1} if backdoor.exe is the name of the file and var1 is the name of the variable.
>
> Use the packet capture from Scans.

## Summary

Find the file that the attacker injected a backdoor into.

## Detailed Solution

Continuing with the stream from the `shells` challenge (4999), we see at the end of the stream that the attacker injects a PHP backdoor into the backup.py file, storing the command in the `cmd` variable.

Flag: `flag{backup.py_cmd}`