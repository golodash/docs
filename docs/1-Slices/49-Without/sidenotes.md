#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	notIncluded := []int{4, 5, 6, 7}
	fmt.Println(slices.Without(arr, notIncluded))
}

```

#! Output
```
[0 1 2 3 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkDifference/slice_size_10-8               473758              5010 ns/op
BenchmarkDifference/slice_size_100-8               44064             49032 ns/op
BenchmarkDifference/slice_size_1000-8               4740            495063 ns/op
BenchmarkDifference/slice_size_10000-8               441           5073114 ns/op
BenchmarkDifference/slice_size_100000-8               43          49647734 ns/op
```