---
Title: IndexOf
---

Gets the index at which the first occurrence of value is found in slice
with equality comparisons. If 'from' is negative, it's used as the offset
from the end of slice

#- Inputs
- slice `[]anything`
- value `anything`
- from `int`  

**Note**: Passing invalid input causes panic.

#- Outputs
- first `int`

#- Complexity
- `IndexOf` has a complexity of O(n).
