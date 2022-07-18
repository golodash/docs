#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.IndexOf(arr, 4, 0))
}
```

#! Output
```
4
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkIndexOf/slice_size_10-4                 3337179               633.3 ns/op
BenchmarkIndexOf/slice_size_100-4                 486624              5249 ns/op
BenchmarkIndexOf/slice_size_1000-4                 44820             52220 ns/op
BenchmarkIndexOf/slice_size_10000-4                 2884            773229 ns/op
BenchmarkIndexOf/slice_size_100000-4                 470           4812985 ns/op
```