# picoCTF 2022
## basic-mod2

> AUTHOR: WILL HONG
>
> Description
>
> A new modular challenge!
>
> Download the message [here](https://github.com/03npan/ctf-write-ups/blob/main/picoctf-2022/cryptography/basic_mod2/message.txt).
>
> Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
>
> Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

Tags: *Cryptography*

## Summary

Use a quick script to decode the flag.

## Detailed Solution

[Script](https://github.com/03npan/ctf-write-ups/blob/main/picoctf-2022/cryptography/basic_mod2/mod.py)

Flag: `picoCTF{1NV3R53LY_H4RD_C680BDC1}`