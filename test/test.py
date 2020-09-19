import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

poll = pd.read_csv('test.csv', sep=r'\s*,\s*',
                   header=0, encoding='ascii', engine='python')

print('Internship hourly wage:')
print('Mean:', poll['intern-hw'].mean())
print('Median', poll['intern-hw'].median())
# ddof = 1 since we use a sample not the whole population
print('Standard deviation:', poll['intern-hw'].std(ddof=1), end=2*'\n')

print('Regular hourly wage:')
print('Mean:', poll['reg-hw'].mean())
print('Median', poll['reg-hw'].median())
print('Standard deviation:', poll['reg-hw'].std(ddof=1), end=2*'\n')

# Spearman's correlation since we don't know the type of correlation
print('Spearman hourly-regular correlation:', 
      stats.spearmanr(poll['intern-hw'], poll['reg-hw']))

# visualize the data distribution
hists = poll[['intern-hw', 'reg-hw']].hist(color='#3377ff')

titles = ['Internship hourly wage [kn]', 'Regular hourly wage [kn]']
for ax, title in zip(hists.flatten(), titles):
    ax.title.set_text(title)

plt.show()
