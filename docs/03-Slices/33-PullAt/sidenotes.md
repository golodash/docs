#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	remSlice := []int{0, 3}
	fmt.Println(slices.PullAt(arr, remSlice))
}
```

#! Output
```
[1 2 4 5 6 7 8 9] [0 3]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkPullAt/slice_size_10-8                  1038351              2187 ns/op
BenchmarkPullAt/slice_size_100-8                   95047             23444 ns/op
BenchmarkPullAt/slice_size_1000-8                   9726            245245 ns/op
BenchmarkPullAt/slice_size_10000-8                   393           5474741 ns/op
BenchmarkPullAt/slice_size_100000-8                    4         581397570 ns/op
```