# DEADFACE CTF 2022
## Shells

> Created by: syyntax
>
> We know now that the attacker uploaded a file called info.php to gain access to the web server backend. What is the name of the tool/shell that gave the attacker a web shell?
>
> Submit the flag as flag{tool_name}. For example: flag{psexec}.
>
> Use the file from Scans.

## Summary

Find the stream with "info.php"

## Detailed Solution

Using Wireshark, search packet bytes for "info.php" and follow the stream of that packet (4999) - you may need to apply this column filter. At the very beginning we see: "b374k shell : connected".

Flag: `flag{b374k}`