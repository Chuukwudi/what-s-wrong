import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()
labels = list(df.columns)
for i in range(6):
    labels[i] = labels[i].replace(' ', '_')

df.columns = labels

df.head()


def mean_quality_rating(thing):
    median = df.thing.median()
    for i, thing in enumerate(df.thing):
        if thing >= median:
            df.loc[i, 'thing'] = 'high'
        else:
            df.loc[i, 'thing'] = 'low'
    df.groupby('thing').quality.mean()


mean_quality_rating(alcohol)
mean_quality_rating(pH)
mean_quality_rating(residual_sugar)
mean_quality_rating(citric_acid)
