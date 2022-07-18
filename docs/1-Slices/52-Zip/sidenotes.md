#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := [][]int{{1, 2}, {3, 4}, {5, 6}, {7, 8}}
	fmt.Println(slices.Zip(arr))
}
```

#! Output
```
[[1 3 5 7] [2 4 6 8]]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkZip/input_size_10-8              246796              9279 ns/op
BenchmarkZip/input_size_100-8              60002             34387 ns/op
BenchmarkZip/input_size_1000-8              8650            262881 ns/op
BenchmarkZip/input_size_10000-8              853           2529777 ns/op
BenchmarkZip/input_size_100000-8              86          29234703 ns/op
```