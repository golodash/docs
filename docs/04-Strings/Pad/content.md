---
Title: Pad
---

Pads string on the left and right sides if it's shorter than length. Padding characters are truncated if they can't be evenly divided by length.

#- Inputs
- input `string`
- length `int`
- pattern `string`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `string`

#- Complexity
- `Pad` has a complexity of O(n).
- n = (length - len(input)) / len(pattern)
