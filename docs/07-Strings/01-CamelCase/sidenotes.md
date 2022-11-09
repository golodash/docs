#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.CamelCase("Test Case"))
}
```

#! Output
```
testCase
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkCamelCase/input_size_10-4              23181925                91.93 ns/op
BenchmarkCamelCase/input_size_100-4              4508040               518.8 ns/op
BenchmarkCamelCase/input_size_1000-4              502591              4779 ns/op
BenchmarkCamelCase/input_size_10000-4              49544             45674 ns/op
BenchmarkCamelCase/input_size_100000-4              4416            466709 ns/op
```