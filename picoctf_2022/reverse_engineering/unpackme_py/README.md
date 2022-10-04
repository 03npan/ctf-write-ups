# picoCTF 2022
## unpackme.py

> AUTHOR: LT 'SYREAL' JONES
>
> Description
>
> Can you get the flag?
>
> Reverse engineer this [Python program](https://github.com/03npan/ctf-write-ups/blob/main/picoctf-2022/reverse_engineering/unpackme_py/unpackme.flag.py).

Tags: *Reverse Engineering, packing*

## Summary

Decode the obfuscated code to find the flag.

## Detailed Solution

When running the program, it asks for a password. Open the program to see if we can find it. The program has an obfuscated payload that is decrypted and then executed through an `exec` call. Let's modify the program to show the decrypted payload.

On the line before the `exec` call, add `print(plain.decode())`. Run the program again.

![decoded_payload.png](https://github.com/03npan/ctf-write-ups/blob/main/picoctf-2022/reverse_engineering/unpackme_py/decoded_payload.png)

We don't need the password; we see the flag: `picoCTF{175_chr157m45_5274ff21}`