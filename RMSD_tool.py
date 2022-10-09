import math

print("Using RMSD = sqrt( sum( (xi - xbar)^2 ) / (N - 1) )")
inputstr = input("Input data below, separated by a space.\n")
try:
    dataset = [float(x) for x in inputstr.split()]
    if len(dataset) == 1:
        print("Dataset size = 1, abort.")
        exit(0)
except:
    print("An error occured. Check your input.")
    exit(0)
xbar = sum(dataset) / len(dataset)
rmsd = math.sqrt(sum([(x - xbar) ** 2 for x in dataset]) / (len(dataset) - 1))
print(f"\nDataset avg. {xbar}")
print(f"RMSD         {rmsd}")
print(f"sigma / xbar {rmsd / xbar}")
print("Dataset------------------------")
for x in enumerate(dataset):
    print(f"{x[0]}            {x[1]}")