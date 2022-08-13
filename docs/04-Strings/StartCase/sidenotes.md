#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.StartCase("test-case"))
}
```

#! Output
```
Test Case
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkStartCase/input_size_10-4              12891734               185.9 ns/op
BenchmarkStartCase/input_size_100-4              1701066              1359 ns/op
BenchmarkStartCase/input_size_1000-4              184456             13289 ns/op
BenchmarkStartCase/input_size_10000-4              18080            153891 ns/op
BenchmarkStartCase/input_size_100000-4              1060           2618749 ns/op
```