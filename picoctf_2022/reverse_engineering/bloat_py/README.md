# picoCTF 2022
## bloat.py

> AUTHOR: LT 'SYREAL' JONES
>
> Description
>
> Can you get the flag?
>
> Run this [Python program](https://github.com/03npan/ctf-write-ups/blob/main/picoctf_2022/reverse_engineering/bloat_py/bloat.flag.py) in the same directory as this [encrypted flag](https://github.com/03npan/ctf-write-ups/blob/main/picoctf_2022/reverse_engineering/bloat_py/flag.txt.enc).

Tags: *Reverse Engineering, obfuscation*

## Summary

Decode the obfuscated password to get the flag.

## Detailed Solution

When running the program, it asks for a password. Open the program to see if we can find it. The code is obfuscated, with several functions and lots of text composed of individual characters pieced together from characters in the array `a`.

Looking at the function calls, the program simply runs through the functions before exiting, save for one function: `arg133`. This function checks its parameter against an obfuscated string and exits if it doesn't match, indicating that this function is the password checking function.

Let's use Python on the command line to get the password. Run `python3` then run the following three lines:

```
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
```

`arg432 = a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]`

`print(arg432)`

The password is `happychance`.

Run the program and input this password. The flag is: `picoCTF{d30bfu5c4710n_f7w_b8062eec}`