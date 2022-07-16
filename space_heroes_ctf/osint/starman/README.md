# Space Heroes CTF
## Starman

> How far away from earth was the space car on January, 20 2021 at 1515 UTC? Enter distance in terms of Million Km. (Rounded to two decimals) (e.g shctf{xx.yy})

> Wrap in shctf{}

> Author: Lil Tipo

## Summary

Access `robots.txt` to get the flag.

## Detailed Solution

The car in question is called a Tesla Roadster, so let's search up "roadster space distance". We find a [site of interest](https://theskylive.com/how-far-is-roadster). 

On the right there is an "Ephemeris Calculator", click "Compute Ephemeris". Even if we specified a date and time before clicking, it defaults to "02-Apr-2022 02:29". There is a clock icon on the left to set the exact date and time. Set it to 20 Jan 2021 15:15. Earth distance is listed as 56.68 Million Km.

Flag: `shctf{56.68}`