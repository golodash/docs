#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	numbers := []int{1, 2, 3}
	fmt.Println(slices.Min(numbers).(int))
}
```

#! Output
```
1
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkMax/slice_size_10-4             1814184              1263 ns/op
BenchmarkMax/slice_size_100-4             193148             16060 ns/op
BenchmarkMax/slice_size_1000-4             18014            121737 ns/op
BenchmarkMax/slice_size_10000-4             1816           1720484 ns/op
BenchmarkMax/slice_size_100000-4              90          24887254 ns/op
```