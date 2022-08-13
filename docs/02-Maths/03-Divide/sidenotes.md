#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/maths"
)

func main() {
	fmt.Println(maths.Divide(0.2, 2).(float64))
}
```

#! Output
```
0.1
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/maths
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkDivide-4       12688716               180.8 ns/op
```