import pandas as pd
data ={
    "students":['sahil', 'om', 'rahul', 'amey', 'raj'],
    "marks":[45, 91, 60, 96, 99],
    "rank":[5, 3, 4, 2, 1]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[3])