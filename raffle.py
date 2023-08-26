import pandas as pd
df = pd.read_csv('list.csv')
if df.size != 0 :
    sample = df.sample()
    print(sample)
    df = df.drop(sample.index, axis=0)
    df = df.to_csv('list.csv',index = False)
else :
    print('End of Line')