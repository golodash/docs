#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.Slice(arr, 3, 6))
}
```

#! Output
```
[3 4 5]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkSlice/input_size_10-4          42698826                53.97 ns/op
BenchmarkSlice/input_size_100-4         42331191                56.38 ns/op
BenchmarkSlice/input_size_1000-4        36713923                60.30 ns/op
BenchmarkSlice/input_size_10000-4       44077087                79.81 ns/op
BenchmarkSlice/input_size_100000-4      28067534                87.30 ns/op
```