### Silver

The naive solution would be to loop over every value in the range and check that the two halves of the string are equal.
However, for very large ranges, this could have a very bad runtime.

We can do something smarter by recognizing that we only need to increment the first half of the string.
For example, for the range 10-105, we don't need to test every value in that range.
We can start from the start of the range, split it in half ("1"), and test that the 
repetition is still less than the maximum. Then, increment and do the same.

So in the above example:
- Starting from 1: 11 is in range.
- Increment to 2: 22 is in range.
- ...
- Increment to 9: 99 is in range.
- Increment to 10: 1010 is not in range.

Special attention should be taken to ranges that start with an odd number of characters. 
For example, 980-1125. It is impossible that anything in the range 980-1000 would be a repetition,
so if we encounter a first odd number, we can bump it up to the nearest power of 10. In this case, setting it at
1000 allows our first real guess to be 1010.


### Gold

For this part, the solution needs to be expanded to include
numbers of all repetitions. To do this, we can use a similar strategy to before,
but this time instead of splitting in half and incrementing,
we will split into any divisible length and increment. 