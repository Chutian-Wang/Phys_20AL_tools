import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y1 = [50,] * 5
y1err = [1,] * 5

y2 = [49.12, 49.36, 49.27, 49.38, 49.43]
y2err = [0.12,] * 5

# plot:
fig1, (ruler, caliper) = plt.subplots(1,2)
fig1.set_figwidth(10)
fig1.suptitle("Measuring my own thumb")

ruler.set_title("Using a plastic ruler")
ruler.set_xlabel("Trials")
ruler.set_ylabel("Mesurment / mm")
ruler.errorbar(x, y1, y1err, fmt='o', linewidth=2, capsize=6)

caliper.set_title("Using a digital caliper")
caliper.set_xlabel("Trials")
caliper.set_ylabel("Mesurment / mm")
caliper.errorbar(x, y2, y2err, fmt='o', linewidth=2, capsize=6)

y1 = [55, 53, 53, 52, 53]
y1err = [1,] * 5

y2 = [52.47, 51.58, 49.08, 50.74, 49.10]
y2err = [1.50,] * 5

fig2, (ruler2, caliper2) = plt.subplots(1,2)
fig2.set_figwidth(10)
fig2.suptitle("Measuring my peers thumb")

ruler2.set_title("Using a plastic ruler")
ruler2.set_xlabel("Trials")
ruler2.set_ylabel("Mesurment / mm")
ruler2.errorbar(x, y1, y1err, fmt='o', linewidth=2, capsize=6)

caliper2.set_title("Using a digital caliper")
caliper2.set_xlabel("Trials")
caliper2.set_ylabel("Mesurment / mm")
caliper2.errorbar(x, y2, y2err, fmt='o', linewidth=2, capsize=6)

plt.show()