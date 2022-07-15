---
Title: Unique
---

Creates a duplicate-free version of a slice that only
keeps the first occurrence of each element.

The order of result values is determined by the order
they occur in the slice.

#- Inputs
- slice `[]anything`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlices`

#- Complexity
- `Unique` has a complexity of O(n).