# Student poll

This student poll was made with the intent to get a better insight of student needs and expectations during their internships and employment.

The poll language is croatian.
All students tested have a minimum final grade of B, with most of them having a grade mean > 4.0, have finished at least one internship and have finished either their second or final bachelors year.

See [this google forms url for the poll.](https://docs.google.com/forms/d/e/1FAIpQLSelt9sSKwEIqqG4JofjQkJl9EAeL5sxRzlNUnaqLS2VIYKzjg/viewform?usp=sf_link)


## Poll results

A total of 21 students participated in the poll, which should include everyone that falls within the set constraints.

The collected data is present in the `data/` folder in the form of `*.csv` files.
Both a Croatian and English translation were made.

All graphs were made using the `process.py` script.
Used libraries:
- Pandas
- Matplotlib

### Desired internship hourly wage

| Min [HRK] | Max [HRK] | Mean [HRK] | Median [HRK]  | Standard deviation |
|:---------:|:---------:|:----------:|:-------------:|:------------------:|
|     20    |     40    |    30.7    |       30      |         4.06       |

![Internship hourly wage](./graphs/internship-hourly-wage.png)

### Desired regular hourly wage

| Min [HRK] | Max [HRK] | Mean [HRK] | Median [HRK]  | Standard deviation |
|:---------:|:---------:|:----------:|:-------------:|:------------------:|
|     30    |     70    |    45.5    |       45      |        8.87        |

![Regular hourly wage](./graphs/regular-hourly-wage.png)

A bigger standard deviation can be observed between the internship and regular hourly wage, this indicates more variance. 
It could be due to some students having more work experience than others and thus having higher salary expectations, some students perhaps have no work experience
so they could have given a lower estimate.

One student noted in the internship hourly wage field how just by having a paid internship it gives companies an edge over the others, since a lot of internships are unpaid. 

### Value of services and characteristics of the employer:

For this section, each question had an accompanying scoring system attached to it ranging from 0 to 4, indicating the value of the given service/characteristic of the employer.

For ease of visualization each question was shortened to the form of:
- q0 - Wage importance
- q1 - Flexible work times
- q2 - Ability to work from home
- q3 - Being given hardware and peripherals for work
- q4 - Free coffe, juice, fruits, snacks in general
- q5 - Paid/cheaper meals
- q6 - Opportunity to progress and improve one's abilities
- q7 - Use technology as desired, if circumstances allow
- q8 - The influence of the individual, the existence of a competent person who listens to your ideas and requirements
- q9 - Possibility to continue working after completing an internship

![Histograms of questions](./graphs/histograms-q0-q9.png)
