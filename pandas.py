import pandas as pd
import numpy as np
df = pd.read_csv('csvFile')
df.head()
#get columnx through index
df = df[ [1, 2, 5] ]
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
