#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.FindIndex(arr, 6))
}
```

#! Output
```
6
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkFindIndex/slice_size_10-4               3924547               657.4 ns/op
BenchmarkFindIndex/slice_size_100-4               345916              6775 ns/op
BenchmarkFindIndex/slice_size_1000-4               39697             60621 ns/op
BenchmarkFindIndex/slice_size_10000-4               4047            629993 ns/op
BenchmarkFindIndex/slice_size_100000-4               348           6322763 ns/op
```