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
4
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkSortedIndexOf/slice_size_10-4            793162              3110 ns/op
BenchmarkSortedIndexOf/slice_size_100-4           459834              5949 ns/op
BenchmarkSortedIndexOf/slice_size_1000-4          356412              6745 ns/op
BenchmarkSortedIndexOf/slice_size_10000-4         222387             10528 ns/op
BenchmarkSortedIndexOf/slice_size_100000-4        207924             14785 ns/op
```