import pandas as pd
import numpy as np

data = pd.read_csv('project/train.csv').values
Y = data[:, -1]
X = data[:, :-1]

