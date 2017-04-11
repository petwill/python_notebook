import pandas as pd
import numpy as np
df = pd.read_csv('csvFile')
df.head()
#get columnx through index
# select single column
df = df[ df.columns[0] ]
# select multiple column, use iloc
#axis defaults to 0
#drop row, header does not count as 0
df = df.drop( [0], axis=0 )
#drop columns 0 1
df = df.drop( df.columns[ [0,1] ] axis=1)
#rename header
df = df.rename(columns={'original':'after'})
#Column name: age
#returns the column
df.age 
#replace all age with boolean
df.age==45
#only get rows with age attribet == 45
df = df[df.age==45]
# Purely integer-location based indexing for selection by position.
# Get row 3, 4
df.iloc[ [3,4] ]
# Purely label-location based indexer for selection by label.
# !! note that contrary to usual python slices, both the start and the stop are included!
df.loc[ 3:4, :]
# write dataframe to csv file without index column
df.to_csv('ans.csv', header=False)
