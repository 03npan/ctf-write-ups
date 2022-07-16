# Space Heroes CTF
## Launched

> What is the name of the launch and the payload in this picture. (flag format is shctf{rocket_payload}, spaces are underscores)

> author: GlitchArchetype

>[dunes.png](https://github.com/03npan/ctf-write-ups/blob/main/space_heroes_ctf/osint/launched/launch.png)

## Summary

Find the date taken of the photo then search for a launch on that date.

## Detailed Solution

On Windows, the "Details" tab of the image's properties shows the date taken as 4/11/2019. Searching for "space launch april 11 2019", we find [this page](https://www.space.com/spacex-falcon-heavy-triple-rocket-landing-success.html#:~:text=CAPE%20CANAVERAL%2C%20Fla.,dummy%20nicknamed%20Starman%20into%20space.).

Reading through the article, we find the rocket was Falcon Heavy, and the payload was Arabsat-6A.

Flag: `shctf{Falcon_Heavy_Arabsat-6A}`