#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.Last(arr).(int))
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
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkLatest/slice_size_10-4                 126150567               21.03 ns/op
BenchmarkLatest/slice_size_100-4                100000000               22.22 ns/op
BenchmarkLatest/slice_size_1000-4               125681389               19.42 ns/op
BenchmarkLatest/slice_size_10000-4              127610109               18.98 ns/op
BenchmarkLatest/slice_size_100000-4             117456176               18.77 ns/op
```