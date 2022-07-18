#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func returnInt(input interface{}) interface{} {
	return int(input.(float64))
}

func main() {
	arr1 := []float64{0, 1.7, 2, 3, 4.5, 5, 6, 7, 8, 9}
	arr2 := []float64{4, 5, 6, 7}
	fmt.Println(slices.XorBy(arr1, arr2, returnInt).([]float64))
}
```

#! Output
```
[0 1.7 2 3 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkXorBy/input_size_10-8            715108              3300 ns/op
BenchmarkXorBy/input_size_100-8            82887             25121 ns/op
BenchmarkXorBy/input_size_1000-8           10846            221335 ns/op
BenchmarkXorBy/input_size_10000-8           1101           2154068 ns/op
BenchmarkXorBy/input_size_100000-8           117          20291565 ns/op
```