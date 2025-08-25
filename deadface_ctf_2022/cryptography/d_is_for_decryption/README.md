# DEADFACE CTF 2022
## "D" is for Decryption

> Created by: rajn-b
>
> Now that you know the correct RSA decryption value d from "D" is for Dumb Mistakes, can you use it to properly decrypt one of DEADFACE's private messages? The ciphertext that De Monne's security team intercepted was:
>
> 992478-1726930-1622358-1635603-1385290
>
> Assuming each - character separates each letter of the ciphertext and every letter in the alphabet is represented by its position (i.e., a = 1, b = 2, etc.), what is the plaintext version of this message? Submit the flag as flag{plaintext}.

## Summary

Use a script to decrypt the ciphertext.

## Detailed Solution

See [script](decrypt.py). Note that the ciphertext should be broken apart into the individual letters before decrypting. After running the script, simply convert the number to the corresponding letter of the alphabet.

Flag: `flag{ghost}`