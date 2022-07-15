---
Title: ZipMap
---

This method is like FromPairs except that it accepts two slices, one of propert
identifiers and one of corresponding values.

#- Inputs
- slice `[]anything`
- values `func(interface{}) interface{}`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `map`

#- Complexity
- `ZipMap` has a complexity of O(n).
