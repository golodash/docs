#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/numbers"
)

func main() {
	fmt.Println(numbers.Random(1, 2.1, false).(int64))
}
```

#! Output
```
1
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/numbers
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkRandom-4         242119              9070 ns/op
```