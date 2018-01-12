# LRU-cache-for-memoization
Implementation of LRU cache for memoization in Python



[Memoization](https://en.wikipedia.org/wiki/Memoization) is an optimization technique for speeding up function calls by caching the function result for a given set of inputs. This works so long as the function is *pure*, i.e., it always returns the same result for the same arguments. The Python standard library actually includes a function decorator in the functools module called [lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) that performs memoization on any function that it wraps with one twist--it only stores function results for for the N most recent calls. This is called a *least recently used* (LRU) cache because the least recently used items are discarded from the function result cache if it has reached its maximum size. 
Here we are writing our own version of the `lru_cache` decorator.
