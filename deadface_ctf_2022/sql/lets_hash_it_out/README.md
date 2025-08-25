# DEADFACE CTF 2022
## Let's Hash it Out

> Created by: syyntax
>
> DEADFACE discussed what users they were going to target out of the database dump obtained. Look around on Ghost Town and submit the password hash of the user they are targeting.
>
> Submit the flag as flag{hash}.
>
> Use the database from Counting Heads.

## Summary

Find the password hash of the only person that works in Administration.

## Detailed Solution

A quick search for "database" on the forum points to the target being the only person that works in Administration.

Looking at the roles:

```
INSERT INTO `roles` VALUES (5,'Adjunct Professor'),(8,'Administration'),(4,'Associate Professor'),(2,'Instructor'),(3,'Professor'),(6,'Research Assistant'),(7,'Research Associate'),(1,'Student');
```

We see that Administration is 8.

A quick Ctrl-F for ",8)" gives us a user ID of 1440, and a quick Ctrl-F for "(1440," gives us the password hash: d949c47bf15799c613e6d28731bc9a369219e49d.

Flag: `flag{d949c47bf15799c613e6d28731bc9a369219e49d}`