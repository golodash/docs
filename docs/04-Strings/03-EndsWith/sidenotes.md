#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.EndsWith("Test Case", "case"))
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
BenchmarkEndsWith/input_size_10-4               455422492                5.530 ns/op
BenchmarkEndsWith/input_size_100-4              445550779                5.428 ns/op
BenchmarkEndsWith/input_size_1000-4             443639830                6.074 ns/op
BenchmarkEndsWith/input_size_10000-4            401579940                5.116 ns/op
BenchmarkEndsWith/input_size_100000-4           430197999                5.534 ns/op
```