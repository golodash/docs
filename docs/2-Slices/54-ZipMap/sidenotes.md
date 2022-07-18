#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3}
	values := []string{"A", "B", "C", "D"}
	fmt.Println(slices.ZipMap(arr, values).(map[int]string))
}
```

#! Output
```
map[0:A 1:B 2:C 3:D]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkZipMap/input_size_10-8                  2317904              1008 ns/op
BenchmarkZipMap/input_size_100-8                  302179              7359 ns/op
BenchmarkZipMap/input_size_1000-8                  31560             71821 ns/op
BenchmarkZipMap/input_size_10000-8                  3603            658030 ns/op
BenchmarkZipMap/input_size_100000-8                  355           6274107 ns/op
```