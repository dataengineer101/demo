# filename = r"C:\Users\mark\PycharmProjects\demo_new\data.csv"
# with open(filename) as file_object:
#    for line in file_object:
#     # print(line)
#     # print(line.strip('\n'))
#     # print(line.split(","))
#     # print(line.strip().split(","))
#
#     # line = line.replace(',\n', '')
#     # print(line)
#
#     x = line.splitlines()
#     # x = line.replace('\r\n', '')
#     # x = x.replace("\r", "")
#     # x = x.replace("\n", "")
#
#     print(x)
#
#     git stash
import pandas as pd
import matplotlib.pyplot as plt

# url2 = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1273/datasets/df2.csv'

filename = r"C:\Users\mark\PycharmProjects\demo_new\data.csv"
df = pd.read_csv(filename, sep = ',')

# print(df.to_string())

df.dropna(how='all', inplace=True)    # drop if all values in the row are nan

# # rename columns
df.rename(columns = {"Month":'Month_Year'}, inplace=True)
#
# # Similarly, to get rid of trailing whitespace:
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



# # Print out df2_tidy
# print(df2_melted)
#
#

#

#


