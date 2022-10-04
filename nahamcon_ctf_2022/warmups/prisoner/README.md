# NahamCon CTF 2022
## Prisoner

> Author: @JohnHammond#6971

> Have you ever broken out of jail? Maybe it is easier than you think!

Tags: *Warmups*

## Summary

Break out of the Python jail and access the flag file contents.

## Detailed Solution

Use Ctrl-D to send an EOF to the jail. The Python prompt `>>>` appears.

Let's find where we are. `import os`, then `os.listdir(os.getcwd())` to get contents of current directory.

We see flag.txt is one of the files. Let's print its contents. (Make sure to include the tab on the second line!)

```
with open ("flag.txt", "r") as f:
     print(f.read())
```

Flag: `flag{c31e05a24493a202fad0d1a827103642}`