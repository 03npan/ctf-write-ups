# picoCTF 2022
## rail-fence

> AUTHOR: WILL HONG
>
> Description
>
> A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?
>
> Download the message [here](https://github.com/03npan/ctf-write-ups/blob/main/picoctf_2022/cryptography/rail_fence/message.txt).
>
> Put the decoded message in the picoCTF flag format, `picoCTF{decoded_message}`.

Tags: *Cryptography*

## Summary

Use an online tool to decrypt the message.

## Detailed Solution

Using this [online tool](https://crypto.interactive-maths.com/rail-fence-cipher.html), we set a custom alphabet: `abcdefghijklmnopqrstuvwxyz1234567890 :_` (based on the characters in the ciphertext).

Paste in the ciphertext, decrypt, and we get: `the flag is: wh3r3_d035_7h3_f3nc3_8361n_4nd_3nd_4a76b997`

Flag: `picoCTF{wh3r3_d035_7h3_f3nc3_8361n_4nd_3nd_4a76b997}`