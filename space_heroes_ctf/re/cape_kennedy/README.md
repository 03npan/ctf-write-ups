# Space Heroes CTF
## Cape Kennedy

> Please find valid input for this program. Don't forget to submit in flag format. (remember this is a themed ctf, the answer is NOT random)

> author: GlitchArchetype

>[moon.py](https://github.com/03npan/ctf-write-ups/blob/main/space_heroes_ctf/re/cape_kennedy/moon.py)

## Summary

Determine the format of the password and find a password that meets the criteria and is related to the challenge name.

## Detailed Solution

Looking at the program, we can tell a couple things about the password. It is 8 characters in length and has this format: `abxyyxzz`. Also, the ASCII values of each character adds up to 713.

Looking into the history of Cape Kennedy, one program in particular stands out: Apollo. It meets the `abxyyx` format. How do we get the last two characters though? Investigating the Apollo program, one mission is quickly mentioned: Apollo 11 (first humans on the moon). "Apollo11" meets the `abxyyxzz` format. We need to check whether "Apollo11" meets the ASCII sum requirement (casing will matter).

Using `python3` on the command line, we can test this:

![ascii_sum.png](https://github.com/03npan/ctf-write-ups/blob/main/space_heroes_ctf/re/cape_kennedy/ascii_sum.png)

It meets the requirement, so flag: `shctf{Apollo11}`