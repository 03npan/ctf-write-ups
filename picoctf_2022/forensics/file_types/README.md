# picoCTF 2022
## File types

> AUTHOR: GEOFFREY NJOGU
>
> Description
>
> This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.
>
> You can download the file from [here](https://github.com/03npan/ctf-write-ups/blob/main/picoctf-2022/forensics/file_types/Flag.pdf).

Tags: *Forensics*

## Summary

Use `file` to see what type of file we have then run appropriate commands.

## Detailed Solution

Basic steps: run `file`, run appropriate command given file type (install packages as needed), repeat.

1) shell archive text, execute Flag.pdf as a shell script (need to install `uudecode` through sharutils)

2) current ar archive, extract using `ar -x flag`

3) cpio archive, extract using `cpio -idv < flag`

4) bzip2 compressed data, block size = 900k, extract using `bzip2 -d flag`

5) gzip compressed data, rename file to have `.gz` extension, extract using `gzip -d flag.gz`

6) lzip compressed data, extract using `lunzip -d flag`

7) LZ4 compressed data, rename file to have `.lz4` extension, extract using `lz4 flag.lz4`

8) LZMA compressed data, extract using `lzma -d flag`

9) lzop compressed data, extract using `lzop -d flag`

10) lzip compressed data, extract using `lunzip -d flag`

11) XZ compressed data, extract using `xz -d flag`

(Note that `-k` can be used with many of these to keep the original file)

Now we have ASCII text. It's not clear what format they are in, but they are mostly numbers with a few letters going up to 'f' so let's assume it's hexadecimal. Let's assume they are hex strings for ASCII characters.

`cat flag | xxd -r -p`

Flag: `picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}`