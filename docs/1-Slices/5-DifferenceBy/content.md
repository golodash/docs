---
Title: DifferenceBy
---

This method is like [difference](#content-slices-difference) except that it accepts a custom function which is invoked to compare elements of `slice` to `notIncluded` slice.

#- Inputs
- slice `[]anything`
- notIncluded `[]anything`
- function `func(interface{}, interface{}) bool`

The `function` takes one element from `slice` variable and one element from `notIncluded` variable and returns true if both of them are the same value and the value will get removed from function's output.

**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `DifferenceBy` has a complexity of O(n*m).

n = length of `slice`

m = length of `notIncluded`
