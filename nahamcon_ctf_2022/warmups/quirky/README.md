# NahamCon CTF 2022
##  Quirky

> Author: @JohnHammond#6971

> This file is seems to have some strange pattern...

> Download the [file](quirky)

Tags: *Warmups*

## Summary

Use CyberChef to get the flag.

## Detailed Solution

The file appears to be in hexadecimal format. If we put the file into CyberChef and use the "From Hex" recipe we see that it is a PNG of some sort. Turns out it is a QR Code, so we can parse it with the "Parse QR Code" recipe to get the flag.

Flag: `flag{b7e2a32f5ae629dcfb1ac210d1f0c032}`