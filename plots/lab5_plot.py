from string import whitespace
from DataProcessing import *

fig = plt.figure(figsize= (9, 15), layout="constrained")
spec = fig.add_gridspec(ncols = 2, nrows= 3)

A = Group(
    0.98 / np.array([0.0465,0.0465,0.0460,0.0465,0.0465]),
    "Spring Constant",
    "N/m",
    "Group A Spring Constant Measurement")
aplt = fig.add_subplot(spec[0,0])

B = Group(
    1.96 / np.array([0.1405,0.1410,0.1405,0.1405,0.1400]),
    "Spring constant",
    "N/m",
    "Group B Spring Constant Measurement")
bplt = fig.add_subplot(spec[0,1])

C = Group(
    2.94 / np.array([0.243,0.243,0.244,0.242,0.243]),
    "Spring constant",
    "N/m",
    "Group C Spring Constant Measurement")
cplt = fig.add_subplot(spec[1,0])

D = Group(
    3.92 / np.array([0.342,0.343,0.341,0.342,0.342]),
    "Spring constant",
    "N/m",
    "Group D Spring Constant Measurement")
dplt = fig.add_subplot(spec[1,1])

E = Group(
    4.9 / np.array([0.443,0.443,0.444,0.444,0.443]),
    "Spring constant",
    "N/m",
    "Group E Spring Constant Measurement")
eplt = fig.add_subplot(spec[2,0])

groups = [A, B, C, D, E]
plots = [aplt, bplt, cplt, dplt, eplt]

for p in enumerate(groups):
    print(p[1])
    p[1].plot(plots[p[0]])

fig.savefig("fig1")

combined = np.concatenate((A.data, B.data, C.data, D.data, E.data))

allgroups = Group(combined, "k all", "N/m")
print(allgroups)
print(z_test(combined, 9.475))

plt.show()