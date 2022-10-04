# picoCTF 2022
## Vigenere

> AUTHOR: MUBARAK MIKAIL
>
> Description
>
> Can you decrypt this message?
>
> Decrypt this [message](https://github.com/03npan/ctf-write-ups/blob/main/picoctf-2022/cryptography/vigenere/cipher.txt) using this key "CYLAB".

Tags: *Cryptography*

## Summary

Use online tool to decode ciphertext.

## Detailed Solution

This is a very simple decryption challenge. Since we have the key, we can use an online decrypter [(dCode)](https://www.dcode.fr/vigenere-cipher) to get the flag. Simply paste in the ciphertext and key into the appropriate places and decrypt it.

Flag: `picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_ae82272q}`