---
Title: SumBy
---

This method is like [Sum](#content-slices-sum) except that it accepts a function which is invoked for each element in slice to generate the value to be summed.

#- Inputs
- slice `[]numbers`
- function `func(interface{}) interface{}`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSliceElement`

#- Complexity
- `SumBy` has a complexity of O(n).
