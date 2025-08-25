# DEADFACE CTF 2022
## Scans

> Created by: syyntax
>
> ESU's IT staff noticed some peculiar traffic from DEADFACE at the beginning of the attack. They sent a series of handshakes - the IT staff is stumped as to what DEADFACE was trying to do.
>
> What type of scan did DEADFACE launch first?
>
> Submit the flag as flag{scantype}.
>
> [Download File](capture_20220727141254.zip)
>
> SHA1: c2b1fcb40d8959d24e45752fbb040521c8fcb110
>
> Password: d34df4c3

## Summary

Look at the type of packets at the start.

## Detailed Solution

There are a ton of SYN packets at the start, each going to a different port, which resembles a SYN scan.

Flag: `flag{synscan}`