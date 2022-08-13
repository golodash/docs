---
Title: TakeRightWhile
---

Creates a sub slice of a slice with elements taken from the end.
Elements are taken until passed function returns false

#- Inputs
- slice `[]anything`
- function `func(interface{}) bool`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `TakeRightWhile` has a complexity of O(n).
