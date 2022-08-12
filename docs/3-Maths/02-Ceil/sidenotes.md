#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/maths"
)

func main() {
	fmt.Println(maths.Ceil(1.1224, 2).(float64))
}
```

#! Output
```
1.13
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/maths
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkCeil-4         11805555               287.6 ns/op
```