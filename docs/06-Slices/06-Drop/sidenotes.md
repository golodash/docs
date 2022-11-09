#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.Drop(arr, 5).([]int))
}
```

#! Output
```
[5 6 7 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkDrop/slice_size_10-4           47358147                51.32 ns/op
BenchmarkDrop/slice_size_100-4          37779825                53.86 ns/op
BenchmarkDrop/slice_size_1000-4         39761155                55.71 ns/op
BenchmarkDrop/slice_size_10000-4        48043132                53.38 ns/op
BenchmarkDrop/slice_size_100000-4       38701556                81.38 ns/op
```