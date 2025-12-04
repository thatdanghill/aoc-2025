### Silver

We can use a greedy algorithm as follows:
- Find the highest value and its index in each bank (excluding the last value; duplicates take the earliest index)
- Slicing from that index forward, find the highest value.

### Gold

This can precede in mostly the same fashion, but we make the second point above iterable.
Every iteration i, find the index of the maximum of the bank (minus the last i-1 values), and then slice the bank from that index forward. 
We then add another value from the bank onto the end.