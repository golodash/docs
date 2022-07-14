#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []interface{}{[]interface{}{0, 1, 2, 3, 4}, []interface{}{3, 4}, []interface{}{5, 6, 7, 8, 9}, []interface{}{9}}
	fmt.Println(slices.Intersection(arr))
}

```

#! Output
```
[0 1 2 3 4 5 6 7 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkIntersection/slice_size_10-8             570230              4203 ns/op
BenchmarkIntersection/slice_size_100-8            152556             17349 ns/op
BenchmarkIntersection/slice_size_1000-8            17624            131197 ns/op
BenchmarkIntersection/slice_size_10000-8            1939           1234242 ns/op
BenchmarkIntersection/slice_size_100000-8            183          12318282 ns/op
```