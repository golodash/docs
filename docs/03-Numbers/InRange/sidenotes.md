#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/numbers"
)

func main() {
	fmt.Println(numbers.InRange(2.1, 1, 2))
}
```

#! Output
```
false
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/numbers
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkInRange-4      24233912               102.5 ns/op
```