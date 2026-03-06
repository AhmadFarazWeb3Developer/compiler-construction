# NOTES

## 1). Tokenization: _Cleaning the code from the white spaces, commnets etc_

## 2). Syntax Error: _If error happen new tokens are requested_

\*0 or more "","a","abc"

-

* ? 0 or ` "","a","ab"

# using square brackets []

# you should use parentheses () for grouping

Why this works:
\b (Word Boundary): This is the most important part. It ensures you match "int" but not the "int" inside "printf".
| (Alternation): This acts as the "OR" operator between your keywords.
() (Grouping): This treats the list of keywords as a single unit.
Note on ^ and $: I removed these because they force the regex to match the entire line. If your line contains anything other than exactly one of those words (like int x = 5;), the match will fail.

^-?\d+(\.\d+)?([eE][-+]?\d+)?$'

Breakdown of the Logic:
^-?: Matches an optional negative sign at the very start.
\d+: Matches one or more digits (the integer part).
(\.\d+)?: An optional group matching a decimal point followed by more digits (the floating-point part).
([eE][-+]?\d+)?: An optional group for exponents:
[eE]: Matches the letter 'e' or 'E'.
[-+]?: Allows for an optional plus or minus sign in the exponent (e.g., 1e-10).
\d+: The exponent value itself.
$: Ensures the match goes to the end of the string.
Examples of what this matches:
Integers: 123, -45
Floats: 3.14, -0.5
Exponents: 1.2e10, -5.5E-3, 10e+5
Common Variations:
If you want to allow numbers that start with a decimal (like .5 instead of 0.5), use this slightly more flexible version:
^-?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?$
Are you using this for data validation (checking if a string is a number) or for lexical analysis (finding numbers inside a block of code)?

^(?=.{1,60}$)-?\d*\.?\d+$
