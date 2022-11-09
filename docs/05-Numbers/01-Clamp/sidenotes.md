#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/numbers"
)

func main() {
	fmt.Println(numbers.Clamp(2.1, 1, 2).(float64))
}
```

#! Output
```
2
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/numbers
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkClamp-4        11290821               180.3 ns/op
```