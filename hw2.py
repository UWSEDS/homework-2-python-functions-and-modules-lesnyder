
"""Create the function test_create_dataframe that takes as input: (a) a pandas DataFrame and (b) a list of column names. The function returns True if the following conditions hold:

        The DataFrame contains only the columns that you specified as the second argument.
        The values in each column have the same python type
        There are at least 10 rows in the DataFrame."""

import pandas as pd

<<<<<<< HEAD
link =  "https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(link)

def test_create_dataframe(df, column_names):
        condition1 =  column_names== list (df.columns)
        rows = len(df)
        condition3 = rows  >= 10
        condition2 = True
        for col in df:
                first_type = type(df[col][0])


