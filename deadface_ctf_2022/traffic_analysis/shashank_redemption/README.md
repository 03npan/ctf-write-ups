# DEADFACE CTF 2022
## SHAshank Redemption

> Created by: syyntax
>
> There is some internal back-and-forth at ESU regarding which file was exfiltrated by DEADFACE. They've asked us to determine "the hash of the file". When asked what kind of hash, they responded "It doesn't matter - anything so that we can verify the integrity of the data stolen". See if you can find a hash for the file stolen by DEADFACE within the packet capture.
>
> Submit the flag as flag{hash}.
>
> Use the packet capture from Scans.

## Summary

Find the stream where the attackers used a SHA hash.

## Detailed Solution

Since the challenge name gives a hint, search for SHA1 in packet bytes, and follow the stream (5054). We see the attackers ran sha1sum on a backup file after they exfiltrated it.

Flag: `flag{334a3d4f976cdf39d49b860afda77d6ac0f8a3c6}`