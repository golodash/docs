#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/functions"
)

func TestFunction(first, second int) int {
	fmt.Println("running just once")
	return first + second
}

func main() {
	wrappedFunctions := functions.WrapFunc(TestFunction, 3, 4)
	one := functions.Once(wrappedFunctions)
	fmt.Println(one())
	fmt.Println(one())
	fmt.Println(one())
	fmt.Println(one())
}
```

#! Output
```
running just once
[7]
[7]
[7]
[7]
```
