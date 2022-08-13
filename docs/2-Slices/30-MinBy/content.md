---
Title: MinBy
---

This method is like [Min](#content-slices-min) except that it accepts a function which is invoked for each element in slice to return a number for comparison.

#- Inputs
- slice `[]anything`
- function `func(interface{}) interface{}`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSliceElement`

#- Complexity
- `MinBy` has a complexity of O(n).
