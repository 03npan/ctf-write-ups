# picoCTF 2022
## basic-mod1

> AUTHOR: WILL HONG
>
> Description
>
> We found this weird message being passed around on the servers, we think we have a working decrpytion scheme.
>
> Download the message [here](https://github.com/03npan/ctf-write-ups/blob/main/picoctf_2022/cryptography/basic_mod1/message.txt).
>
> Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
>
> Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

Tags: *Cryptography*

## Summary

Use a quick script to decode the flag.

## Detailed Solution

[Script](https://github.com/03npan/ctf-write-ups/blob/main/picoctf_2022/cryptography/basic_mod1/mod.py)

Flag: `picoCTF{R0UND_N_R0UND_79C18FB3}`