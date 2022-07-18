#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.FlattenDepth(arr, 1))
}
```

#! Output
```
[0 1 2 3 4 5 6 7 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFlattenDepth/slice_size_10-8             635437              3686 ns/op
BenchmarkFlattenDepth/slice_size_100-8             62772             37297 ns/op
BenchmarkFlattenDepth/slice_size_1000-8             6214            363569 ns/op
BenchmarkFlattenDepth/slice_size_10000-8             655           3541826 ns/op
BenchmarkFlattenDepth/slice_size_100000-8             66          36196918 ns/op
```