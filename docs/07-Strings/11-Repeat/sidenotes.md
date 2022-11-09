#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.Repeat("_-", 3))
}
```

#! Output
```
_-_-_-
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkRepeat/input_size_10-4                 16046761               126.0 ns/op
BenchmarkRepeat/input_size_100-4                  655422              4182 ns/op
BenchmarkRepeat/input_size_1000-4                  10305            212063 ns/op
BenchmarkRepeat/input_size_10000-4                   133          17047021 ns/op
```