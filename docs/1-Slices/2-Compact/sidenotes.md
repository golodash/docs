#! Example
```go
package main

import (
	"fmt"
	"github.com/golodash/godash/slices"
)

func main() {
	arg := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.Compact(arg, []interface{}{}).([]int))
}
```

#! Output
```
[1 2 3 4 5 6 7 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkCompact/slice_size_10-8         	 1373620	      1802 ns/op
BenchmarkCompact/slice_size_100-8        	  156679	     14718 ns/op
BenchmarkCompact/slice_size_1000-8       	   16185	    144851 ns/op
BenchmarkCompact/slice_size_10000-8      	    1549	   1434761 ns/op
BenchmarkCompact/slice_size_100000-8     	     166	  13659337 ns/op
```