#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	numbers := []int{1, 2, 3}
	fmt.Println(slices.Sum(numbers))
}
```

#! Output
```
6
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkSum/slice_size_10-4             3519469               976.9 ns/op
BenchmarkSum/slice_size_100-4             150198             13505 ns/op
BenchmarkSum/slice_size_1000-4             26662             95260 ns/op
BenchmarkSum/slice_size_10000-4             3566            826375 ns/op
BenchmarkSum/slice_size_100000-4             361           6540329 ns/op
```