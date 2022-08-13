---
Title: Unzip
---


This method is like [Zip](#content-slices-zip) except that it accepts a slice of grouped elements
and creates a slice regrouping the elements to their pre-zip configuration.

#- Inputs
- slice `[][]anything`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `Unzip` has a complexity of O(n).