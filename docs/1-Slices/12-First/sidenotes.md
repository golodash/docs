#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.First(arr))
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
BenchmarkHead/slice_size_10-8           150996794               16.37 ns/op
BenchmarkHead/slice_size_100-8          147189555               16.08 ns/op
BenchmarkHead/slice_size_1000-8         150779842               16.40 ns/op
BenchmarkHead/slice_size_10000-8        133938576               17.20 ns/op
BenchmarkHead/slice_size_100000-8       134970955               17.00 ns/op
```