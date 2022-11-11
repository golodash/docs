#! Example
```go
package main

import (
	"fmt"
	"sync"
	"time"

	"github.com/golodash/godash/functions"
)

func TestFunction(first, second int, wg *sync.WaitGroup) int {
	defer wg.Done()
	fmt.Println("running after 1 second")
	return first + second
}

func main() {
	wg := &sync.WaitGroup{}
	wg.Add(1)
	wrappedFunctions := functions.WrapFunc(TestFunction, 3, 4, wg)
	runCancel := functions.RunAfter(wrappedFunctions, 1*time.Second, true)
	runCancel.Run()

	wg.Wait()
}
```

#! Output
```
running after 1 second
```
