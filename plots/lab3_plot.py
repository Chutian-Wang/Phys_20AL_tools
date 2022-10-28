import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

trials = [0, 1, 2, 3, 4, 5]
colors = ["green", "blue", "blue", "blue", "blue"]

A = [1.4192, 1.447, 1.425, 1.435, 1.434, 1.438]
Aerr = [0.0007] + [0.008,] * 5

B = [1.4192, 1.434, 1.428, 1.419, 1.437, 1.437]
Berr = [0.0007] + [0.008,] * 5

C = [1.4192, 1.428, 1.438, 1.425, 1.425, 1.438]
Cerr = [0.0007] + [0.007,] * 5

D = [2.0071, 2.025, 2.019, 2.019, 2.019, 2.019]
Derr = [0.0005] + [0.003,] * 5

E = [1.4192, 1.527, 1.537, 1.539, 1.535, 1.566]
Eerr = [0.0007] + [0.014,] * 5


fig1, (Aplt, Bplt, Cplt) = plt.subplots(1, 3, sharey=True)
fig2, (Aplt1, Dplt) = plt.subplots(1, 2)
fig3, (Aplt2, Eplt) = plt.subplots(1, 2)

fig1.set_figwidth(15)
fig1.suptitle("Test Relationship Between Mass and Period, L = 50.00 ± 0.005 cm, θ = 10.0 ± 2.5 degrees")
fig2.set_figwidth(10)
fig2.suptitle("Test Relationship Between Length and Period, m = 24.20 ± 0,05 g, θ = 10.0 ± 2.5 degrees")
fig3.set_figwidth(10)
fig3.suptitle("Test Relationship Between Angular Amplitude and Period, m = 24.20 ± 0,05 g, L = 50.00 ± 0.005 cm")

Aplt.set_title("Group A (m = 24.20 ± 0.05 g)")
Aplt.set_xlabel("Trials (trial 0 is theoretical)")
Aplt.set_ylabel("Peirod / s")
Aplt.errorbar(trials, A, Aerr, fmt='o', linewidth=2, capsize=6)

Bplt.set_title("Group B (m = 54.10 ± 0.05 g)")
Bplt.set_xlabel("Trials (trial 0 is theoretical)")
Bplt.set_ylabel("Peirod / s")
Bplt.errorbar(trials, B, Berr, fmt='o', linewidth=2, capsize=6)

Cplt.set_title("Group C (m = 4.80 ± 0.05 g)")
Cplt.set_xlabel("Trials (trial 0 is theoretical)")
Cplt.set_ylabel("Peirod / s")
Cplt.errorbar(trials, C, Cerr, fmt='o', linewidth=2, capsize=6)

Aplt.yaxis.set_minor_locator(MultipleLocator(0.005))


Aplt1.set_title("Group A (L = 50.00 ± 0.005 cm)")
Aplt1.set_xlabel("Trials (trial 0 is theoretical)")
Aplt1.set_ylabel("Peirod / s")
Aplt1.errorbar(trials, A, Aerr, fmt='o', linewidth=2, capsize=6)

Dplt.set_title("Group D (L = 100.00 ± 0.005 cm)")
Dplt.set_xlabel("Trials (trial 0 is theoretical)")
Dplt.set_ylabel("Peirod / s")
Dplt.errorbar(trials, D, Derr, fmt='o', linewidth=2, capsize=6)


Aplt2.set_title("Group A (θ = 10.0 ± 2.5 degrees)")
Aplt2.set_xlabel("Trials (trial 0 is theoretical)")
Aplt2.set_ylabel("Peirod / s")
Aplt2.errorbar(trials, A, Aerr, fmt='o', linewidth=2, capsize=6)

Eplt.set_title("Group E (θ = 70.0 ± 2.5 degrees)")
Eplt.set_xlabel("Trials (trial 0 is theoretical)")
Eplt.set_ylabel("Peirod / s")
Eplt.errorbar(trials, E, Eerr, fmt='o', linewidth=2, capsize=6)

plt.show()