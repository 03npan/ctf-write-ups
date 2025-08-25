# Flare-On 9
## Flaredle

> Welcome to Flare-On 9!
>
> You probably won't win. Maybe you're like us and spent the year playing Wordle. We made our own version that is too hard to beat without cheating.
>
> Play it live at: http://flare-on.com/flaredle/
>
> 7-zip password: flare
>
> [flaredle.7z](https://github.com/03npan/ctf-write-ups/blob/main/flare_on_9/flaredle/flaredle.7z)

## Summary

Use inspect element to solve the Wordle.

## Detailed Solution

With inspect element we find that the page is using `script.js`. Looking at that file, we see three important things:

`import { WORDS } from "./words.js";`
`const CORRECT_GUESS = 57;`
`let rightGuessString = WORDS[CORRECT_GUESS];`

Let's open `words.js` and find the word at index 57. We get `flareonisallaboutcats`. You can enter it in to get the flag or check later on in the `script.js` file to see the concatenation of the flag.

Flag: `flareonisallaboutcats@flare-on.com`