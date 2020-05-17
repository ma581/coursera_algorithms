from typing import List
import collections

def mah(maxTravelDist, forwardRouteList, returnRouteList):
    d = collections.defaultdict(list)
    for f in forwardRouteList:
        for r in returnRouteList:
            d[f[1] + r[1]].append((f[0], r[0]))

    if min(d.keys()) > maxTravelDist:
        return [()]
    elif maxTravelDist in d:
        return d[maxTravelDist]
    else:
        best = maxTravelDist
        while best not in d:
            best = best - 1
        return d[best]

def test_lbah():
    a = mah(7000, [[1, 3000], [2, 4000], [3, 6000]], [[1, 2000]])
    assert a == [(2,1)]
    assert False
