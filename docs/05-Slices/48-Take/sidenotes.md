#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.Take(arr, 3).([]int))
}
```

#! Output
```
[0 1 2]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkTake/input_size_10-8           51511062                45.67 ns/op
BenchmarkTake/input_size_100-8          50494014                46.20 ns/op
BenchmarkTake/input_size_1000-8         50453743                46.33 ns/op
BenchmarkTake/input_size_10000-8        51561108                46.23 ns/op
BenchmarkTake/input_size_100000-8       51525472                45.76 ns/op
```