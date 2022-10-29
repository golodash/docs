#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/generals"
)

func main() {
	fmt.Println(generals.Duplicate([]int{1, 2, 3}).([]int))
}
```

#! Output
```
[1 2 3]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/generals
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkDuplicate/slice_size_10-4               1548967              1494 ns/op
BenchmarkDuplicate/slice_size_100-4               238851             10067 ns/op
BenchmarkDuplicate/slice_size_1000-4               25339             93124 ns/op
BenchmarkDuplicate/slice_size_10000-4               2598            888095 ns/op
BenchmarkDuplicate/slice_size_100000-4               270           9030681 ns/op
```