#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	type myObject struct {
		rank int
	}

	returnRank := func(value1 interface{}) interface{} {
		return value1.(myObject).rank
	}

	numbers := []myObject{{rank: 1}, {rank: 2}, {rank: 3}}
	fmt.Println(slices.MeanBy(numbers, returnRank))
}
```

#! Output
```
2
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkMeanBy/slice_size_10-4                  5385985               422.8 ns/op
BenchmarkMeanBy/slice_size_100-4                  600210              4550 ns/op
BenchmarkMeanBy/slice_size_1000-4                  58600             39264 ns/op
BenchmarkMeanBy/slice_size_10000-4                  5895            559592 ns/op
BenchmarkMeanBy/slice_size_100000-4                  433           6686956 ns/op
```