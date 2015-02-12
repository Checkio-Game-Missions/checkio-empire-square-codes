We have thought up tricky recognizing system friend/foe for our crafts, when they land.
On the landing pad glowing lines appear and pilot should answer how many square he counted.


The glowing line image is a grid of numbered dots.
The grid is comprised of a square shaped array of dots and contains lines
that connect some pairs of adjacent dots.
The answer to the code is the number of squares that are formed by these lines.
For example, in the figure shown below, there are 3 squares: 2 small squares and 1 medium square.</p>

![Squares](squares-chest.png)

The dots are marked by the numbers 1 through 16.
The endpoints of the lines are represented by lists of two numbers.

**Input:** A list of lines as a list of list. Each list consists of the two integers. 

**Output:** The quantity of squares formed as an integer.

**Example:**

```python
count_squares([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
 [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
 [10, 14], [12, 16], [14, 15], [15, 16]]) == 3
count_squares([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
 [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
 [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2
```
**How it is used:**

This is a simple puzzle that illustrates pattern searching.
For complex cases you can improve your program and use it to search for more complex patterns, shapes and objects.

**Precondition:**
```python
???
```
