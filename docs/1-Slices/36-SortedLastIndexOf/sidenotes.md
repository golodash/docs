#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.SortedLastIndexOf(arr, 2))
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
BenchmarkSortedLastIndexOf/slice_size_10-8                894435              2735 ns/op
BenchmarkSortedLastIndexOf/slice_size_100-8               534220              4257 ns/op
BenchmarkSortedLastIndexOf/slice_size_1000-8              408559              5877 ns/op
BenchmarkSortedLastIndexOf/slice_size_10000-8             285562              9053 ns/op
BenchmarkSortedLastIndexOf/slice_size_100000-8            184581             11110 ns/op
```