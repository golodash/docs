#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.Pad("Test-Case", 13, "||"))
}
```

#! Output
```
||Test-Case||
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkPad/input_size_10-4            10747732               220.3 ns/op
BenchmarkPad/input_size_100-4            3500734               628.4 ns/op
BenchmarkPad/input_size_1000-4            517333              4070 ns/op
BenchmarkPad/input_size_10000-4            60566             33323 ns/op
BenchmarkPad/input_size_100000-4            5911            362017 ns/op
```