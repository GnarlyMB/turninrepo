import numpy as np
class LissajousParameters:

    def __init__(self):
        self.amplitudes()
        self.frequencies()
        self.phase_shift()
        self.t_values()
        self.coordinates()

#Amplitudes
    def amplitudes(self):
        self.A = 1
        self.B = 1


#Frequencies
    def frequencies(self):
        self.a = 3
        self.b = 2

#Phase shift
    def phase_shift(self):
        self.delta = np.pi / 2

#t values
    def t_values(self):
        self.t = np.linspace(0, 2 * np.pi, 1000)

    def coordinates(self):
        self.x = self.A * np.sin(self.a * self.t + self.delta)
        self.y = self.B * np.sin(self.b * self.t)





