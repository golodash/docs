#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	numbers := []int{1, 2, 3}
	fmt.Println(slices.Mean(numbers))
}
```

#! Output
```
2
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkMean/slice_size_10-4            3513686               667.1 ns/op
BenchmarkMean/slice_size_100-4            347628              6714 ns/op
BenchmarkMean/slice_size_1000-4            32551             82608 ns/op
BenchmarkMean/slice_size_10000-4            3951            666946 ns/op
BenchmarkMean/slice_size_100000-4            351           8283905 ns/op
```