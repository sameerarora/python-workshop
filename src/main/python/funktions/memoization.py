from functools import lru_cache
from funktions.partials import print_with_tabs as print


@lru_cache(maxsize=32)  # defaults to 128
def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)  # fact(4) -> 4 * fact(3) -> 4 * 3 * fact(2) -> 4 * 3 *2 *fact(1)


print(fact(4))
print(fact(4))
print(fact(4))
print(fact(4))
print(fact(4))
print(fact(3))
print(fact(2))
print(fact(1))
print(fact(6))
print(fact.cache_info())
# TODO how to reset the cache
