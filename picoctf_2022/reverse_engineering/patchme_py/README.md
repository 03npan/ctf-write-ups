# picoCTF 2022
## patchme.py

> AUTHOR: LT 'SYREAL' JONES
>
> Description
>
> Can you get the flag?
>
> Run this [Python program](https://github.com/03npan/ctf-write-ups/blob/main/picoctf_2022/reverse_engineering/patchme_py/patchme.flag.py) in the same directory as this [encrypted flag](https://github.com/03npan/ctf-write-ups/blob/main/picoctf_2022/reverse_engineering/patchme_py/flag.txt.enc).

Tags: *Reverse Engineering*

## Summary

Find the password in the Python program and use it to get the flag.

## Detailed Solution

In the Python program, a check is performed on the user's input, and if the password matches, the flag is decoded.

Password: `ak98-=90adfjhgj321sleuth9000`

Run the program and input the password.

Flag: `picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}`