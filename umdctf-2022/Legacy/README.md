# UMDCTF 2022
## Legacy

> Fred just won’t keep up with the times. Why don't you show him the error of his ways?
>
> **Author**: esiddali
>
> `0.cloud.chals.io 28964`

## Summary

Exploit input vulnerability in Python 2.

## Detailed Solution

The challenge description suggests that the code being used is outdated and has some vulnerability we can exploit.

Use `nc` to connect to the server and port provided. We see that the program asks for input, so we try inputting some numbers.

![hint.png](https://github.com/03npan/ctf-write-ups/blob/main/umdctf-2022/Legacy/hint.png)

Luckily for us, the program tells us that the code is using Python 2. Searching for "Python 2 input vulnerabilities", we find that we can directly use a variable name in the input, and the evaluation will always be true.

Let's see if we can find the variable name to use. We'll try to crash the program with bad input and see what error message we get.

![error.png](https://github.com/03npan/ctf-write-ups/blob/main/umdctf-2022/Legacy/error.png)

Voila! We see the input is being compared to a variable `secret`. Using `secret` as our input, we get the flag.

![flag.png](https://github.com/03npan/ctf-write-ups/blob/main/umdctf-2022/Legacy/flag.png)