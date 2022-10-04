# picoCTF 2022
## Lookey Here

> AUTHOR: LT 'SYREAL' JONES / MUBARAK MIKAIL
>
> Description
>
> Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.
>
> Download the data [here](https://github.com/03npan/ctf-write-ups/blob/main/picoctf-2022/forensics/lookey_here/anthem.flag.txt).

Tags: *Forensics, grep*

## Summary

Search the file for the prefix of the flag.

## Detailed Solution

Open the file in Notepad and search through it (Ctrl-F) for the prefix of the flag: `picoCTF`.

On Linux `grep` will do the same thing.

Flag: `picoCTF{gr3p_15_@w3s0m3_4c479940}`