#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.DropRight(arr, 5).([]int))
}
```

#! Output
```
[0 1 2 3 4]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkDropRight/slice_size_10-4              45264411                58.69 ns/op
BenchmarkDropRight/slice_size_100-4             44810901                55.79 ns/op
BenchmarkDropRight/slice_size_1000-4            39948584                51.91 ns/op
BenchmarkDropRight/slice_size_10000-4           46059705                71.10 ns/op
BenchmarkDropRight/slice_size_100000-4          40177173                58.69 ns/op
```