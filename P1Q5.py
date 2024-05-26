import numpy as np
import matplotlib.pyplot as plt
import math
import random

class P1Q5:
    def __init__(self, phi, w):
        self.phi = phi
        self.t0 = 0
        self.y0 = 1
        self.w = w
    
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
        delta_t = 0.01
        t = 0
        l = -1
        while self.psi(l, t, 100) <= 1:
            t += delta_t
        self.absInt = (-delta_t, 0)
        print("Absolute Stability Interval: ", self.absInt)

    def _StabRegWithMonteCarlo(self, n):
        delta_t = 1
        limit = (1/self.w) + 1
        valids = []
        for n in range(n):
            re = random.uniform(-limit, 1)
            im = random.uniform(-limit, limit)
            num = complex(re, im)
            if self.psi(num, delta_t, 100) <= 1:
                valids.append(num)
        plot = plt.figure()
        plt.scatter([x.real for x in valids], [x.imag for x in valids])
        plt.show()

    def _StabRegWithLevelCurves(self, n, m, amp_func):
        delta_t = 1
        limit = (1/self.w) + 1
        re = np.linspace(-limit, 1, n)
        im = np.linspace(-limit, limit, n)
        Re, Im = np.meshgrid(Re, Im)
        vec_psi = np.vectorize(self.psi)
        Z = vec_psi(complex(Re, Im), delta_t, 100)
        plot = plt.figure()
        plt.contour(Re, Im, Z, levels=np.linspace(-1, 1, m), cmap='viridis')
        plt.show()



    