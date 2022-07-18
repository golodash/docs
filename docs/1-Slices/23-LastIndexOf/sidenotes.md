#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.LastIndexOf(arr, 2, 6))
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
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkLastIndexOf/slice_size_10-4            32410231                76.06 ns/op
BenchmarkLastIndexOf/slice_size_100-4           26458272                83.43 ns/op
BenchmarkLastIndexOf/slice_size_1000-4          26196644                76.96 ns/op
BenchmarkLastIndexOf/slice_size_10000-4         31507578                85.79 ns/op
BenchmarkLastIndexOf/slice_size_100000-4        27467983                76.85 ns/op
```