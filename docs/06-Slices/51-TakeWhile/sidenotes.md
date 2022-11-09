#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func isEven(input interface{}) bool {
	return input.(int)%2 == 0
}

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.TakeWhile(arr, isEven).([]int))
}
```

#! Output
```
[1 2 3 4 5 6 7 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkTakeWhile/input_size_10-8               5539058               403.8 ns/op
BenchmarkTakeWhile/input_size_100-8               656920              3402 ns/op
BenchmarkTakeWhile/input_size_1000-8               68175             32306 ns/op
BenchmarkTakeWhile/input_size_10000-8               7010            335293 ns/op
BenchmarkTakeWhile/input_size_100000-8               637           3313901 ns/op
```