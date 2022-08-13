#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.TakeRight(arr, 3).([]int))
}
```

#! Output
```
[7 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkTakeRight/input_size_10-8              42589473                56.00 ns/op
BenchmarkTakeRight/input_size_100-8             42422679                55.62 ns/op
BenchmarkTakeRight/input_size_1000-8            42695554                55.88 ns/op
BenchmarkTakeRight/input_size_10000-8           42712028                55.92 ns/op
BenchmarkTakeRight/input_size_100000-8          38658364                55.96 ns/op
```