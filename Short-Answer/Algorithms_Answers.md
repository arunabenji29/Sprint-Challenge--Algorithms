#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The run time of this is O(n), since the while loop runs only n times.


b) The run time of this is O(n^2), since there is a while loop inside a for loop. Meaning there is a loop inside a loop, which has to run n^2 times.


c) the run time of this is O(n). Since the recurisve function is passed n-1 times after the function is invoked for the first time.

## Exercise II

Fn eggsThrown(n)

-> If n>=f then the eggs gets broken

-> if n < f then the eggs does not get broken

This is a binary search. 

For example:

Lets say a building has 10 floors. The number of floors can be divided by 2. The egg can be dropped from the 5th floor. If the egg breaks, then anything higher than 5, the egg can be broken.

So the midpoint of 1st-5th floor is taken,which is 2nd floor to see which floor the egg gets broken. The egg is dropped from the 2nd floor. If the egg is not broken then anything between 3rd floor or the 4th floor is the fth floor.

So the midpoint of them is 3rd floor.If the egg is not broken on the 3rd floor, Then the fth floor should be 4th floor.

So the time complexity of binary search is logn.
