# UTCTF 2022
## Login as Admin Pt 3

> Ok sorry but just one more time. HQ really needs your help. These Web D-EVIL-opers keep changing their site and preventing us from logging in. It seems the one thing they won't change is their username and password *rolls eyes*. Can you figure out how to log in?
>
> FYI, you do not need to do the 'Login as Admin' sequence in order, and later parts are not necessarily harder than earlier ones.
>
> By Aya Abdelgawad (@Aya the Awesome on discord)
>
> [app.py](https://github.com/03npan/ctf-write-ups/blob/main/utctf_2022/login_as_admin_pt_3/app.py)

Category: *Beginner*

## Summary

Send a POST request using `curl` to get the flag.

## Detailed Solution

Login attempts from the website provided always fail. Looking into the python file provided, we see that the program is looking for a POST request with three key-value pairs (more than can be provided on the web login). Let's craft a POST request using `curl`:

![flag.png](https://github.com/03npan/ctf-write-ups/blob/main/utctf_2022/login_as_admin_pt_3/flag.png)

Flag: `utflag{omg_why_not_upd8_pwd!?!}`