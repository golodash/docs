#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/strings"
)

func main() {
	fmt.Println(strings.SnakeCase("Test Case"))
}
```

#! Output
```
test_case
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/strings
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkSnakeCase/input_size_10-4              13422240               172.2 ns/op
BenchmarkSnakeCase/input_size_100-4              1749292              1187 ns/op
BenchmarkSnakeCase/input_size_1000-4              218361             10949 ns/op
BenchmarkSnakeCase/input_size_10000-4              20769            108580 ns/op
BenchmarkSnakeCase/input_size_100000-4              2182           1048172 ns/op
```