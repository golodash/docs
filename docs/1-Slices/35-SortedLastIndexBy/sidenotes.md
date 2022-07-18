#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func makeInt(input interface{}) interface{} {
	return int(input.(float64))
}

func main() {
	arr := []float64{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.SortedLastIndexBy(arr, 2.5, makeInt))
}
```

#! Output
```
3
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkSortedLastIndexBy/slice_size_10-8                544986              4331 ns/op
BenchmarkSortedLastIndexBy/slice_size_100-8               314430              7639 ns/op
BenchmarkSortedLastIndexBy/slice_size_1000-8              192150             10862 ns/op
BenchmarkSortedLastIndexBy/slice_size_10000-8             133254             15196 ns/op
BenchmarkSortedLastIndexBy/slice_size_100000-8            108862             18665 ns/op
```