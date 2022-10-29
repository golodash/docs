#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/generals"
)

func main() {
	fmt.Println(generals.Same([]int{1, 2, 3}, []int{1, 2, 3}))
}
```

#! Output
```
true
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/generals
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkSame/slice_size_10-4            2359940               965.5 ns/op
BenchmarkSame/slice_size_100-4            229263              9587 ns/op
BenchmarkSame/slice_size_1000-4            25977             97398 ns/op
BenchmarkSame/slice_size_10000-4            1969           1137098 ns/op
BenchmarkSame/slice_size_100000-4            246           9607156 ns/op
```