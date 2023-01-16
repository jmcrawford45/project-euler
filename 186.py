from functools import lru_cache

@lru_cache
def generator(k: int) -> int:
    if 1 <= k <= 55:
        return (100003 - 200003*k + 300007*k**3) % 1000000
    return (generator(k-24) + generator(k-55))  % 1000000

def records():
    curr = 1
    while True:
        yield generator(curr), generator(curr+1)
        curr += 2

assert next(records()) == (200007, 100053)
from collections import defaultdict
components = []
component_graph = defaultdict(set)
calls = 0
prime_minister = 524287
for caller, called in records():
    if caller == called:
        continue
    if calls % 50000 == 0:
        print(calls)
    bigger = component_graph[called]
    smaller = component_graph[caller]
    if caller in bigger and called in smaller:
        calls += 1
        continue
    if len(component_graph[caller]) > len(component_graph[called]):
        bigger = component_graph[caller]
        smaller = component_graph[called]
    smaller |= set([caller, called])
    bigger |= smaller
    for person in smaller:
        component_graph[person] = bigger
    calls += 1
    if len(component_graph[prime_minister]) >= 990000:
        break
print(calls)
