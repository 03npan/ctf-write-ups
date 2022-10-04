# picoCTF 2022
## credstuff

> AUTHOR: WILL HONG / LT 'SYREAL' JONES
>
> Description
>
> We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?
>
> Download the leak [here](https://github.com/03npan/ctf-write-ups/blob/main/picoctf-2022/cryptography/credstuff/leak.tar).
>
> The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.

Tags: *Cryptography*

## Summary

Decode the encrypted flag using the Caesar cipher.

## Detailed Solution

The passwords are all ciphertext with no apparent pattern. Since the password for `cultiris` is on the same line number as the username is, let's find which line the username is on: `grep -n cultiris usernames.txt`

We get line 378. Let's see what the password looks like on line 378: `sed -n '378p' passwords.txt`

We get: `cvpbPGS{P7e1S_54I35_71Z3}`. Certainly seems to be formatted like a flag. We can assume `cvpbPGS` is `picoCTF` then. We see that both 'c' and 'C' map to 'p' (with matching casing), hinting that the cipher used might be a substitution cipher. In fact, each character in the ciphertext is a shift of the plaintext character by 13, so it's possible that the cipher is a Caesar cipher.

Decoding the ciphertext with a shift of 13 using an [online tool](https://www.dcode.fr/caesar-cipher) for the Caesar cipher, we get the flag: `picoCTF{C7r1F_54V35_71M3}`