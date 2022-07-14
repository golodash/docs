#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	values := []int{0, 2, 4, 6, 8}
	fmt.Println(slices.Difference(arr, values).([]int))
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
BenchmarkDifference/slice_size_10-4               512715              4721 ns/op
BenchmarkDifference/slice_size_100-4               27476             84766 ns/op
BenchmarkDifference/slice_size_1000-4               4910            597633 ns/op
BenchmarkDifference/slice_size_10000-4               421           6182947 ns/op
BenchmarkDifference/slice_size_100000-4               50          61383962 ns/op
```