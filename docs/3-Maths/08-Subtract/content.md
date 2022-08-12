---
Title: Subtract
---

Subtracts two numbers.

#- Inputs
- number1 `interface{}`
- Has to be a number, does not matter what type.
- number2 `interface{}`
- Has to be a number, does not matter what type.

**Note**: Passing invalid input causes panic.

#- Outputs
- first `interface{}`
- A number which carries result of `number1-number2` and its type is type of the biggest and most detailed in size between types of `number1` and `number2` inputs. example: float32 - int = float32

#- Complexity
- `Subtract` has a complexity of O(1).
