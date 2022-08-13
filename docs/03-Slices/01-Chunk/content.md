---
Title: Chunk
---

Gets a `slice` and a `size` as input and splits the slice into pieces in length of the `size`.

#- Inputs
- slice `[]anything`
- Has to be a slice but type of elements of slice do not matter.
- size `int`
- Can be any number in range of [1,2,...].

**Note**: Passing invalid input causes panic.

#- Outputs
- first `[]sameTypeAsSlice`
- A slice of `slice` type input will return as output.

#- Complexity
- `Chunk` has a complexity of O(n).
