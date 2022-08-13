---
Title: Truncate
---

Truncates string if it's longer than the given maximum string length. The last characters of the truncated string are replaced with the omission string.

#- Inputs
- input `string`
- length `int`
- separators `[]rune`
- omission `string`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `string`

#- Complexity
- `Truncate` has a complexity of O(n).
