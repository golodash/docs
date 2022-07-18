#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.SortedIndexOf(arr, 3))
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
BenchmarkSortedIndexOf/slice_size_10-8            876394              2896 ns/op
BenchmarkSortedIndexOf/slice_size_100-8           488282              4752 ns/op
BenchmarkSortedIndexOf/slice_size_1000-8          366484              6610 ns/op
BenchmarkSortedIndexOf/slice_size_10000-8         270328              8639 ns/op
BenchmarkSortedIndexOf/slice_size_100000-8        203395             10544 ns/op
```