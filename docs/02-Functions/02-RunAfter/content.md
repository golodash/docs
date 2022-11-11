---
Title: RunAfter
---

Returns an interface with two methods. one called Run which executes the function and other one
called Cancel which cancels executing of current executed Run function.

You can use [WrapFunc](#content-functions-wrapfunction) to generate `function`.

#- Inputs
- function `func() []interface{}`
- wait `time.Duration`
- parallel `bool`

#- Outputs
- first `runCancel`
- runCancel has two function:
  - `Run` which returns `[]interface{}`, they are outputs of running the function, if `parallel` is **true**, returns **nil**
  - `Cancel` which returns (`bool`, `error`)

- `Cancel` can happen if main function didn't start and still is waiting and `parallel` is **true**.

#- Complexity
- `RunAfter` has a complexity of O(1).
