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

	myObjects := []myObject{{rank: 1}, {rank: 2}, {rank: 3}}
	fmt.Println(slices.MaxBy(myObjects, returnRank).(myObjects))
}
```

#! Output
```
{3}
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkMaxBy/slice_size_10-4           1772199              1323 ns/op
BenchmarkMaxBy/slice_size_100-4           169602             12744 ns/op
BenchmarkMaxBy/slice_size_1000-4           18681            133627 ns/op
BenchmarkMaxBy/slice_size_10000-4           1524           2068457 ns/op
BenchmarkMaxBy/slice_size_100000-4           168          17706295 ns/op
```