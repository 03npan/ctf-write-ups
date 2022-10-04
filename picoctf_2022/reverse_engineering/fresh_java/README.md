# picoCTF 2022
## Fresh Java

> AUTHOR: LT 'SYREAL' JONES
>
> Description
>
> Can you get the flag?
>
> Reverse engineer this [Java program](https://github.com/03npan/ctf-write-ups/blob/main/picoctf_2022/reverse_engineering/fresh_java/KeygenMe.class).

Tags: *Reverse Engineering, Java*

## Summary

Decompile the program and piece together the flag.

## Detailed Solution

Offline tools exist for decompiling Java class files, but we can use an [online tool](http://www.javadecompilers.com/) instead. Upload the program and decompile it.

Flag: `picoCTF{700l1ng_r3qu1r3d_738cac89}`