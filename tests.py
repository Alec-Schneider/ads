import ads
import pandas as pd
v1 = ads.merge_files([r'C:\Users\afs95\MyPython\Baseball\data\2019\2019Standard.csv',
                r'C:\Users\afs95\MyPython\Baseball\data\2019\2019Advanced.csv'],
                on=['playerid', 'Name'])

v2 = ads.merge_files([r'C:\Users\afs95\MyPython\Baseball\data\2019\2019Standard.csv',
                r'C:\Users\afs95\MyPython\Baseball\data\2019\2019Advanced.csv'],
                on=['playerid', 'Name'], chunksize=250)

nulls = pd.concat([v1.isnull().sum(), v2.isnull().sum()], axis=1)
check = (v1 == v2).sum()
print(nulls)
print(check)

