import numpy as np
from Comp_Methods import *
import math

def total_convergence(f, t0, y0, t, delta_t, N, method, exact):
    y = exact(t)
    entries = []
    for i in range(N):
        h = delta_t / 2**i
        n1 = method(f, t0, y0, t, h)[1][-1]
        n2 = method(f, t0, y0, t, h/2)[1][-1]
        e1 = abs(n1-y)
        e2 = abs(n2-y)
        q = e1/e2
        p = math.log2(q)
        entries.append([2**i, h, e1, p])
    return entries

def estimated_convergence(f, t0, y0, t, delta_t, N, method):
    entries = []
    for i in range(N):
        h = delta_t / 2**i
        n1 = method(f, t0, y0, t, h)[1][-1]
        n2 = method(f, t0, y0, t, h/2)[1][-1]
        n3 = method(f, t0, y0, t, 2*h)[1][-1]
        e1 = abs(n3-n1)
        e2 = abs(n1-n2)
        q = e1/e2
        p = math.log2(q)
        entries.append([2**i, h, e1, p])
    return entries