#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func returnSameValue(input interface{}) interface{} {
	return input.(int)
}

func main() {
	arr := []int{0, 0, 0, 1, 1, 2, 3, 4, 5, 5}
	fmt.Println(slices.SortedUniqueBy(arr, returnSameValue))
}
```

#! Output
```
[0 1 2 3 4 5]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkSortedUniqueBy/input_size_10-4                  1348014              2017 ns/op
BenchmarkSortedUniqueBy/input_size_100-4                   81312             27153 ns/op
BenchmarkSortedUniqueBy/input_size_1000-4                   7152            393312 ns/op
BenchmarkSortedUniqueBy/input_size_10000-4                   591           6788050 ns/op
BenchmarkSortedUniqueBy/input_size_100000-4                   39          61417030 ns/op
```