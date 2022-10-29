#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []float64{0, 1, 2, 3, 3, 4, 7, 9, 5, 6, 7, 8, 9}
	fmt.Println(slices.Unique(arr).(float64))
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
BenchmarkUnique/input_size_10-8           2910115               833.5 ns/op
BenchmarkUnique/input_size_100-8           407136              5787 ns/op
BenchmarkUnique/input_size_1000-8           43980             52662 ns/op
BenchmarkUnique/input_size_10000-8           4494            497668 ns/op
BenchmarkUnique/input_size_100000-8           432           4912433 ns/op
```