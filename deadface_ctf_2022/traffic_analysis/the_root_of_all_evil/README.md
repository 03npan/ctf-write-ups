# DEADFACE CTF 2022
## The Root of All Evil

> Created by: syyntax
>
> DEADFACE is known for leaving a "calling card" on systems they exploit. What flag did the attackers leave after they gained root access to the web server?
>
> Submit the flag as flag{flag_text}
>
> Use the packet capture from Scans.

## Summary

Find the next stream that follows the backdoor injection.

## Detailed Solution

Looking for the next stream that follows the backdoor injection stream (4999), we see a new stream number that has a SYN packet (5054). Following this stream, we see the flag.

Flag: `flag{pr1vesc_wi7h_cROn}`