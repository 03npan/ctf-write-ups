# Space Heroes CTF
## Flag in Space

> “The exploration of space will go ahead, whether we join in it or not.” - John F. Kennedy

> Author: v10l3nt

## Summary

Guess the flag.

## Detailed Solution

The link provided has `?flag=` following it. Lets try typing in `shctf{` and seeing what happens.

![prefix.png](https://github.com/03npan/ctf-write-ups/blob/main/space_heroes_ctf/web/flag_in_space/prefix.png)

The squares are filling in! Let's add a '}' at the end and place underscores in between to figure out where the breaks are. From here, it's just a guessing game - keep in mind that the theme is space.

Flag: `shctf{2_explor3_fronti3r}`