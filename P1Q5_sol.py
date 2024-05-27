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
        phis = []
        for i in range(n):
            y1 = y0 + delta_t * self.phi(delta_t, f, t, y0)
            t = t + delta_t
            phis.append(y1/y0)
            y0 = y1
        return abs(np.mean(phis))
    
    def _calculateAbsStabInt(self):
        delta_t = 0.01
        t = 0
        l = -1
        valids = []
        if abs(self.psi(l, t, 100)) <= 1:
            valids.append(t)
            current = True
        else: current = False
        while t <= (1/self.w):
            t += delta_t
            psi = abs(self.psi(l, t, 100))
            next = (psi <= 1)
            if current != next:
                valids.append(round(t,2))
                current = next
        if len(valids) == 1:
            valids.append(1/self.w)
        return valids

    def _StabRegWithMonteCarlo(self, n):
        delta_t = 1
        limit = (1/self.w) + 1
        valids = []
        for n in range(n):
            re = random.uniform(-limit, limit)
            im = random.uniform(-limit, limit)
            num = complex(re, im)
            if self.psi(num, delta_t, 100) <= 1:
                valids.append(num)
        plot = plt.figure()
        plt.scatter([x.real for x in valids], [x.imag for x in valids], color="black", marker=".")
        plt.show()

    def _StabRegWithLevelCurves(self, n, m, amp_func):
        delta_t = 1
        limit = (1/self.w) + 1
        re = np.linspace(-limit, 1, n)
        im = np.linspace(-limit, limit, n)
        Re, Im = np.meshgrid(re, im)
        vec_psi = np.vectorize(self.psi)
        vec_complex = np.vectorize(complex)
        Z = vec_psi(vec_complex(Re, Im), delta_t, 50)
        plot = plt.figure()
        plt.contour(Re, Im, Z, levels=np.linspace(-1, 1, m), cmap='binary')
        plt.show()

    def _StabRegWithLevelCurvesWithAmp(self, n, amp_func):
        delta_t = 1
        limit = (1/self.w) + 1
        re = np.linspace(-limit, 1, n)
        im = np.linspace(-limit, limit, n)
        Re, Im = np.meshgrid(re, im)
        vec_amp = np.vectorize(amp_func)
        vec_complex = np.vectorize(complex)
        Z = vec_amp(vec_complex(Re, Im), delta_t)
        plot = plt.figure()
        plt.contour(Re, Im, Z, levels=np.linspace(-1, 1, 50), cmap='binary')
        plt.show()



    