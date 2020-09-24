import pandas as pd
import matplotlib.pyplot as plt

poll = pd.read_csv('data/student-poll-english.csv', quotechar='"', 
                   skipinitialspace=True, header=1, skiprows=0,
                   engine='python')

print('Internship hourly wage:')
print('Min:', poll['intern-hw'].min())
print('Max:', poll['intern-hw'].max())
print('Mean:', poll['intern-hw'].mean())
print('Median', poll['intern-hw'].median())
# ddof = 1 since we use a sample not the whole population
print('Standard deviation:', poll['intern-hw'].std(ddof=1), end=2*'\n')

print('Regular hourly wage:')
print('Min:', poll['reg-hw'].min())
print('Max:', poll['reg-hw'].max())
print('Mean:', poll['reg-hw'].mean())
print('Median', poll['reg-hw'].median())
print('Standard deviation:', poll['reg-hw'].std(ddof=1), end=2*'\n')

poll['intern-hw'].value_counts().sort_index().plot(kind='bar')
plt.title('Internship hourly wage')
plt.xlabel('hourly wage [HRK]')
plt.ylabel('number of people')

plt.figure()
poll['reg-hw'].value_counts().sort_index().plot(kind='bar')
plt.title('Regular hourly wage')
plt.xlabel('hourly wage [HRK]')
plt.ylabel('number of people')

# histograms for q0 - q9
# number of questions ranging from 0-10
# score ranges from 0-4, important-non important
nqs = 10
qs = ['q'+str(i) for i in range(nqs)]
binrange = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5]
hists = poll[qs].hist(layout=(5, int(nqs/5)), bins=binrange, rwidth=0.5, figsize=(5, 2))
for hist in hists.flatten():
    hist.set_ylabel('number of people')
    hist.set_xlabel('score')

# pie charts
# location
plt.figure()
locpie = poll['location'].value_counts().plot(kind='pie', autopct='%.2f%%',
                                              textprops={'color': 'w'})
locpie.legend()

# workspace
# workspace
plt.figure()
workpie = poll['workspace'].value_counts().plot(kind='pie', autopct='%.2f%%',
                                              textprops={'color': 'w'})
workpie.legend()

plt.show()
