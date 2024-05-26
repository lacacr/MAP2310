import numpy as np
import matplotlib.pyplot as plt
import math
import random

class P1Q5:
    def __init__(self, phi):
        self.phi = phi
        self.t0 = 0
        self.y0 = 1
    
    def psi(self, l, delta_t, n):
        f = lambda y: l * y
        y0 = self.y0
        t = self.t0 + delta_t
        phi = []
        for i in range(n):
            y1 = y0 + delta_t * phi(f, t, y0)
            x = x + delta_t
            phi.append(y1/y0)
            y0 = y1
        return np.mean(phi)
    
    def _calculateAbsStabInt(self):
        delta_t = 0
        l = -1
        while self.psi(l, delta_t, 100) <= 1:
            delta_t += 0.01
        self.absInt = (-delta_t, 0)