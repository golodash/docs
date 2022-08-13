---
Title: Xor
---

Returns a slice of unique values that is the symmetric difference of the given slices.

#- Inputs
- slice1 `[]anything`
- slice2 `[]anything`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `Xor` has a complexity of O(n).
n = number of all elements in both 'slice1' and 'slice2'