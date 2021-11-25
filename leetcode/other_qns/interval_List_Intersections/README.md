# Link
https://leetcode.com/problems/interval-list-intersections/submissions/

# Problem
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

# My explanation of the solution
While firstList not empty and secondList not empty:
    compare the elements of both List to find the interval
    0. edge case: If the pairs clearly do not have intervals ie the start of one element is bigger than the end of the other element, increment the "smaller" element
    1. start interval is the biggest start val between the 2 pairs ie. max(f_start, s_start)
    2. end interval is the smallest end val between the 2 pairs. 
        increment to the next pair for the pair with the smaller end val so we need to compare and not just find min().
    3. append [start_interval, end_interval] to the list of answers
    4. continue till while criteria fails

# Insight
My introduction to the 2 pointer coding pattern. The main challenge of this pattern is trying to find the advancement criteria. This is also a variation on the basic 2 pointer question because this involves 2 different lists.

1. Making use of max() or min()
Learnt from Darrel, Abhi. It's common to use these functions instead of comparing a > b etc.
* Use this only when you DONT care where the value comes from. In this case, the starting values of the pairs don't affect the advancement criteria. So its ok to use max()
* Not the same case for the end, because it affects the advancement criteria. We choose the smaller "end" value to be the end of the interval. Afterwards, we need to increment that to continue finding new intervals.

2. Solving edge cases (hardcoding vs understanding the issue)
- My solution resulted in a weird result when the 2 pairs being compared have no intersection at all. This would result in an interval where `itv_start` > `itv_end`. 
- I hardcoded this away by checking if this criteria happened. It works, but I wouldn't consider that a real answer. 
- Instead I needed to understand the edge case when the pair is not able to compare, and find a criteria that would allow me to skip this issue entirely hence:
```python
if f_start > s_end:
    s_ptr +=1
    continue
if s_start > f_end:
    f_ptr += 1
    continue
```
Overall, still not the most elegant. But it is an optimal solution that works.