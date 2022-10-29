#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/maths"
)

func main() {
	fmt.Println(maths.Power(2, 2).(int))
}
```

#! Output
```
4
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/maths
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkPower/slice_size_10-4          25945111                95.71 ns/op
BenchmarkPower/slice_size_100-4         11808710               189.6 ns/op
BenchmarkPower/slice_size_1000-4          982213              2238 ns/op
BenchmarkPower/slice_size_10000-4         178603             13503 ns/op
BenchmarkPower/slice_size_100000-4         18968            125575 ns/op
```