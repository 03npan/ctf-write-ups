# DEADFACE CTF 2022
## Counting Heads

> Created by: syyntax
>
> DEADFACE compromised a database from Eastern State University. They fired their security team, and now they're reaching out to you to see if you can help them figure out the scope of the breach. Below is a link to the compromised database.
>
> How many users are in the database? Submit the flag as flag{#}.
>
> [Download File](esu-202209211051.zip)
>
> SHA1: 371f9bcc71efa6b0a280546943be13fea705c8c0
>
> Password: d34df4c3

## Summary

Do quick math to figure out the number of users.

## Detailed Solution

Opening the `esu.sql` file, we see at the bottom there is a line:

```
INSERT INTO `users` VALUES (801,'br3athep1g1164','DORETHEA','TEATES','I','br3athep1g1164@postportal.com','2283 Louisiana Blvd','Fredon Township',35,'7860','f','1991-05-22'),(802,...
```

The last entry in this line is numbered 3200, and since the users go from 801 to 3200, there are 2400 users.

Flag: `flag{2400}`