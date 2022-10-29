#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.Initial(arr).([]int))
}
```

#! Output
```
[0 1 2 3 4 5 6 7 8]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkInitial/slice_size_10-8                49310410                48.25 ns/op
BenchmarkInitial/slice_size_100-8               49644171                47.97 ns/op
BenchmarkInitial/slice_size_1000-8              49418430                48.39 ns/op
BenchmarkInitial/slice_size_10000-8             a48584812               48.67 ns/op
BenchmarkInitial/slice_size_100000-8            48989869                48.48 ns/op
```