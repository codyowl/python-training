# Regular expression patterns:

### "." : Matches any character except \n 
### "^" : Matches start of string
### "$" : Matches end of string
### "*" : Matches 0 or more cases of previous regular expression
### "+" : Matches 1 or more cases of previous regular expression
### "?" : Matches 0 or 1 case of previous regular expression
### {m,n} : Matches m to n cases of previous regular expression(greedy)
### {m,n}? : Matches m to n cases of previous regular expression(non greedy)
### [...] : Matches any one of a set of characters contained within brackets
### | : Matches expression either preceding it or following it
### (...) : Matches the regular expression withing the parentheses and also indicates a group
### (?iLmsux) : Alternate way to set optional flags, no effect on match
### (?:...) : similar to (...) but does not indicate a group
### (?P<id>...) : similar to (...) but the group also gets the name id
### (?#...) : Content of parentheses is just a comment
### (?=...) : Matches what comes next but doesnot consume any part of the string
### (?!...) : Doesnot match what comes next and doesnot consume any part of the string
### (?<=...) : Matches if there is a match for regular expression
### \A : Matches an empty string but only at the start of whole string
### \b : Matches an empty string but only at start or end of a word
### \B : Matches an empty string but not at start or end of a word
### \d : Matches one digit , in the set [0-9]
### \D : Matches one non-digit, in the set [^0-9]
### \s : Matches a white space character
### \S : Matches a non-white character
### \w : Matches one alphanumeric character
### \W : Matches one non-alphanumeric character
### \Z : Matches an empty string but only at the end of whole string
### \\ : Matches one backslash character            


# Regular expression objects:

 - .match(string[, pos, endpos]) -> MatchObject
 - .search(string[, pos, endpos]) -> MatchObject
 - .findall(string[, pos, endpos]) -> list of strings
 - .finditer(string[, pos, endpos]) -> iter of MatchObjects
 - .split(string[, maxsplit]) -> list of strings
 - .sub(repl, string[, count]) -> string
 - .subn(repl, string[, count]) -> (string, int)
 - .flags      # int, Passed to compile()
 - .groups     # int, Number of capturing groups
 - .groupindex # {}, Maps group names to ints
 - .pattern    # string, Passed to compile()  
  
