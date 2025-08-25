# DEADFACE CTF 2022
## The Faculty

> Created by: syyntax
>
> DEADFACE discussed what users they were going to target out of the database dump obtained. Look around on Ghost Town and submit the password hash of the user they are targeting.
>
> Submit the flag as flag{hash}.
>
> Use the database from Counting Heads.

## Summary

Find the number of students then get the number of non-students.

## Detailed Solution

There are two relevant lines in the database:

```
INSERT INTO `roles` VALUES (5,'Adjunct Professor'),(8,'Administration'),(4,'Associate Professor'),(2,'Instructor'),(3,'Professor'),(6,'Research Assistant'),(7,'Research Associate'),(1,'Student');
```

And

```
INSERT INTO `roles_assigned` VALUES (801,801,7),(802,802,1),(803,803,1),(804,804,1),(805,805,1),(806,806,1),(807,807,1),(808,808,5),(809,809,1),...
```

Students are assigned role 1, so copy the "roles_assigned" line into a text file and grep for ",1)": `grep ",1)" -o roles.txt | wc -l`

-o is needed to split each occurrence onto a new line. We get 1773 matches, so there are 2400 - 1773 = 627 non-students.

Flag: `flag{627}`