#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/maths"
)

func main() {
	fmt.Println(maths.Add(1.2, 2.3).(float64))
}
```

#! Output
```
3.5
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/maths
cpu: Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz
BenchmarkAdd-4          12339258               254.8 ns/op
```