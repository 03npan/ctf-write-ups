# picoCTF 2022
## substitution0

> AUTHOR: ???
>
> Description
>
> Download the message [here](https://github.com/03npan/ctf-write-ups/blob/main/picoctf_2022/cryptography/substitution0/message.txt).
>
> Could the string at the top be a hint?
>
> Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

Tags: *Cryptography*

## Summary

Use an online tool to decrypt the message.

## Detailed Solution

The string at the top seems to be the substitution alphabet used. Plug the substitution alphabet into an [online tool](https://www.dcode.fr/monoalphabetic-substitution) and then paste in the last line which looks to be the flag.

Output: `THE FLAG IS: PICOCTF{5UB5717U710N_3V0LU710N_59533A2E}`