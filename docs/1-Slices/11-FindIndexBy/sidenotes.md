#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func isEqual(value interface{}) bool {
	return value.(int) == 5
}

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.FindIndexBy(arr, isEqual))
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
BenchmarkFindIndexBy/slice_size_10-8            10307150               216.7 ns/op
BenchmarkFindIndexBy/slice_size_100-8           10656043               215.3 ns/op
BenchmarkFindIndexBy/slice_size_1000-8          10572000               217.1 ns/op
BenchmarkFindIndexBy/slice_size_10000-8         10415377               215.6 ns/op
BenchmarkFindIndexBy/slice_size_100000-8        10584814               217.2 ns/op
```