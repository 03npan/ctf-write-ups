# DEADFACE CTF 2022
## Two Dead Boys

> Created by: TheZeal0t
>
> Good evening, this is a NEWSFLASH from Quick News Network (QNN)... I'm Crime News Reporter Frank Viginere.
>
> Ladies and gentleman skinny and scout I'll tell you a tale I know nothing about The admission is free so pay at the door Now pull out a chair and sit on the floor
>
> On one bright day in the middle of the night Two dead boys got up to fight Back to back they faced each other Drew their swords and shot each other
>
> The blind man came to see fair play The mute man came to shout hooray The deaf policeman heard the noise And came to stop those two dead boys
>
> He lived on the corner in the middle of the block In a two story house on a vacant lot A man with no legs came walking by And kicked the lawman in his thigh
>
> He crashed through a wall without making a sound Into a dry creek bed and suddenly drowned A long black hearse came to cart him away But he ran for his life and is still gone today
>
> I watched from the corner of the table The only eyewitness to facts of my fable If you doubt my lies are true Just ask the blind man, he saw it too
>
> Gla ktwulpbr pg Klkw Urao ax qlsn{Pvelnnad Aumjcnyg: Ibrwpaty ENLECPZNYG!}
>
> Submit the flag as flag{flag text}

## Summary

Use an online tool to solve the Vigenere cipher.

## Detailed Solution

This is a Vigenere cipher, so let's use an [online tool](https://www.dcode.fr/vigenere-cipher). Paste in the last line as the ciphertext, and since we know the line contains "flag" we can decrypt using the "Knowing a plaintext word" method, which gives us a plaintext of `The solution to Fake News is flag{Critical Thinking: Question EVERYTHING!}`

Flag: `flag{Critical Thinking: Question EVERYTHING!}`