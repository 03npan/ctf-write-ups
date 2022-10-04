# picoCTF 2022
## morse-code

> AUTHOR: WILL HONG
>
> Description
>
> Morse code is well known. Can you decrypt this?
>
> Download the file [here](https://github.com/03npan/ctf-write-ups/blob/main/picoctf-2022/cryptography/morse_code/morse_chal.wav).
>
> Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.

Tags: *Cryptography, morse_code*

## Summary

Use Audacity to analyze the morse code audio.

## Detailed Solution

![audacity.png](https://github.com/03npan/ctf-write-ups/blob/main/picoctf-2022/cryptography/morse_code/audacity.png)

It's pretty easy to piece the morse code together into the flag once we see this.

Flag: `picoCTF{wh47_h47h_90d_w20u9h7}`