---
Title: CustomDelimitedCase
---

CustomDelimitedCase converts a string to SCREAMING.DELIMITED.SNAKE.CASE if 'delimiter' equals to '.' and 'screaming' equals to true or to delimited.snake.case if 'delimiter' equals to '.' and screaming equals to false.

'ignore' variable is what you want the function to ignore and do not change.

#- Inputs
- input `string`
- delimiter `uint8`
- ignore `string`
- screaming `string`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `string`

#- Complexity
- `CustomDelimitedCase` has a complexity of O(n).
