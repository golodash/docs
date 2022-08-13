---
Title: IntersectionBy
---


This method is like [Intersection](#content-slices-intersection) except that it accepts a function comparator which is invoked to compare elements of 'slices'. The order and references of result values are determined by the first slice. The 'function' is invoked with two arguments: (slice1, slice2).

#- Inputs
- slices `[][]anything`
- function `func(interface{}, interface{}) bool`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `[]slicesElementType`

#- Complexity
- `IntersectionBy` has a complexity of O(n*log(n)).
