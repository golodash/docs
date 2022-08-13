#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr1 := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	arr2 := []int{4, 5, 6, 7}
	fmt.Println(slices.Xor(arr1, arr2).([]int))
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
BenchmarkXor/input_size_10-8              573898              3503 ns/op
BenchmarkXor/input_size_100-8              98935             23059 ns/op
BenchmarkXor/input_size_1000-8             10884            201678 ns/op
BenchmarkXor/input_size_10000-8             1098           2067460 ns/op
BenchmarkXor/input_size_100000-8             120          21314330 ns/op
```