# DEADFACE CTF 2022
## "D" is for Dumb Mistakes

> Created by: rajn-b
>
> To show off their 1337 programming skills, DEADFACE attempted to create their own encryption process to help them communicate privately. Although the encryption process is working, the decryption process is flawed. The De Monne security team was able to find DEADFACE's code and can see that they are trying to use the RSA algorith with these variables:
>
> Prime numbers of 1049 and 2063
>
> Exponent of 777887
>
> Recompute the decryption key (d) and submit the flag as flag{d=VALUE}

## Summary

Use an online calculator to find d.

## Detailed Solution

Use [Wolfram Alpha](https://www.wolframalpha.com/widgets/view.jsp?id=d5bb63088eb2fb2e762f1c260d2b886d) to calculate d using the given numbers.

Flag: `flag{d=1457215}`