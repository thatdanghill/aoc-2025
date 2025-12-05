### Silver

The naive method here works fine. Store the list of ranges and a list of ingredients, 
and have two nested loops that test inclusion of each ingredient until a range is matched.


### Gold

The naive solution here would be to create a set of fresh ingredients,
but as the input contains extremely large ranges, adding to this set would
be computationally difficult.

Instead, let's create a list of nonoverlapping ranges.
The list's invariant is that no intervals in it overlap.
To insert into the list, we loop through the list and test for overlap.
When we find a range that overlaps, we remove the range from the list, create a "joined" range,
then try again to insert the range into the list.

For example, say our list consists of:

[(1,4), (6, 10)]

and then we try to insert (3, 7).

On the first iteration of the loop, we notice that
(3,7) and (1,4) overlap. So remove (1,4) from the list, then
combine the ranges to make (1,7). Our list is now [(6,10)]

Then, we try to insert (1,7) into the list. We see it overlaps with (6,10),
so remove (6,10) from the list and combine to make (1,10). Now we insert (1,10) into the list.

As for the how to test the overlapping condition: notice
that two ranges DO NOT overlap iff the end of one is strictly before the start of the other.
The negation of this definition is much easier to encode than testing all the ways
two ranges CAN overlap. 