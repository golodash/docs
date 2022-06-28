#! Example
```go
package main

import (
        "fmt"
        "github.com/golodash/godash/slices"
)

func main() {
        arg := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} 
        fmt.Println(slices.Chunk(arg, 2).([][]int))
}
```

#! Output
```
[[0 1] [2 3] [4 5] [6 7] [8 9]]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkChunk/slice_size_10-4           1591783              1482 ns/op
BenchmarkChunk/slice_size_100-4           174444             16644 ns/op
BenchmarkChunk/slice_size_1000-4           19929            152630 ns/op
BenchmarkChunk/slice_size_10000-4           2278           1141037 ns/op
BenchmarkChunk/slice_size_100000-4           195          15050196 ns/op
```