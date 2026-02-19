# import numpy as np
# import random
# import pandas as pd

# from sklearn.mixture import GaussianMixture

ct=0
for i in range(1, 5):
    for j in range(1, i+1):
        for k in range(1, j+1):
            for l in range(1, k+1):
                ct+=l**1.005

print(ct)