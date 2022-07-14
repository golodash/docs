#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)


func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.SortedIndex(arr, 5))
}

```

#! Output
```
5
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkSortedIndex/slice_size_10-8              843955              2752 ns/op
BenchmarkSortedIndex/slice_size_100-8             532975              4469 ns/op
BenchmarkSortedIndex/slice_size_1000-8            387897              6287 ns/op
BenchmarkSortedIndex/slice_size_10000-8           245674              8405 ns/op
BenchmarkSortedIndex/slice_size_100000-8          242020              9808 ns/op
```