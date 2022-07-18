#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.FlattenDeep(arr))
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
BenchmarkFlattenDeep/slice_size_10-8              617414              4224 ns/op
BenchmarkFlattenDeep/slice_size_100-8              52245             40261 ns/op
BenchmarkFlattenDeep/slice_size_1000-8              6363            373210 ns/op
BenchmarkFlattenDeep/slice_size_10000-8              573           3803052 ns/op
BenchmarkFlattenDeep/slice_size_100000-8              61          38775982 ns/op
```