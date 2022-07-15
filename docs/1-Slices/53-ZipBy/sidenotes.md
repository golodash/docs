#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func makeInt(input interface{}) interface{} {
	return int(input.(int))
}

func main() {
	arr := [][]int{{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}}
	fmt.Println(slices.ZipBy(arr, makeInt))
}

```

#! Output
```

```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkZipBy/slice_size_10-8            666265              3636 ns/op
BenchmarkZipBy/slice_size_100-8           119318             19204 ns/op
BenchmarkZipBy/slice_size_1000-8           15674            159563 ns/op
BenchmarkZipBy/slice_size_10000-8           1654           1524024 ns/op
BenchmarkZipBy/slice_size_100000-8           156          14639071 ns/op
```