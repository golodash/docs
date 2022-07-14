---
Title: DropBy
---

Creates a new slice from the passed slice and removes elements from it when passed function returns true on that element.

#- Inputs
- slice `[]anything`
- function `func(interface{}) bool`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `DropBy` has a complexity of O(n).
