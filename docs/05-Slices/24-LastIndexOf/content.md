---
Title: LastIndexOf
---


This method is like [IndexOf](#content-slices-indexof) except that it iterates over elements of
'slice' from right to left. If 'from' is negative, it's used as the offset
from the end of slice.

#- Inputs
- slice `[]anything`
- value `[]anything`
- from `int`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `int`

#- Complexity
- `LastIndexOf` has a complexity of O(n).
