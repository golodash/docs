---
Title: Pull
---


Removes all given values from slice.

#- Inputs
- slice `[]anything`
- values `[]anything`


**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `Pull` has a complexity of O(n*m).
n = length of 'slice'
m = length of 'values'