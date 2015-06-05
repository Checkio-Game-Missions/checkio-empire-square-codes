The glowing line image is a grid of numbered dots.
The grid is comprised of a square shaped array of dots and contains lines
that connect some pairs of adjacent dots.
The answer to the code is the number of squares that are formed by these lines.
For example, in the figure shown below, there are 3 squares: 2 small squares and 1 medium square.</p>


```
 1---2   3---4
 |   |       |
 5---6---7---8
     |   |   |
 9  10--11  12
     |       |
13  14--15--16

3 Squares -- 1-6, 6-11, 6-16
```

```
 1---2---3---4
 |           |
 5   6---7   8
 |   |   |   |
 9  10--11  12
 |           |
13--14--15--16

2 Squares -- 1-16, 6-11
```

The dots are marked by the numbers 1 through 16.
The endpoints of the lines are represented by lists of two numbers.
