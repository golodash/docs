---
Title: SortedIndexOf
---

This method is like [IndexOf](#content-slices-indexof) except that it performs a binary search on a sorted slice.

#- Inputs
- slice `[]anything`
- value `anything`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `int`

#- Complexity
- `SortedIndexOf` has a complexity of O(log(n)).
