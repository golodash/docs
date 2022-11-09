#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.PadEnd("Test-Case", 11, "||"))
}
```

#! Output
```
Test-Case||
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkPadEnd/input_size_10-4                 20379440               118.8 ns/op
BenchmarkPadEnd/input_size_100-4                 5289979               448.3 ns/op
BenchmarkPadEnd/input_size_1000-4                 572967              4520 ns/op
BenchmarkPadEnd/input_size_10000-4                 50173             71794 ns/op
BenchmarkPadEnd/input_size_100000-4                 3816            652216 ns/op
```