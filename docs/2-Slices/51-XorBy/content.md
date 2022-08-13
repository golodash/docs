---
Title: XorBy
---

This method is like [Xor](#content-slices-xor) except that it accepts a function which is
invoked for each element of each slices for comparing them.

#- Inputs
- slice1 `[]anything`
- slice2 `[]anything`
- function `func(interface{}) interface{}`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `XorBy` has a complexity of O(n).
n = number of all elements in both 'slice1' and 'slice2'