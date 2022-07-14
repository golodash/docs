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
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkSortedLastIndex/slice_size_10-8                 1101890              2314 ns/op
BenchmarkSortedLastIndex/slice_size_100-8                 561837              3797 ns/op
BenchmarkSortedLastIndex/slice_size_1000-8                435921              5323 ns/op
BenchmarkSortedLastIndex/slice_size_10000-8               321384              7584 ns/op
BenchmarkSortedLastIndex/slice_size_100000-8              261897              9035 ns/op
```