#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)


func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.LastIndexOf(arr, 2, 6))
}

```

#! Output
```
9
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkLastIndexOf/slice_size_10-8            32647378                72.78 ns/op
BenchmarkLastIndexOf/slice_size_100-8           28089960                75.73 ns/op
BenchmarkLastIndexOf/slice_size_1000-8          27191648                75.07 ns/op
BenchmarkLastIndexOf/slice_size_10000-8         31362648                73.07 ns/op
BenchmarkLastIndexOf/slice_size_100000-8        34623212                68.36 ns/op
BenchmarkSortedLastIndexOf/slice_size_10-8        750374              2876 ns/op
BenchmarkSortedLastIndexOf/slice_size_100-8       519843              4623 ns/op
BenchmarkSortedLastIndexOf/slice_size_1000-8      359866              6723 ns/op
BenchmarkSortedLastIndexOf/slice_size_10000-8             261360              9189 ns/op
BenchmarkSortedLastIndexOf/slice_size_100000-8            181812             11408 ns/op
```