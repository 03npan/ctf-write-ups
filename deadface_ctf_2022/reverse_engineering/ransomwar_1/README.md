# DEADFACE CTF 2022
## RansomWAR 1

> Created by: TheZeal0t
>
> [DarkAngel Encrypter 03](darkangel-crypt-03.exe)
>
> HINT: The Dark Angel ransomware operates only on files in the current directory that have an extension of .dface, which is used exclusively by DEADFACE members. All other file extensions and directories are ignored by this ransomware.
>
> RansomWAR 1 Challenge 1 - Obtain the SHA512 hash of the DarkAngel Encryptor program (Windows version). Enter the flag as the first eight hex digits, a colon (":"), and the last eight digits of the SHA512 hash, in lower case, as follows:
>
> flag{aabbccdd:eeff0011}

## Summary

Use CyberChef to get the hash.

## Detailed Solution

Upload the file to CyberChef and use the SHA2 recipe with size 512 to get the SHA512 hash. Then copy the first and last 8 digits.

Flag: `flag{d5241cbd:681ebf44}`