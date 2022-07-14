#! Example
```go
package main

import (
	"fmt"

	"github.com/golodash/godash/slices"
)

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(slices.IndexOf(arr, 4, 0))
}

```

#! Output
```
4
```

#! Benchmark Output
```
BenchmarkIndexOf/slice_size_10-8                 3970878               572.2 ns/op
BenchmarkIndexOf/slice_size_100-8                 476493              5020 ns/op
BenchmarkIndexOf/slice_size_1000-8                 45938             48496 ns/op
BenchmarkIndexOf/slice_size_10000-8                 4888            489439 ns/op
BenchmarkIndexOf/slice_size_100000-8                 452           4839417 ns/op
BenchmarkLastIndexOf/slice_size_10-8            33820658                73.36 ns/op
BenchmarkLastIndexOf/slice_size_100-8           31159791                75.05 ns/op
BenchmarkLastIndexOf/slice_size_1000-8          31756544                75.50 ns/op
BenchmarkLastIndexOf/slice_size_10000-8         30758478                71.13 ns/op
BenchmarkLastIndexOf/slice_size_100000-8        32282296                78.20 ns/op
BenchmarkSortedIndexOf/slice_size_10-8            818491              2859 ns/op
BenchmarkSortedIndexOf/slice_size_100-8           523748              4603 ns/op
BenchmarkSortedIndexOf/slice_size_1000-8          380896              6136 ns/op
BenchmarkSortedIndexOf/slice_size_10000-8                 285841              8533 ns/op
BenchmarkSortedIndexOf/slice_size_100000-8                220206              9965 ns/op
BenchmarkSortedLastIndexOf/slice_size_10-8                846108              2726 ns/op
BenchmarkSortedLastIndexOf/slice_size_100-8               518176              4843 ns/op
BenchmarkSortedLastIndexOf/slice_size_1000-8              391922              6123 ns/op
BenchmarkSortedLastIndexOf/slice_size_10000-8             279405              8483 ns/op
BenchmarkSortedLastIndexOf/slice_size_100000-8            237076             10077 ns/op
```