---
Title: SortedIndexBy
---

This method is like [SortedIndex](#content-slices-sortedindex) except that it accepts a 'function' which is invoked for value and each element of slice to compute their sort ranking. The function is invoked with one argument: (value).

#- Inputs
- slice `[]anything`
- value `anything`
- function `func(interface{}) interface{}`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `int`

#- Complexity
- `SortedIndexBy` has a complexity of O(log(n)).
