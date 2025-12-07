### Silver

For parsing part 1, we don't really need to do much 
other than finding the index of the start point.

Then we can loop through each line in the map, keeping a 
set of the indices of the beams. We'll check each index
and if we encount a "^", we'll add the neighbouring indices to the set.
The final answer is the length of the set.

### Gold

The naive solution to this would be to keep track of the paths themselves.
Or, instead of maintaining a set of beam indices, we can maintain
a list of them (without removing the duplicates).

However, knowing that the number of paths is going to grow exponentially at each
step, we don't want our runtime to also scale exponentially.
So instead, we can keep track of the indices of each beam and a count 
of the number of paths taken to get there. 

We keep a dictionary where the keys are the beam indices and the values
are the beam counts. In the end, we'll get the silver and gold
solutions in one pass, with the length of the dict being the silver
solution and the sum of the values being the gold solution.