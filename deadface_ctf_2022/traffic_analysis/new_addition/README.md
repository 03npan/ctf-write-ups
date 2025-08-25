# DEADFACE CTF 2022
## New Addition

> Created by: syyntax
>
> DEADFACE tried to add a user to the ESU database. What is the username of the user they tried to add to the database?
>
> Submit the flag as flag{username}.
>
> Use the packet capture from Scans.

## Summary

Find the stream where the attackers attempt to INSERT a new user into the database.

## Detailed Solution

Search for INSERT in packet bytes, and follow the stream (5158). The mysql command used is shown, and the username is "areed2022".

Flag: `flag{areed2022}`