---
Title: WrapFunc
---

Returns a function that invokes `function`, with passed `inputs` arguments.

#- Inputs
- function `interface{}`
- inputs `...interface{}`

#- Outputs
- first `func() []interface{}`

#- Complexity
- `WrapFunc` has a complexity of O(n).
- n = length of `inputs`, it is technically O(1).
