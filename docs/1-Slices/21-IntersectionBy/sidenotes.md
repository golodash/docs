#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func isEqual(value1, value2 interface{}) bool {
	v1 := value1.([]int)
	v2 := value2.([]int)
	same := true
	for i := 0; i < len(v1); i++ {
		if v1[i] != v2[i] {
			same = false
			break
		}
	}
	return same
}

func main() {
	arr := [][]int{{0, 1, 2}, {0, 1, 2}, {4}, {4}, {8, 9}}
	fmt.Println(slices.IntersectionBy(arr, isEqual))
}
```

#! Output
```
[0 1 2 4]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkIntersectionBy/slice_size_10-8                  9986732               225.4 ns/op
BenchmarkIntersectionBy/slice_size_100-8                  280450              8870 ns/op
BenchmarkIntersectionBy/slice_size_1000-8                  26110             87873 ns/op
BenchmarkIntersectionBy/slice_size_10000-8                  2654            887947 ns/op
BenchmarkIntersectionBy/slice_size_100000-8                  252           9177988 ns/op
```