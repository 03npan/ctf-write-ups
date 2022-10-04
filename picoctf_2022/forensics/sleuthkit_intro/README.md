# picoCTF 2022
## Sleuthkit Intro

> AUTHOR: LT 'SYREAL' JONES
>
> Description
> Download the [disk image](https://github.com/03npan/ctf-write-ups/blob/main/picoctf-2022/forensics/sleuthkit_intro/disk.img.gz) and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.
>
> Access checker program: nc saturn.picoctf.net 52279

Tags: *Forensics, sleuthkit*

## Summary

Use `mmls` to get the length in sectors of the Linux partition.

## Detailed Solution

Extract the image and use `mmls` to get the length in sectors of the Linux partition: 202752

Connect to the checker using the provided command and get the flag.

Flag: `picoCTF{mm15_f7w!}`