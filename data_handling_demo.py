''' Short demo to demonstrate file handling, data wrangling & plots '''

import pandas as pd
import matplotlib.pyplot as plt

filename = r"C:\Users\mark\PycharmProjects\demo_new\data.csv"
df = pd.read_csv(filename, sep = ',')

# print out the full contents of thee df using to_string
# print(df.to_string())

# drop if all values in the row are nan
df.dropna(how='all', inplace=True)

# rename column month to month_year
df.rename(columns = {"Month":'Month_Year'}, inplace=True)

# drop the notes column
df = df.drop('Notes',1)

df['Month_Year'] = df['Month_Year'].replace(['Mar-19 (r)'], 'Mar-19')
df['Month_Year'] = df['Month_Year'].replace(['Apr-19 (p)'], 'Apr-19')

print(df.to_string())

# # Create a line plot
lines = df.plot.line()
plt.show()

# save  file
pd.set_option('precision', 0)
df.to_csv(r"C:\Users\mark\PycharmProjects\demo_new\data_cleaned.csv", encoding="utf-8",index=False)






