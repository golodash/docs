---
Title: Random
---

Produces a random number between the inclusive 'lower' and exclusive 'upper' bounds.
If floating is true, a floating-point number is returned instead of an integer.

If floating is true, a float64 number type is returned.
If floating is false, an int64 number type is returned.

#- Inputs
- lower `number`
- upper `number`
- floating `bool`

**Note**: Passing invalid input causes panic.

#- Outputs
- first `number`

#- Complexity
- `Random` has a complexity of O(1).
