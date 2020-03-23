from math import sin, cos, pi
from random import randrange
import matplotlib.pyplot as plt
import matplotlib as mpl

def iexp(n):
    return complex(cos(n), sin(n))

def FFT(x_n, N, start=0, stride=1):
    "cooley-turkey fft"
    if N == 1: return [x_n[start]]
    h_n, s_n = N // 2, stride * 2
    rs = FFT(x_n, h_n, start, s_n) + FFT(x_n, h_n, start + stride, s_n)
    for i in range(h_n):
        e = iexp(-2 * pi * i / N)
        rs[i], rs[i + h_n] = rs[i] + e * rs[i + h_n], rs[i] - e * rs[i + h_n]
    return rs

def show(t, name="FFT"):
    plt.title(name)
    plt.xlabel('N')
    plt.ylabel(name)
    plt.plot([i for i in range(len(t))], t, color='red')
    plt.show()

def create_signal(n=8, N=1024, W=1200):
        """Function for create random signal"""
        x = [0 for i in range(N)]
        for i in range(N):
            for j in range(n):
                A = randrange(0, 100)
                q = randrange(0, 100)
                SINUSOID = A * sin((W/n * (j + 1) / n) * i + q)
                x[i] += SINUSOID
        return [round(x[i], 3) for i in range(len(x))]

x_n = create_signal()
a = FFT(x_n, len(x_n))

show(x_n, name="X(t)")
show(a)