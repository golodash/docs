#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.Head(arr))
}

```

#! Output
```
0
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkHead/slice_size_10-8           131572886               18.08 ns/op
BenchmarkHead/slice_size_100-8          136606566               16.99 ns/op
BenchmarkHead/slice_size_1000-8         137233167               17.58 ns/op
BenchmarkHead/slice_size_10000-8        145114666               17.07 ns/op
BenchmarkHead/slice_size_100000-8       141873880               16.43 ns/op
```