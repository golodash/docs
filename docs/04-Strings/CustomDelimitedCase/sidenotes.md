#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.CustomDelimitedCase("test case is here", '-', "", true))
}
```

#! Output
```
TEST-CASE-IS-HERE
```