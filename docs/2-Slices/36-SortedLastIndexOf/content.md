---
Title: SortedLastIndexOf
---

This method is like [LastIndexOf](#content-slices-lastindexof) except that it performs a
binary search on a sorted slice

#- Inputs
- slice `[]anything`
- value `anything`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `int`

#- Complexity
- `SortedLastIndexOf` has a complexity of O(log(n)).
