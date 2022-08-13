---
Title: SortedUniqueBy
---

This method is like [UniqueBy](#content-slices-uniqueby) except that it's designed and optimized
for sorted slices.

It accepts a function which is invoked for each element in slice to
generate the criterion by which uniqueness is computed.

#- Inputs
- slice `[]anything`
- function `func(interface{}) interface{}`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `SortedUniqueBy` has a complexity of O(n).
