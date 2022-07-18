---
Title: RemoveBy
---

Removes all elements from slice that the passed function returns true on them
and returns a slice of remaining elements and a slice of removed elements.
The passed function will invoke with one argument.

#- Inputs
- slice `[]anything`
- function `funcWithanythinInputandBollOutput`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`
- second `sameTypeAsSlice`

#- Complexity
- `RemoveBy` has a complexity of O(n).
