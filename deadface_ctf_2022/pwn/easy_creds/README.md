# DEADFACE CTF 2022
## Easy Creds

> Created by: syyntax
>
> We were going through password dumps and we found a password hash associated with an email address that crypto_vamp uses. See if you can crack the hash and find his password.
>
> Password: $6$xyz$mNc63Q/k4GOeih/lF4YFzMKrJQc31yjwQ8pBIJ8.Q2Bo/2RgiMXohuVfg/O8xUx3ENTpAEk0N1eEhU5J6VwA/0

## Summary

Use HashCat to crack the password.

## Detailed Solution

Save the hash to a file and run this command: `hashcat -a 0 -m 1800 Desktop/hash.txt /usr/share/wordlists/rockyou.txt` (locations may differ). The $6$ indicates a SHA512 hash, so `-m 1800` uses the SHA512Crypt mode. Let it run for a while and we see that it gets cracked, with HashCat outputting: `$6$xyz$mNc63Q/k4GOeih/lF4YFzMKrJQc31yjwQ8pBIJ8.Q2Bo/2RgiMXohuVfg/O8xUx3ENTpAEk0N1eEhU5J6VwA/0:123456789q`. The password has been appended to the end of the hash.

Flag: `flag{1234566789q}`