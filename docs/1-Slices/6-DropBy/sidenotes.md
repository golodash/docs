#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func dropOrNot(input interface{}) bool {
	return input.(int)%2 == 0
}

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.DropBy(arr, dropOrNot).([]int))
}
```

#! Output
```
[1 3 5 7 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkDropBy/slice_size_10-4                  7113940               334.7 ns/op
BenchmarkDropBy/slice_size_100-4                  743323              3157 ns/op
BenchmarkDropBy/slice_size_1000-4                  76142             36792 ns/op
BenchmarkDropBy/slice_size_10000-4                  7795            299942 ns/op
BenchmarkDropBy/slice_size_100000-4                  776           3603703 ns/op
```