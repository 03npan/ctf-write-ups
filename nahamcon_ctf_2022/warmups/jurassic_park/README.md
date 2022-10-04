# NahamCon CTF 2022
## Jurassic Park

> Author: @artemis19#5698

> Dr. John Hammond has put together a small portfolio about himself for his new theme park, Jurassic Park. Check it out here!

## Summary

Use robots.txt to find the hidden directory with the flag.

## Detailed Solution

Go to *link*/robots.txt. The /ingen/ directory is disallowed, so let's go to *link*/ingen.

We see an index of /ingen, including a link to flag.txt. Open the link and get the flag.

Flag: `flag{c2145f65df7f5895822eb249e25028fa}`