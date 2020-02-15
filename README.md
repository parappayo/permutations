
# Permutations & Combinations

This repo contains small programs that explore [permutations](https://en.wikipedia.org/wiki/Permutation) and [combinations](https://en.wikipedia.org/wiki/Combination) using various tools.

The goal is to explore algorithms and programming languages.

## Iterables and Lazy Evaluation

The number of permutations of an ordered list is `factorial(length(list))`. The factorial function grows quickly, so it is not generally practical to store a copy of every permutation of the list in memory at the same time.

When iterating through the permutations in order, it is efficient to store state about the current permutation for use in generating the next one; recursive algorithms keep such state on the stack. Either way, the storage used grows linearly with the size of the input, `O(n)`.

## Indexed Permutations

A method for enumerating permutations of an ordered list is to consider sequential factors of the index number as divisors and use the resulting sequence of remainders as insertion indexes. This method allows one to jump straight to the Nth enumerated permutation without iterating through the previous ones.

For the ordinal permutation `index` of ordered list `list`, calculate a sequence of insertion indexes as `[index % x for x in range(1,len(list)+1)]`.

For example, consider `[a, b, c, d]` with 24 permutations. If we want to generate the 10th permutation,

* `10 % 1 = 0`, so `[a]`
* `10 % 2 = 0`, so `[b, a]`
* `10 % 3 = 1`, so `[b, c, a]`
* `10 % 4 = 2`, so `[b, c, d, a]`

There are varations on ordering when inserting from the front of the list versus from the end, as well as from inserting the elements in reverse order. The amount of work is `O(n * k)` where `k` is the work needed for a list insertion operation, which could be constant in which case the time complexity is `O(n)`.

## Shuffle

Shuffling an ordered list can be defined as selecting a random permutation. This can be accomplished with `index = random(factorial(length(this)))` and then generating the corresponding permutation; see "Indexed Insertion" above.

A simple algorithm for shuffling a list in-place is the [Fisher-Yates Shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle).

## Immutable Strings

Programming environments often have immutable strings, so care has to be taken not to waste memory with a lot of intermediate string objects during the creation of a new permutation string.

Eg. from the [C# Programming Guide](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/strings/),

"String objects are immutable: they cannot be changed after they have been created. All of the String methods and C# operators that appear to modify a string actually return the results in a new string object."

C# provides the `StringBuilder` type for working efficiently with string construction. `String.Format` is also useful, as is the string interpolation operator, `$`.

Python also has immutable strings and the [Python 3 docs](https://docs.python.org/3/library/stdtypes.html) offer the following advice:

"There is also no mutable string type, but str.join() or io.StringIO can be used to efficiently construct strings from multiple fragments."

## Dynamic Typing

For programming environments that are either loosely typed or have good type inference rules, a single implementation can be used to permute an ordered list of objects, values, or even the characters of a string. Consider, for example, that a simple Python generator implementation works on strings and lists.

C# offers generics and C++ offers templates for expanding code to handle multiple types at compile time. Alternatively, reference semantics using universal base types like `object` or `void*` could be used to permute a list of references without being aware of what the referenced data is.
