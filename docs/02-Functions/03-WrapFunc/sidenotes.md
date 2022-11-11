#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/functions"
)

func TestFunction(first, second int) int {
	fmt.Println("running wrapped function")
	return first + second
}

func main() {
	wrappedFunction := functions.WrapFunc(TestFunction, 1, 2)
	fmt.Println(wrappedFunction())
}
```

#! Output
```
running wrapped function
[3]
```
