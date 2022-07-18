---
Title: TakeWhile
---

Creates a sub slice of a slice with elements taken from the beginning.
Elements are taken until passed function returns false.

#- Inputs
- slice `[]anything`
- finction `func(interface{}) bool`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `TakeWhile` has a complexity of O(n).
n = number of elements that passed function returns true on them