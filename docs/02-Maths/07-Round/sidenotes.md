#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/maths"
)

func main() {
	fmt.Println(maths.Round(1.021, 2).(float64))
}
```

#! Output
```
1.02
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/maths
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkRound-4         4882981               416.7 ns/op
```