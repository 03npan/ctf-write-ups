# UMDCTF 2022
## Class Project

> I was working on a project for my C programming class and I broke my VM when trying to compile my code! My project is due at 11:59. Can you please help me get my VM up and running again?
>
> VM Password: 1_w1ll_n07_br34k_7h15
>
> [https://drive.google.com/drive/folders/1gE4Idj6DjhJ3AX64tOL3Tp31k8gurj94?usp=sharing](https://drive.google.com/drive/folders/1gE4Idj6DjhJ3AX64tOL3Tp31k8gurj94?usp=sharing)
>
> **Author**: amanthanvi

Category: *forensics*

## Summary

Search through `.vmdk` file using 7-Zip for the flag.

## Detailed Solution

We can open `.vmdk` files using 7-Zip, so let's open the `.vmdk` file that comes with the challenge.

Going into the filesystem (`1.img`), we see a typical Linux filesystem. Based on the challenge description, it's likely that the flag might be in a user's home directory, so let's search there first.

There are two directories in `/home/`, `aman` and `aman_esc`. Searching through these directories, we eventually find `/home/aman_esc/Documents/admin_notes`.

```
ONLY USE THIS ACCOUNT FOR THINGS THAT NEED ESCALATED PRIVS

1. Check homework for today
2. Plan for class tomorrow
3. Remember to hydrate!
4. UMDCTF Kickoff! - Done!
5. Finish paper for English class.
6. Finish project for next Thursday!
7. Verify VU1EQ1RGe2YwcmtfYjBtYjVfNHIzXzRfYjRkXzcxbTN9
```

Decoding the base64 string gets us the flag: `UMDCTF{f0rk_b0mb5_4r3_4_b4d_71m3}`