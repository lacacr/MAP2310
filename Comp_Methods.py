import numpy as np

def euler(f, t0, y0, t, delta_t):
    y = [y0]
    time = np.arange(t0, t, delta_t)
    for i in time:
        y.append(y[-1] + delta_t*f(i, y[-1]))
    return time, y

def euler_mod(f, t0, y0, t, delta_t):
    y = [y0]
    time = np.arange(t0, t, delta_t)
    for i in time:
        k1 = f(i, y[-1])
        k2 = f(i + delta_t, y[-1] + delta_t*k1)
        y.append(y[-1] + delta_t*(k1 + k2)/2)
    return time, y