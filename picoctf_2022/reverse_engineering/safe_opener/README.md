# picoCTF 2022
## Safe Opener

> AUTHOR: MUBARAK MIKAIL
>
> Description
>
> Can you open this safe?
>
> I forgot the key to my safe but this [program](https://github.com/03npan/ctf-write-ups/blob/main/picoctf_2022/reverse_engineering/safe_opener/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
>
> Put the password you recover into the picoCTF flag format like:
>
> `picoCTF{password}`

Tags: *Reverse Engineering*

## Summary

Find the password in the program and decode it.

## Detailed Solution

The program checks the user input against a base64 encoded string: `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz`

Decode this base64 encoded string (e.g., using an [online tool](https://www.base64decode.org/)) and we get the flag.

Flag: `picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`