---
Title: Fill
---

Fills a slice with a value from `start` up to but not including `end`.

#- Inputs
- slice `[]anything`
- value `anything`
- start `int`
- end `int`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `Fill` has a complexity of O(n).

n = end - start
