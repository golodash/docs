---
Title: ZipBy
---


This method is like Zip except that it accepts a function to specify
how grouped values should be combined.

#- Inputs
- slice `[]anything`
- function `func(interface{}) interface{}`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `ZipBy` has a complexity of O(n).
