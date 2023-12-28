# Thought process
In this little file i will document any thoughts on how i try to came up with a solution.

## Parts 01 through 11
These were done before i thought i could do that. Therefore i will skip on actually giving my thought process

## Part 12
In the beginning the bruteforce approach is very fitting. We get a cartesian product of all possible replacements and we check it against the needed ratio. If it fulfills the requirement we add one to possible combination. Otherwise we go to the next one.

### P1
This part was successfully done with the approach given previously

### P2
This part deemed to be computationally impossible to solve in this way. Due to introduction of repeats (5 to be exact) the original number of possible solutions to the last line of the example went from 2^9 = 512 to 2 ^ 49 = 562_949_953_421_312

In theory this ?###???????? 3,2,1 has only 10 possible outcomes. However if we repeat it and in between we put the "?" it results in

```tsv
?###????????  ?   ?###????????    ?   ?###????????    ?   ?###????????    ?   ?###????????
```
which in turn has 506250 possible combinations. Sooo given that 
`X = ?###????????` and `f(X) = 10` then the possible combinations are as following:
```tsv
10            2   10              2   10              2   10              2   10
```
which gives us:
```python
print((10*2) ** 4 * 10)
# >>> 1_600_000
```
However we can all define that not all of these will be working so the number would be smaller than that. Nevertheless it vastly helps in reducing the number of all combinations. Comparably one would need to check.
```tsv
9             1   9               1   9               1   9               1   9
```
That gives us product of 49 different solutions
```python
print(2 ** 49)
# >>> 562_949_953_421_312
```
We can calculate the ratio in this particular case:
```python
print(562_949_953_421_312 / 1_600_000)
# >>> ~351_843_721
```

There is an edge case though... if there was
```txt
???? 1,1
.#.#
#..#
#.#.

????    ?   ????    ?   ????    ?   ????    ?   ????    1,1, 1,1, 1,1, 1,1, 1,1, (10)
3 *     2 * 3 *     2 * 3 *     2 * 3 *     2 * 3   =   3888
#.#.    #   .#.#    .   #.#.    #   .#.#    .   ....    >10
#..#    .   #.#.    #   ...#    .   #...    #   .#.#    >10
#.#.    #   ..#.    #   ..#.    #   ..#.    #   .#..    >10
```
Then one can see that without some extra signs it can still count therefore it's still missing key pieces...
So perhaps this one may help in this? That lower subsets of these might work as well (more empty ones)

## Trickle down the possibilites
Assuming the above edge case a possible solution would be to actually "trickle down" the good solutions found for each of the possibilities and replace each damaged with fixed one. Sooo the possible combinations from three

```txt
???? 1,1
.#.#
#..#
#.#.
```

Would be:
```text
.#.#
.#..
...#
....

#..#
...#
#...
....

#.#.
#...
..#.
....
```
