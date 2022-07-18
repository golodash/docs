---
Title: SortedIndex
---

Uses a binary search to determine the lowest index at which value should be
inserted into slice in order to maintain its sort order

#- Inputs
- slice `[]anything`
- value `anything`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `int`

#- Complexity
- `SortedIndex` has a complexity of O(log(n)).
