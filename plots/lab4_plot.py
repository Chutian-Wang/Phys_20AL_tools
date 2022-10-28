import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

def RMSD(X):
    mean = X.mean()
    return (sum([(x - mean) ** 2 for x in X]) / (X.size - 1)) ** 0.5

def t_test(x1: np.ndarray, x2: np.ndarray) -> bool:
    sigma1 = x1.std() / (x1.size) ** 0.5
    sigma2 = x2.std() / (x2.size) ** 0.5
    t = (x1.mean() - x2.mean()) / (sigma1 ** 2 + sigma2 ** 2) ** 0.5
    t = abs(t)
    print("t =", t)
    return t > 2.776
    

class Group():
    def __init__(self, x, name = "default", sigFig = 4):
        self.name = name
        self.data = np.array(x)
        self.sigFig = sigFig
    
    def __str__(self) -> str:
        out = self.name + ":\n"
        for x in self.data:
            out += f"{x:.2f}\n"
        out += self.getStats()
        out += "------------------------------\n"
        return out
    
    def getStats(self):
        rmsd = RMSD(self.data)
        mean = self.data.mean()
        return "RMSD = {0:#.4g}, ".format(rmsd) + "Mean = {0:#.4g}\n".format(mean)

    def print(self):
        print(self.name, ":")
        print(self.getStats())

    def rmsd(self):
        return RMSD(self.data)

A = Group(np.array([1.426, 1.436, 1.427, 1.422, 1.425]), name = "A")
B = Group(np.array([1.440, 1.424, 1.432, 1.437, 1.425]), name = "B")
C = Group(np.array([1.417, 1.426, 1.417, 1.435, 1.422]), name = "C")
D = Group(np.array([1.017, 1.027, 1.029, 1.030, 1.025]), name = "D")

AO = Group(np.array([1.447, 1.425, 1.435, 1.434, 1.438]), name = "A Old")
BO = Group(np.array([1.434, 1.428, 1.419, 1.437, 1.437]), name = "B Old")
CO = Group(np.array([1.428, 1.438, 1.425, 1.425, 1.438]), name = "C Old")
DO = Group(np.array([2.025, 2.019, 2.019, 2.019, 2.019]), name = "D Old")

trials = np.arange(1, 6, 1)

print(A, B, C, D)

fig1, (Aplt, Bplt, Cplt) = plt.subplots(1, 3, sharey=True)

fig2, (AOplt, BOplt, COplt) = plt.subplots(1, 3, sharey=True)

fig3, (Dplt, DOplt) = plt.subplots(1, 2)

fig1.set_figwidth(15)
fig2.set_figwidth(15)
fig3.set_figwidth(11)

Aplt.set_xlabel("Trials")
Aplt.set_ylabel("Peirod (s)\n ")
Aplt.errorbar(trials, A.data, A.rmsd(), fmt='o', linewidth=2, capsize=6)
Aplt.set_xlim([0.5,5.5])
Aplt.axhspan(1.4192 + 0.0007, 1.4192 - 0.0007, alpha = 0.2, color = "b")
Aplt.hlines(1.4192,xmin = -1, xmax = 6, color = "r", linewidth = 1)
Aplt.tick_params(top=True, right=True)

Bplt.set_xlabel("Trials")
Bplt.set_ylabel("Peirod (s)")
Bplt.errorbar(trials, B.data, B.rmsd(), fmt='o', linewidth=2, capsize=6)
Bplt.set_xlim([0.5,5.5])
Bplt.axhspan(1.4192 + 0.0007, 1.4192 - 0.0007, alpha = 0.2, color = "b")
Bplt.hlines(1.4192,xmin = -1, xmax = 6, color = "r", linewidth = 1)
Bplt.tick_params(top=True, right=True)

Cplt.set_xlabel("Trials")
Cplt.set_ylabel("Peirod (s)")
Cplt.errorbar(trials, C.data, C.rmsd(), fmt='o', linewidth=2, capsize=6)
Cplt.set_xlim([0.5,5.5])
Cplt.axhspan(1.4192 + 0.0007, 1.4192 - 0.0007, alpha = 0.2, color = "b")
Cplt.hlines(1.4192,xmin = -1, xmax = 6, color = "r", linewidth = 1)
Cplt.tick_params(top=True, right=True)

AOplt.set_xlabel("Trials")
AOplt.set_ylabel("Peirod (s)")
AOplt.errorbar(trials, AO.data, AO.rmsd(), fmt='o', linewidth=2, capsize=6)
AOplt.set_xlim([0.5,5.5])
AOplt.axhspan(1.4192 + 0.0007, 1.4192 - 0.0007, alpha = 0.2, color = "b")
AOplt.hlines(1.4192,xmin = -1, xmax = 6, color = "r", linewidth = 1)
AOplt.tick_params(top=True, right=True)

BOplt.set_xlabel("Trials")
BOplt.set_ylabel("Peirod (s)")
BOplt.errorbar(trials, BO.data, BO.rmsd(), fmt='o', linewidth=2, capsize=6)
BOplt.set_xlim([0.5,5.5])
BOplt.axhspan(1.4192 + 0.0007, 1.4192 - 0.0007, alpha = 0.2, color = "b")
BOplt.hlines(1.4192,xmin = -1, xmax = 6, color = "r", linewidth = 1)
BOplt.tick_params(top=True, right=True)

COplt.set_xlabel("Trials")
COplt.set_ylabel("Peirod (s)")
COplt.errorbar(trials, CO.data, CO.rmsd(), fmt='o', linewidth=2, capsize=6)
COplt.set_xlim([0.5,5.5])
COplt.axhspan(1.4192 + 0.0007, 1.4192 - 0.0007, alpha = 0.2, color = "b")
COplt.hlines(1.4192,xmin = -1, xmax = 6, color = "r", linewidth = 1)
COplt.tick_params(top=True, right=True)

Dplt.set_xlabel("Trials)")
Dplt.set_ylabel("Peirod (s)")
Dplt.errorbar(trials, D.data, D.rmsd(), fmt='o', linewidth=2, capsize=6)
Dplt.set_xlim([0.5,5.5])
Dplt.axhspan(1.0035 + 0.0010, 1.0035 - 0.0010, alpha = 0.2, color = "b")
Dplt.hlines(1.0035, xmin = -1, xmax = 6, color = "r", linewidth = 1)
Dplt.tick_params(top=True, right=True)

DOplt.set_xlabel("Trials")
DOplt.set_ylabel("Peirod (s)")
DOplt.errorbar(trials, DO.data, DO.rmsd(), fmt='o', linewidth=2, capsize=6)
DOplt.set_xlim([0.5,5.5])
DOplt.axhspan(2.020 + 0.0003, 2.020 - 0.0003, alpha = 0.2, color = "b")
DOplt.hlines(2.020, xmin = -1, xmax = 6, color = "r", linewidth = 1)
DOplt.tick_params(top=True, right=True)

print("t-test A, A Old: ", t_test(A.data, AO.data))
print("t-test B, B Old: ", t_test(B.data, BO.data))
print("t-test C, C Old: ", t_test(C.data, CO.data))
print("t-test D, D Old: ", t_test(D.data, DO.data))

print("t-test A, B", t_test(A.data, C.data))

plt.show()