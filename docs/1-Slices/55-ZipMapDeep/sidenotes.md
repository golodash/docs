#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	keys := []string{"a.bid", "a.b", "b.c"}
	values := []string{"A", "B", "C"}
	fmt.Println(slices.ZipMapDeep(keys, values))
}

```

#! Output
```
map[a:map[b:B bid:A] b:map[c:C]]
```

#! Benchmark Output
```
goos: linux
goarch: amd64
pkg: github.com/golodash/godash/slices
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkZipMapDeep/input_size_10-8               922364              2518 ns/op
BenchmarkZipMapDeep/input_size_100-8              116497             18481 ns/op
BenchmarkZipMapDeep/input_size_1000-8              13326            174051 ns/op
BenchmarkZipMapDeep/input_size_10000-8              1171           1751329 ns/op
BenchmarkZipMapDeep/input_size_100000-8              134          17345435 ns/op
```