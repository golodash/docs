#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)


func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	values := []int{0, 3}
	fmt.Println(slices.Pull(arr, values))
}

```

#! Output
```
[1 2 4 5 6 7 8 9]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkPull/slice_size_10-8             427863              5567 ns/op
BenchmarkPull/slice_size_100-8              5082            459484 ns/op
BenchmarkPull/slice_size_1000-8               51          45298096 ns/op
BenchmarkPull/slice_size_10000-8               1        4515833971 ns/op
```