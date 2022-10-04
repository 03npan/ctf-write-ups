# picoCTF 2022
## Redaction gone wrong

> AUTHOR: MUBARAK MIKAIL
>
> Description
>
> Now you DON’T see me.
>
> This [report](https://github.com/03npan/ctf-write-ups/blob/main/picoctf-2022/forensics/redaction_gone_wrong/Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

Tags: *Forensics*

## Summary

Copy the improperly redacted text and find the flag.

## Detailed Solution

Hovering over some of the redacted text causes the mouse cursor to change and indicate that there is text there. If we copy all the text and paste into Notepad, we see this:

```
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021. 
Breakdown - Just painted over in MS word. 
 
Cost Benefit Analysis
Credit Debit
This is not the flag, keep looking
Expenses from the 
picoCTF{C4n_Y0u_S33_m3_fully}
Redacted document.
```

Flag: `picoCTF{C4n_Y0u_S33_m3_fully}`