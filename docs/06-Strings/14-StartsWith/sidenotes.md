#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.StartsWith("Test Case", "test"))
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
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkStartsWith/input_size_10-4             525174032                4.201 ns/op
BenchmarkStartsWith/input_size_100-4            481693155                4.247 ns/op
BenchmarkStartsWith/input_size_1000-4           480372396                4.406 ns/op
BenchmarkStartsWith/input_size_10000-4          524829112                5.417 ns/op
BenchmarkStartsWith/input_size_100000-4         516586989                4.719 ns/op
```