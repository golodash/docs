---
Title: Intersection
---


Creates a slice of unique values that are included in all given slices for equality comparisons. The order and references of result values are determined by the first slice.

#- Inputs
- slices `[][]anything`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `[]slicesElementType`

#- Complexity
- `Intersection` has a complexity of O(n).
