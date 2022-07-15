---
Title: UnionBy
---

Returns a slice of unique values, in order, from combine of all given slices.

#- Inputs
- slice1 `[]anything`
- slice2 `[]anything`
- function `function func(interface{}) interface{}`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlices`

#- Complexity
- `UnionBy` has a complexity of O(n).
n = length of both slices combined