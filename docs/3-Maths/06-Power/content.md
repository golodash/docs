---
Title: Power
---

Returns input to the power of number.

#- Inputs
- input `interface{}`
- Has to be a number, does not matter what type.
- number `int`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `interface{}`
- A number which carries result of `input^number` and its type is type of the biggest and most detailed in size between types of `input` and `number` inputs. example: float32 ^ int = float32

#- Complexity
- `Power` has a complexity of O(number).
