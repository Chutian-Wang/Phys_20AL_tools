import numpy as np
import matplotlib.pyplot as plt

trials = [1, 2, 3, 4, 5]

A = [0.2280, 0.2130, 0.2030, 0.1910, 0.1821]
Aerr = [0.0179, ] * 5
B = [0.2477, 0.2263, 0.2281, 0.2111, 0.1921]
Berr = [0.0208, ] * 5
C = [0.2198, 0.2180, 0.2244, 0.2170, 0.2212]
Cerr = [0.0029, ] * 5

fig1, (Aplt, Bplt, Cplt) = plt.subplots(1, 3, sharey=True,)

fig1.set_figwidth(15)
fig1.suptitle("Measurements of tan(θ) With Experimental Setup")

Aplt.set_title("m = 100g, Plastic/Paper")
Aplt.set_xlabel("Trials")
Aplt.set_ylabel("tan(θ)")
Aplt.errorbar(trials, A, Aerr, fmt='o', linewidth=2, capsize=6)

Bplt.set_title("m = 500g, Plastic/Paper")
Bplt.set_xlabel("Trials")
Bplt.set_ylabel("tan(θ)")
Bplt.errorbar(trials, B, Berr, fmt='o', linewidth=2, capsize=6)

Cplt.set_title("m = 500g, Plastic/Parchment Paper")
Cplt.set_xlabel("Trials")
Cplt.set_ylabel("tan(θ)")
Cplt.errorbar(trials, C, Cerr, fmt='o', linewidth=2, capsize=6)

plt.show()