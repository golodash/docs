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
	fmt.Println(slices.MinBy(myObjects, returnRank).(myObjects))
}
```

#! Output
```
{1}
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkMinBy/slice_size_10-4           1000000              2291 ns/op
BenchmarkMinBy/slice_size_100-4           165362             13695 ns/op
BenchmarkMinBy/slice_size_1000-4           18630            170302 ns/op
BenchmarkMinBy/slice_size_10000-4           1650           2094441 ns/op
BenchmarkMinBy/slice_size_100000-4           186          17021700 ns/op
```