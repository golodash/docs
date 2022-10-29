---
Title: PadStart
---

Pads string on the left side if it's shorter than length. Padding characters are truncated if they exceed length.

#- Inputs
- input `string`
- length `int`
- pattern `string`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `string`

#- Complexity
- `PadStart` has a complexity of O(n).
- n = (length - len(input)) / len(pattern)
