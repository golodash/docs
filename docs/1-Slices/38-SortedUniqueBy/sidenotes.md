#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)


func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.SortedUnique(arr))
}

```

#! Output
```
[0 1 2 3 4 5 6 7 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkSortedUniqueBy/input_size_10-8                  1475721              1559 ns/op
BenchmarkSortedUniqueBy/input_size_100-8                   95887             22138 ns/op
BenchmarkSortedUniqueBy/input_size_1000-8                   9766            248835 ns/op
BenchmarkSortedUniqueBy/input_size_10000-8                   835           2412745 ns/op
BenchmarkSortedUniqueBy/input_size_100000-8                   92          26679660 ns/op
```