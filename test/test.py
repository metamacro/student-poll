import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

poll = pd.read_csv('test.csv', sep=r'\s*,\s*',
                   header=0, encoding='ascii', engine='python')

print('Internship hourly wage:')
print('Mean:', poll['intern-hw'].mean())
print('Median', poll['intern-hw'].median())
print('Standard deviation:', poll['intern-hw'].std(ddof=1), end=2*'\n')

print('Regular hourly wage:')
print('Mean:', poll['reg-hw'].mean())
print('Median', poll['reg-hw'].median())
print('Standard deviation:', poll['reg-hw'].std(ddof=1))
