---
Title: UniqueBy
---

Creates a duplicate-free version of a slice that only
keeps the first occurrence of each element.

The order of result values is determined by the order
they occur in the slice.

#- Inputs
- slice `[]anything`
- function `func(interface{}) interface{}`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `UniqueBy` has a complexity of O(n).