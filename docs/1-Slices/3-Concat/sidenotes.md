#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5}
	values := []int{6, 7, 8, 9}
	fmt.Println(slices.Concat(arr, values).([]int))
}
```

#! Output
```
[1 2 3 4 5 6 7 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkConcat/slice_size_10-4                  1752954              1373 ns/op
BenchmarkConcat/slice_size_100-4                  172347             11978 ns/op
BenchmarkConcat/slice_size_1000-4                  19111            108830 ns/op
BenchmarkConcat/slice_size_10000-4                  2148           1204137 ns/op
BenchmarkConcat/slice_size_100000-4                  207          21197693 ns/op
```