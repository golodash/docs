#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func compare(value1, value2 interface{}) bool {
	return value1.(int) == value2.(int)
}

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	values := []int{0, 1, 2}
	fmt.Println(slices.DifferenceBy(arr, values, compare).([]int))
}
```

#! Output
```
[3 4 5 6 7 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkDifferenceBy/slice_size_10-4             538833              4789 ns/op
BenchmarkDifferenceBy/slice_size_100-4             51003             54536 ns/op
BenchmarkDifferenceBy/slice_size_1000-4             5197            428041 ns/op
BenchmarkDifferenceBy/slice_size_10000-4             504           4613594 ns/op
BenchmarkDifferenceBy/slice_size_100000-4             49          59129673 ns/op
```