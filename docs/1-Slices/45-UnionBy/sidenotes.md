#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func makeInt(input interface{}) interface{} {
	return int(input.(float64))
}

func main() {
	arr1 := []float64{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	arr2 := []float64{0, 1, 2, 3, 4, 5, 10, 11}
	fmt.Println(slices.UnionBy(arr1, arr2, makeInt))
}
```

#! Output
```
[0 1 2 3 4 5 6 7 8 9 10 11]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkUnionBy/input_size_10-8                  658910              3206 ns/op
BenchmarkUnionBy/input_size_100-8                 135414             14922 ns/op
BenchmarkUnionBy/input_size_1000-8                 18309            123212 ns/op
BenchmarkUnionBy/input_size_10000-8                 1870           1230371 ns/op
BenchmarkUnionBy/input_size_100000-8                 180          11784229 ns/op
```