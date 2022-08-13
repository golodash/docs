---
Title: MeanBy
---

This method is like [Mean](#content-slices-mean) except that it accepts a function which is invoked for each element in slice to generate the value to be averaged.

#- Inputs
- slice `[]anything`
- function `func(interface{}) interface{}`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `float64`

#- Complexity
- `MeanBy` has a complexity of O(n).
