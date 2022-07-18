#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.Reverse(arr).([]int))
}
```

#! Output
```
[9 8 7 6 5 4 3 2 1 0]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkReverse/input_size_10-8                 5802160               377.2 ns/op
BenchmarkReverse/input_size_100-8                1579416              1561 ns/op
BenchmarkReverse/input_size_1000-8                150835             13478 ns/op
BenchmarkReverse/input_size_10000-8                18358            129043 ns/op
BenchmarkReverse/input_size_100000-8                1502           1341846 ns/op
```