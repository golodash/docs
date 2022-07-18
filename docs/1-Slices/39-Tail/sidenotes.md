#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []float64{0.1, 1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.9}
	fmt.Println(slices.Tail(arr))
}
```

#! Output
```
[1.2 2.3 3.4 4.5 5.6 6.7 7.8 8.9 9.9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkTail/slice_size_10-8           50808295                50.51 ns/op
BenchmarkTail/slice_size_100-8          42129543                48.66 ns/op
BenchmarkTail/slice_size_1000-8         50119210                46.95 ns/op
BenchmarkTail/slice_size_10000-8        49919943                46.75 ns/op
BenchmarkTail/slice_size_100000-8       50864626                46.34 ns/op
```