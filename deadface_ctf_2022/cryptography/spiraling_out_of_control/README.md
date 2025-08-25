# DEADFACE CTF 2022
## Spiraling Out of Control

> A message was left by DEADFACE on one of De Monne's machines. In Ghost Town, mirveal mentioned that he posted a hint on Twitter.
>
> This was the message that was left:
>
> fmbi~i{v1d`t3ygz~vfbn
> 
> Can you tell us what it says? Submit the flag as flag{plaintext}.

## Summary

Decrypt the dynamic rotation on the ASCII values to get the plaintext.

## Detailed Solution

On the Ghost Town forum, one post by mirveal says "I left a little calling card on one of De Monne’s machines lol." A follow-up message says "A little encoded message. Nothing serious but I think they’ll have their work cut out for them haha. Left a nice little hint on Twitter." An image is attached, but appears to be broken. However, using inspect element we get the link: [https://twitter.com/Akio08641379/status/1556370305853030401/photo/1](https://twitter.com/Akio08641379/status/1556370305853030401/photo/1). The hint is the Fibonacci sequence, from 0 to 34.

Looking at the message, we see it starts with "fmbi", which if we shift each character back by the corresponding number in the Fibonacci sequence, we get "flag". We can write a script to automate this decrypting for us. See [script](decrypt.py).

Flag: `flag{dynam1c_r0t_mirveal}`