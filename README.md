# psaville
A python script to generate colour codes from strings, inspired by the graphic designer Peter Saville.
The program has been rewritten by [scoliono](https://github.com/scoliono/psaville) in Javascript for those wanting a web implementation.
## Usage
The program is supposed to be run at a command prompt, and takes in 4/5 variables as input like so:
### `python psaville.py filename 'text' x y`
(-v is optional as a vertical mode)

Note that by design, the colour-coding does not differentiate between uppercase and lowercase, and it omits any unrecognized characters. Also, if there are two digits in a row, they get stacked into one block. 
This introduces ambiguity; any letter will look identical to the number corresponding with its position in the alphabet.
Peter Saville's work relied heavily on context to convey meaning, so these are just the rules I'm working with.
- Availability on pip?

Sometime in the future when I've cleaned it up a bit.

- Is this readme copied near verbatim from scoliono's except with no helpful images?

Yes, I'm *very* lazy.
