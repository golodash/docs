#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.Join(arr, "-"))
}
```

#! Output
```
0-1-2-3-4-5-6-7-8-9
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkJoin/input_size_10-8            1581897              1532 ns/op
BenchmarkJoin/input_size_100-8            130808             15440 ns/op
BenchmarkJoin/input_size_1000-8             9249            248230 ns/op
BenchmarkJoin/input_size_10000-8             225          10256914 ns/op
BenchmarkJoin/input_size_100000-8              3         826928085 ns/op
```