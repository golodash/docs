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
9
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkLastIndexOf/slice_size_10-4            32547106                77.40 ns/op
BenchmarkLastIndexOf/slice_size_100-4           29125891                79.99 ns/op
BenchmarkLastIndexOf/slice_size_1000-4          25449651                88.73 ns/op
BenchmarkLastIndexOf/slice_size_10000-4         27468854                90.20 ns/op
BenchmarkLastIndexOf/slice_size_100000-4        19642573               113.5 ns/op
```