---
Title: IntersectionBy
---


This method is like Intersection except that it accepts comparator which is
invoked to compare elements of 'slices'. The order and references of result
values are determined by the first slice. The comparator is invoked with
two arguments: (slice1, slice2).

#- Inputs
- slice `[]anything`
- function `funcWithTwoAnythingInputandBoolOutput`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `IntersectionBy` has a complexity of O(n*log(n)).
