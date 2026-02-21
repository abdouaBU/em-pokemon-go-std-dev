import numpy as np
from scipy.stats import multivariate_normal
import pandas as pd
import json

# constants
EPSILON: float = 1e-12
DELTA: float = 1e-9

# round10k(num) rounds num to the nearest 10,000s place (up to 4 decimal places)
def round10k(num):
    return float(int(num*10000))/10000


# Load in JSON file
filepath = "pokemon_data.json"
with open(filepath, 'r') as file:
    data = json.load(file)

print(data)


filepath = "pokemon_data.json"
with open(filepath, 'r') as file:
    data = json.load(file)
x = 1
for key in data:
    print(x, key, str(data[key]["weight"])+" kg")
    x+=1


df = pd.DataFrame(data).T
print(df)


lightest = 0.25*df["weight"].min()
heaviest = 2.5*df["weight"].max()
shortest = 0.25*df["height"].min()
tallest = 2.5*df["height"].max()

rand = np.random.rand()

print(f"The shortest Pokemon is {shortest} meters tall.")
print(f"The tallest Pokemon is {tallest} meters tall.")
print(f"The lightest Pokemon is {lightest} kg.")
print(f"The heaviest Pokemon is {heaviest} kg.")

val = rand*(heaviest-lightest)+lightest
print(f"Sample weight: {round10k(val)} kg")