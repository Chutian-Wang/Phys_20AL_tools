import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import scipy.stats as st
from scipy.optimize import curve_fit

def RMSD(X: np.ndarray) -> float:
    return X.std(ddof = 1)

#return true if t > 2
def t_test(x1: np.ndarray, x2: np.ndarray, T = 2) -> bool:
    sigma1 = x1.std() / (x1.size) ** 0.5
    sigma2 = x2.std() / (x2.size) ** 0.5
    t = (x1.mean() - x2.mean()) / (sigma1 ** 2 + sigma2 ** 2) ** 0.5
    t = abs(t)
    print("t =", t)
    return t > 2, t

#return true if z > 1.96 (2-tailed 95%)
def z_test(x: np.ndarray, mu: float, Z = 1.96) -> bool:
    z = (x.mean() - mu) / RMSD(x)
    return z > Z, z

class Group():
    def __init__(self, data, dataName, dataUnit, name = "default", sigFig = 4):
        self.name = name
        self.data = np.array(data)
        self.sigFig = sigFig
        self.uncertainty = [np.std(self.data, ddof = 1),] * self.data.size
        self.dataName = dataName
        self.dataUnit = dataUnit
    
    def __str__(self) -> str:
        out = self.name + ":\n"
        for x in self.data:
            out += f"{x:.2f}\n"
        out += self.getStatsString()
        out += "------------------------------\n"
        return out
    
    def getStats(self)->tuple:
        rmsd = RMSD(self.data)
        mean = self.data.mean()
        return mean, rmsd

    def getStatsString(self):
        rmsd = RMSD(self.data)
        mean = self.data.mean()
        return "Mean = {0:#.4g}\n".format(mean) + "RMSD = {0:#.4g}, ".format(rmsd)

    def print(self):
        print(self.name, ":")
        print(self.getStatsString())

    def RMSD(self):
        return RMSD(self.data)
    
    def plot(self, axes:plt.Axes)->None:
        axes.set_xlabel("Trials" + '\n\n' + self.name)
        axes.set_ylabel(self.dataName + ' (' + self.dataUnit + ')')
        axes.xaxis.set_major_locator(MultipleLocator(1))
        axes.yaxis.set_minor_locator(AutoMinorLocator())
        axes.yaxis.set_major_formatter('{x:.2f}')
        axes.tick_params(axis='both', direction = 'in', top = True, right = True, which = 'both')

        axes.errorbar(np.arange(1, self.data.size + 1), self.data, self.uncertainty, fmt='o', linewidth = 2, capsize = 6)
