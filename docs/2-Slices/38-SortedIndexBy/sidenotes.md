#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func returnSameValue(input interface{}) interface{} {
	return input.(float64)
}

func main() {
	arr := []float64{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.SortedIndexBy(arr, 1.4, returnSameValue))
}
```

#! Output
```
2
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkSortedIndexBy/slice_size_10-8            557904              4281 ns/op
BenchmarkSortedIndexBy/slice_size_100-8           290359              7537 ns/op
BenchmarkSortedIndexBy/slice_size_1000-8          195153             10858 ns/op
BenchmarkSortedIndexBy/slice_size_10000-8         131415             15262 ns/op
BenchmarkSortedIndexBy/slice_size_100000-8        120562             18753 ns/op
```