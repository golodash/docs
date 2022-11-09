#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.UpperFirst("test-Case"))
}
```

#! Output
```
Test-Case
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkUpperFirst/input_size_10-4             37515921                69.27 ns/op
BenchmarkUpperFirst/input_size_100-4            22407496                95.48 ns/op
BenchmarkUpperFirst/input_size_1000-4            5670046               382.4 ns/op
BenchmarkUpperFirst/input_size_10000-4            948313              3471 ns/op
BenchmarkUpperFirst/input_size_100000-4           102876             28148 ns/op
```