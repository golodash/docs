#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.LowerCase("Test-Case"))
}
```

#! Output
```
test case
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkLowerCase/input_size_10-4              15789709               144.1 ns/op
BenchmarkLowerCase/input_size_100-4              1955625              1202 ns/op
BenchmarkLowerCase/input_size_1000-4              189141             11439 ns/op
BenchmarkLowerCase/input_size_10000-4              21609            109408 ns/op
BenchmarkLowerCase/input_size_100000-4              1872           1959692 ns/op
```