---
Title: Clamp
---

Clamps number within the inclusive lower and upper bounds.

#- Inputs
- number `number`
- lower `number`
- upper `number`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `number`
- A number which carries clamp of `number` between bounds and its type is type of the biggest and most detailed in size between all three inputs. example: float32, uint8, int8 = float32

#- Complexity
- `Clamp` has a complexity of O(1).
