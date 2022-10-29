#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.KebabCase("Test Case"))
}
```

#! Output
```
test-case
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkKebabCase/input_size_10-4              18445420               138.7 ns/op
BenchmarkKebabCase/input_size_100-4              1968680              1124 ns/op
BenchmarkKebabCase/input_size_1000-4              224498             10739 ns/op
BenchmarkKebabCase/input_size_10000-4              21013            132266 ns/op
BenchmarkKebabCase/input_size_100000-4              2373           1022121 ns/op
```