#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.Words("test-Case is_here"))
}
```

#! Output
```
[test Case is here]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkWords/input_size_10-4           6085548               398.3 ns/op
BenchmarkWords/input_size_100-4           622466              3606 ns/op
BenchmarkWords/input_size_1000-4           67502             40020 ns/op
BenchmarkWords/input_size_10000-4           6705            333301 ns/op
BenchmarkWords/input_size_100000-4           663           3367702 ns/op
```