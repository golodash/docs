#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.Truncate("  This is a freaking test just for the fun of it!??", 20, []rune{' '}, "..."))
}
```

#! Output
```
This is a freaking...
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkTruncate/input_size_10-4               30879622                73.86 ns/op
BenchmarkTruncate/input_size_100-4              20838583               125.8 ns/op
BenchmarkTruncate/input_size_1000-4              6543098               322.1 ns/op
BenchmarkTruncate/input_size_10000-4             1089510              1919 ns/op
BenchmarkTruncate/input_size_100000-4             111117             18698 ns/op
```