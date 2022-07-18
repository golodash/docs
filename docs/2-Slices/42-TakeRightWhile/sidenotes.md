#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func isOdd(input interface{}) bool {
	return input.(int)%2 == 1
}

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.TakeRightWhile(arr, isOdd).([]int))
}
```

#! Output
```
[0 1 2 3 4 5 6 7 8]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkTakeRightWhile/input_size_10-8                  5978796               404.0 ns/op
BenchmarkTakeRightWhile/input_size_100-8                  652140              3098 ns/op
BenchmarkTakeRightWhile/input_size_1000-8                  70790             30903 ns/op
BenchmarkTakeRightWhile/input_size_10000-8                  7928            290529 ns/op
BenchmarkTakeRightWhile/input_size_100000-8                  819           2829011 ns/op
```