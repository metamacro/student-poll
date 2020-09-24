import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

poll = pd.read_csv('data/student-poll-english.csv', quotechar='"', 
                   skipinitialspace=True, header=1, skiprows=0,
                   engine='python')

print(poll['dreamy-goals'])
