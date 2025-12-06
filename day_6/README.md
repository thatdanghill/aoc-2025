### Silver

Again today, the major lift in this problem is the parsing.
We can read each line, split on the whitespace, then
reverse the nesting of the lists using `zip(*rows)`.
Then a simple if statement determines whether we apply a 
sum or a product to each equation.

### Gold

The twist in part 2 means we need to completely change the parsing.
Instead of splitting each line, we preserve whitespace before 
we strip and store numbers.