#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.PascalCase("test_case"))
}
```

#! Output
```
TestCase
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkPascalCase/input_size_10-4             25959451                87.17 ns/op
BenchmarkPascalCase/input_size_100-4             4359375               534.7 ns/op
BenchmarkPascalCase/input_size_1000-4             495932              4781 ns/op
BenchmarkPascalCase/input_size_10000-4             51381             45606 ns/op
BenchmarkPascalCase/input_size_100000-4             5334            590612 ns/op
```