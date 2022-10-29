#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr1 := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	arr2 := []int{0, 1, 2, 3, 4, 5, 10, 11}
	fmt.Println(slices.Union(arr1, arr2).([]int))
}
```

#! Output
```
[0 1 2 3 4 5 6 7 8 9 10 11]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkUnion/input_size_10-8            812878              2905 ns/op
BenchmarkUnion/input_size_100-8           183706             13099 ns/op
BenchmarkUnion/input_size_1000-8           21643            107780 ns/op
BenchmarkUnion/input_size_10000-8           2263           1056208 ns/op
BenchmarkUnion/input_size_100000-8           219          10629537 ns/op
```