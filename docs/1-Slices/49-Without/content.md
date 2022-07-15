---
Title: Without
---

Returns a slice of 'slice' elements that are not included in the
other given slice using equality comparisons.

#- Inputs
- slice `[]anything`
- notIncluded `[]anything`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `Without` has a complexity of O(n*m).
n = length of 'slice'
m = length of 'notIncluded'