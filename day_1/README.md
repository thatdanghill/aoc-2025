### Silver

This is a simple modulo math problem. Notice that the dial can be represented by simple additions and subtractions with modulo 100 applied.

Only a single state variable will be required to represent the state of the dial at each step. 
Two simple "left" and "right" turn operations are the only functionality we need to manipulate the state.


### Gold

The curveball here is that any time we cross 0, we must increment our count.

For a simple solution, we can simply make a nested loop to only move one click at a time, checking for zero at every click. 
However, modulo additions and subtractions happen in constant time, and it would be best if our solution could maintain that complexity.
So we need to introduce a way to determine how many times an operation "crosses" 0. 

When we turn right, we can do a simple addition and use the `//` (floored division) operator to see how many times we've crossed 0. 
Since we're always guaranteed that the start number is < 100, this simple division is guaranteed to work.

A left turn is trickier. If a subtraction gives a positive number, we haven't crossed 0 at all. 
If it's in [-99, 0], then we've crossed once. If [-199, -100], we've crossed twice. And so on.
To handle the positive case, we could use an if/else statement. But to keep it elegant, let's transform the output of the subtraction
by multiplying by -1 and adding 100, then using a simple `//` floor division. We must be careful, however. 
If the left turn starts at 0, we don't want to count that hit twice, so before making the left turn we will not count it if the state is at 0.

### Golf

No sacrifice in runtime was made for today's golf solution. 

Conditional branching logic was condensed into variables to avoid nesting.z