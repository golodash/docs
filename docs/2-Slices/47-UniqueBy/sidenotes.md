#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func makeInt(input interface{}) interface{} {
	return int(input.(float64))
}

func main() {
	arr := []float64{0, 1, 2, 3, 3, 4, 7, 9, 5, 6, 7, 8, 9}
	fmt.Println(slices.UniqueBy(arr, makeInt))
}
```

#! Output
```
[0 1 2 3 4 7 9 5 6 8]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkUniqueBy/input_size_10-8               2741020               817.2 ns/op
BenchmarkUniqueBy/input_size_100-8               404720              5773 ns/op
BenchmarkUniqueBy/input_size_1000-8               37808             58157 ns/op
BenchmarkUniqueBy/input_size_10000-8               4252            511183 ns/op
BenchmarkUniqueBy/input_size_100000-8               424           5355624 ns/op
```