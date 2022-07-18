#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.Nth(arr, 3))
}
```

#! Output
```
3
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkNth/input_size_10-8            131498138               17.76 ns/op
BenchmarkNth/input_size_100-8           133639078               17.81 ns/op
BenchmarkNth/input_size_1000-8          134501211               17.76 ns/op
BenchmarkNth/input_size_10000-8         135755653               17.66 ns/op
BenchmarkNth/input_size_100000-8        135227160               17.92 ns/op
```