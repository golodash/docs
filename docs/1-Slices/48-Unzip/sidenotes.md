#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := [][]int{{0, 1, 2, 3}, {4, 5, 6, 7}}
	fmt.Println(slices.Unzip(arr))
}

```

#! Output
```
[[0 4] [1 5] [2 6] [3 7]]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkUnzip/input_size_10-8            272108              8612 ns/op
BenchmarkUnzip/input_size_100-8            68739             31977 ns/op
BenchmarkUnzip/input_size_1000-8            9051            261772 ns/op
BenchmarkUnzip/input_size_10000-8            888           2470203 ns/op
BenchmarkUnzip/input_size_100000-8            87          26158966 ns/op
```