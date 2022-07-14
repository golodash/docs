#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := [][]string{{"0", "1"}, {"2", "3"}, {"4", "5"}, {"6", "7"}, {"8", "9"}}
	fmt.Println(slices.FromPairs(arr))
}

```

#! Output
```
map[0:1 2:3 4:5 6:7 8:9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFromPairs/slice_size_10-8               1662324              1433 ns/op
BenchmarkFromPairs/slice_size_100-8               196152             12440 ns/op
BenchmarkFromPairs/slice_size_1000-8               20236            116410 ns/op
BenchmarkFromPairs/slice_size_10000-8               2042           1215846 ns/op
BenchmarkFromPairs/slice_size_100000-8               188          12115077 ns/op
```