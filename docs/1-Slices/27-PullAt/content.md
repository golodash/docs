---
Title: PullAt
---

Removes elements from slice corresponding to indexes and returns a slice of
remaining elements and removed elements.

**Note**: Duplicate key numbers in 'remSlice' variable will get removed

#- Inputs
- slice `[]anything`
- remSlice `sliceOfInt`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`
- second `sameTypeAsSlice`

#- Complexity
- `PullAt` has a complexity of O(n*log(n)).
This complexity is mainly because of sorting 'remSlice'.
Keep it sorted to have a better complexity of:
Best-Case Complexity: O(n)