# Space Heroes CTF
## Netflix and CTF

> I don't like watching anything other than TV shows about Space Heroes.

> Author: v10l3nt

>[netflix-and-ctf.pcap](https://github.com/03npan/ctf-write-ups/blob/main/space_heroes_ctf/forensics/netflix_and_ctf/netflix-and-ctf.pcap)

## Summary

Parse the packet capture for the flag.

## Detailed Solution

Looking through the packet capture, we see a lot of "keypress" packets. The key follows "Lit_", so let's parse for that and put together the keypresses. `grep -a` is needed to process the binary file as a text file. Using `cut` and `tr` to remove the unnecessary data and newlines, we can see the flag.

![keypresses.png](https://github.com/03npan/ctf-write-ups/blob/main/space_heroes_ctf/forensics/netflix_and_ctf/keypresses.png)

"%7B" and "%7D" are '{' and '}', respectively.

Flag: `shctf{T1m3-is-th3-ultimat3-curr3Ncy}`