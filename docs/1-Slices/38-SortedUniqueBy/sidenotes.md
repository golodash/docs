#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 0, 0, 1, 1, 2, 3, 4, 5, 5}
	fmt.Println(slices.SortedUnique(arr))
}
```

#! Output
```
[0 1 2 3 4 5]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkSortedUnique/input_size_10-4            1043737              2333 ns/op
BenchmarkSortedUnique/input_size_100-4            340372              6989 ns/op
BenchmarkSortedUnique/input_size_1000-4            43672             53851 ns/op
BenchmarkSortedUnique/input_size_10000-4            3540            647702 ns/op
BenchmarkSortedUnique/input_size_100000-4            354           7361202 ns/op
```