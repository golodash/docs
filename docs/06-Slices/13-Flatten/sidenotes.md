#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []interface{}{[]int{0}, [][]int{{1}}, [][][]int{{{2}}}, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.Flatten(arr).([]interface{}))
}
```

#! Output
```
[0 [1] [[2]] 3 4 5 6 7 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFlatten/slice_size_10-8                 2231444              1056 ns/op
BenchmarkFlatten/slice_size_100-8                 260198              9251 ns/op
BenchmarkFlatten/slice_size_1000-8                 24380             91485 ns/op
BenchmarkFlatten/slice_size_10000-8                 2622            906673 ns/op
BenchmarkFlatten/slice_size_100000-8                 248           9100311 ns/op
```