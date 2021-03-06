#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.SortedUnique(arr))
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
BenchmarkSortedUnique/input_size_10-8            1138270              2057 ns/op
BenchmarkSortedUnique/input_size_100-8            363392              6568 ns/op
BenchmarkSortedUnique/input_size_1000-8            43142             49021 ns/op
BenchmarkSortedUnique/input_size_10000-8            5100            470954 ns/op
BenchmarkSortedUnique/input_size_100000-8            458           4606857 ns/op
```