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
# ddof = 1 since we use a sample (close to the whole population)
print('Standard deviation:', poll['intern-hw'].std(ddof=1), end=2*'\n')

print('Regular hourly wage:')
print('Min:', poll['reg-hw'].min())
print('Max:', poll['reg-hw'].max())
print('Mean:', poll['reg-hw'].mean())
print('Median', poll['reg-hw'].median())
print('Standard deviation:', poll['reg-hw'].std(ddof=1), end=2*'\n')

# internship hourly wage
poll['intern-hw'].value_counts().sort_index().plot(kind='bar')
plt.title('Internship hourly wage')
plt.xlabel('hourly wage [HRK]')
plt.ylabel('number of people')

# regular hourly wage
plt.figure()
poll['reg-hw'].value_counts().sort_index().plot(kind='bar')
plt.title('Regular hourly wage')
plt.xlabel('hourly wage [HRK]')
plt.ylabel('number of people')

# histograms for q0 - q9
# number of questions ranging from 0-10
# score ranges from 0-4, important-non important
titles = ["Wage importance", "Flexible work times", "Ability to work from home", 
          "Being given hardware and peripherals for work", "Free coffee, juice, fruits, snacks in general", 
          "Paid/cheaper meals", "Opportunity to progress and improve one's abilities",
          "Use technology as desired, if circumstances allow", 
          "The influence of the individual, the existence of a person who listens to your ideas and requirements", 
          "Possibility to continue working after completing an internship"]
nqs = 10
qs = ['q'+str(i) for i in range(nqs)]
binrange = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5]
hists = poll[qs].hist(layout=(5, int(nqs/5)), bins=binrange, rwidth=0.5, figsize=(5, 2))
for title, hist in zip(titles, hists.flatten()):
    hist.title.set_text(title)
    hist.set_ylabel('number of people')
    hist.set_xlabel('score')

# pie charts
# location
plt.figure()
locpie = poll['location'].value_counts().plot(kind='pie', autopct='%.2f%%',
                                              textprops={'color': 'w'})
locpie.legend()

# workspace
plt.figure()
workpie = poll['workspace'].value_counts().plot(kind='pie', autopct='%.2f%%',
                                              textprops={'color': 'w'})
workpie.legend()

plt.show()
