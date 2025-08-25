# UMDCTF 2023
## ChungusBot v3

> Check me out in the UMDCTF2023 discord! Also my code is somewhere on GitHub.
>
> **Author**: gary

Category: *misc*

## Summary

Analyze source code of ChungusBot and interact with ChungusBot in Discord to get the flag.

## Detailed Solution

The challenge description tells us to check out the [code for ChungusBot](https://github.com/UMD-CSEC/ChungusBot_v3).

In `chungus.py` we see four different tasks that will give us parts of the flag. All messages must be sent privately to the bot.

First send the link "https://tenor.com/view/sigma-sigma-male-sigma-rule-b2k-sigma-expression-gif-27239871" to the bot. This gives you `UMDCTF{Chungu`.

Another part is given by guessing the outcome of three coin flips through "---> flip X Y Z", where "tails" is 0 and anything else is 1. This can be brute forced by guessing repeatedly, giving us `5_4ppr3c1@t3s`.

Next we need four numbers that satisfy the following two conditions: a+b+c+d > 4000 and ((a+b)*(c+d)) % 1337 == 25. Any large number will do, so sending "---> numbers 1 4 267404 1" is valid and gives us `_y0ur_l0y@lty`.

The last part asks for an attachment that contains "You like jazz?" and has at least 100 characters. Send "---> bee" with the appropriate attachement and get `_a61527bd8ec}`.

Putting it together the flag is: `UMDCTF{Chungu5_4ppr3c1@t3s_y0ur_l0y@lty_a61527bd8ec}`