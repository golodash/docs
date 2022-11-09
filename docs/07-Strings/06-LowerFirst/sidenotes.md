#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.LowerFirst("Test-Case"))
}
```

#! Output
```
test-Case
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkLowerFirst/input_size_10-4             31733970                95.71 ns/op
BenchmarkLowerFirst/input_size_100-4            12689145               182.8 ns/op
BenchmarkLowerFirst/input_size_1000-4            5299764               762.7 ns/op
BenchmarkLowerFirst/input_size_10000-4           1028904              2503 ns/op
BenchmarkLowerFirst/input_size_100000-4            86404             25815 ns/op
```