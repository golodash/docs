#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func isOdd(n interface{}) bool {
	return n.(int)%2 != 0
}

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.RemoveBy(arr, isOdd))
}
```

#! Output
```
[0 2 4 6 8] [9 7 5 3 1]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkRemoveBy/input_size_10-8                5332122               410.2 ns/op
BenchmarkRemoveBy/input_size_100-8                806427              2872 ns/op
BenchmarkRemoveBy/input_size_1000-8                78412             27322 ns/op
BenchmarkRemoveBy/input_size_10000-8                8348            277035 ns/op
BenchmarkRemoveBy/input_size_100000-8                800           2694867 ns/op
```