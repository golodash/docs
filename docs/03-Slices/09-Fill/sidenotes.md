#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.Fill(arr, 0, 0, 5).([]int))
}
```

#! Output
```
[0 0 0 0 0 5 6 7 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkFill/slice_size_10-4            9085520               236.6 ns/op
BenchmarkFill/slice_size_100-4           2167212              1071 ns/op
BenchmarkFill/slice_size_1000-4           246256              9651 ns/op
BenchmarkFill/slice_size_10000-4           25684             92565 ns/op
BenchmarkFill/slice_size_100000-4           1968           1382148 ns/op
```