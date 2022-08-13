#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.PadStart("Test-Case", 11, "||"))
}
```

#! Output
```
||Test-Case
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkPadStart/input_size_10-4               15442777               190.3 ns/op
BenchmarkPadStart/input_size_100-4               2896818               776.1 ns/op
BenchmarkPadStart/input_size_1000-4               438655              5824 ns/op
BenchmarkPadStart/input_size_10000-4               41041             53441 ns/op
BenchmarkPadStart/input_size_100000-4               4689            645725 ns/op
```