### Silver

This problem is a simple looping algorithm. 
The gotchas are mostly in the form of off-by-one errors that may arise.

For each spot, if it is an @, check the eight surrounding places, being
careful not to get an IndexError by going out of bounds.

### Gold

Now we just need to iterate over our algorithm, keeping track of how many
rolls are removed until 0 are removed. After each step, we will update the room
to remove the rolls.