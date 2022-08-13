---
Title: Compact
---

Removes `falsey` items from slice except values you mentioned.

Falsey items are: `{"", nil, 0, false}`

#- Inputs
- slice `[]anything`
- excepts `[]anything`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `sameTypeAsSlice`

#- Complexity
- `Compact` has a complexity of O(n).
