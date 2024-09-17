### Name: Yash Daswani
### Student ID: `1002257766`

## Explanation of Recursive Steps in `fib(5)`

1. The initial call `fib(5)` triggers two recursive calls: `fib(4)` and `fib(3)`.
2. Next, `fib(4)` calls both `fib(3)` and `fib(2)`.
3. `fib(3)` further breaks down into `fib(2)` and `fib(1)`.
4. `fib(2)` invokes `fib(1)` and `fib(0)`, which return `1` and `0` respectively.
5. Using these base cases, `fib(2)` returns `1`, and `fib(3)` computes its value as `2` by summing `fib(2)` and `fib(1)`.
6. Returning to `fib(4)`, the result of `fib(3)` (which is `2`) is added to the result of `fib(2)` (which is `1`), leading `fib(4)` to return `3`.
7. Finally, back in `fib(5)`, the results of `fib(4)` and `fib(3)` are summed (i.e., `3 + 2`), yielding the final output of `5`.

For a more detailed explanation of how the recursive function call stack works, refer to the `fibonacci.py` file.

## Time Complexity of Recursive Fibonacci Function

The time complexity of the recursive Fibonacci function is `O(2^n)`, which is exponential.

### Why is it `O(2^n)`?

#### Recursive Call Structure:
- For each `fib(n)` call, two recursive calls are made: `fib(n-1)` and `fib(n-2)`. This branching continues at every level, leading to an exponential number of recursive calls.

#### Overlapping Subproblems:
- Many Fibonacci numbers are computed multiple times. For instance, `fib(2)` and `fib(1)` are computed several times within the recursion tree. The repeated calculations grow exponentially as `n` increases.

As a result, for Fibonacci number `n`, approximately `2^n` recursive calls are made, contributing to the exponential time complexity `O(2^n)`.

## Optimizing Fibonacci Function

### 1. Memoization:
- Memoization involves storing the results of previously computed Fibonacci numbers to avoid redundant calculations. This optimization reduces the time complexity to `O(n)` by allowing quick access to previously computed results in constant time `O(1)`.

### 2. Dynamic Programming:
- By storing the Fibonacci sequence in an array and calculating the results iteratively up to `n`, dynamic programming can also reduce the time complexity to `O(n)`.

