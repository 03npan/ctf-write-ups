# UMDCTF 2022
## ChungusBot v2

> Check out my code!
>
> NOTE: Browser Discord might be finicky with this challenge.
>
> **Author**: itsecgary

Category: *misc*

## Summary

Analyze source code of ChungusBot and interact with ChungusBot in Discord to get the flag.

## Detailed Solution

The challenge description tells us to check out the [code for ChungusBot](https://github.com/UMD-CSEC/ChungusBot_v2).

In `chungus.py` we see a section that will give us the flag.

![flag_code.png](https://github.com/03npan/ctf-write-ups/blob/main/umdctf-2022/chungusbot_v2/flag_code.png)

It looks like there are two checks we need to pass: `check1` and `check2`.

We see line 55: `if str(ctx.channel.type) == "private" and start in str(ctx.content) and str(ctx.content).split(start)[1] in commands:`. To attempt the checks, we need to send a DM to ChungusBot, with the command `Oh Lord Chungus please ` + one of the four options in the `commands` array.

Let's try to get the flag: `Oh Lord Chungus please tellme theflag`

![flag_fail_1.png](https://github.com/03npan/ctf-write-ups/blob/main/umdctf-2022/chungusbot_v2/flag_fail_1.png)

The `check1` function is comparing our profile picture to... something. Likely the bot's profile picture. Trying similar pictures from online doesn't work though.

However, there is a piece of code in `cogs/tellme.py` that is of interest.

![avatar.png](https://github.com/03npan/ctf-write-ups/blob/main/umdctf-2022/chungusbot_v2/avatar.png)

There is a DM-only command, `avatar`, that sends us a picture. Let's try: `Oh Lord Chungus please tellme avatar`

![chunga_diff.png](https://github.com/03npan/ctf-write-ups/blob/main/umdctf-2022/chungusbot_v2/chunga_diff.png)

We have the profile picture, but there's a slight problem. The red scribbles are not in the bot's profile picture.

Removing the red using Paint, we can now set our profile picture to this image. However, there's a problem. When we ask for the flag, ChungusBot says:

`not the right time my friend`

Let's take another look at the source code: `if check2(str(ctx.created_at)):` (line 60)

So `check2` is comparing the time that we sent our message at:

`something = int(hmm.split(':')[-1].split('.')[0])`
    `if (something > 45 and something < 50) or (something > 14 and something < 19):`
        `return True`

Looking up the created_at field, we find that it returns the time as a datetime.datetime object, formatted as `YYYY-MM-DD HH:MM:SS.Millis`. Splitting this using the code above gives us the specific second that the message was sent. So to get the flag, we need to send the message sometime between either 45-50 seconds or 14-19 seconds.

We get the flag: `UMDCTF{Chungus_15_wh0_w3_str1v3_t0_b3c0m3}`