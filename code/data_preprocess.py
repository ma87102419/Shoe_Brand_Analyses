import pandas as pd
import numpy as np
df1 = pd.read_csv("/Users/ruby/Desktop/大三/三下/大數據與商業分析/final/91ForNTUDataSet/OrderData.csv")

#df1 = df1[df1['Status'].isin(["New", "Shipping", "Finish"])]
df1 = df1[df1['Status'].isin(["Finish"])]
#print(df1)
df2 = pd.read_csv("/Users/ruby/Desktop/大三/三下/大數據與商業分析/final/91ForNTUDataSet/MemberData.csv")
df2 = df2[["MemberCardLevel", "MemberID", "Birthday"]]
#print(df2.dtypes)
curr_date = pd.to_datetime('today').date()
df2['Birthday'] = pd.to_datetime(df2['Birthday'], format="%Y-%m-%d", errors='coerce')
df2['Birthday'] = pd.to_datetime(df2['Birthday']).dt.date
df2['age'] = (curr_date - df2["Birthday"]).dt.days // 365

#df2.loc[(df2.age > 100), 'age'] = 0
#df2['age'] = df2['age'].replace(np.nan, 35)
#df2['age'] = df2['age'].replace(np.nan, 1)
#df2.drop(df2[df2['age'] >= 80].index, inplace = True)
#df2.drop(df2[df2['age'] < 10].index, inplace = True)
id_level = dict(zip(df2["MemberID"], zip(df2["MemberCardLevel"], df2['age'])))
#print(id_level)
#exit()
level_amount = dict()
count = 0
for i in range(len(df1)):
    if i % 10000 == 0:
        print(i, flush=True)
    id = df1.iloc[i]["MemberID"]
    if id_level.get(id) == None:
        continue
    else:
        level = id_level.get(id)[0]
        #age = id_level.get(id)[1]
    amount = df1.iloc[i]["TotalSalesAmount"]
    good_quantity = df1.iloc[i]["Qty"]
    if level in level_amount:
        level_amount[level][0].add(id)
        level_amount[level][1] += amount
        level_amount[level][2] += good_quantity
        #level_amount[level][3] += age
    else:
        level_amount[level] = [set(id), amount, good_quantity]
    count += 1
    #print(level_amount[level][3])
print(count)

for i in level_amount:
    level_amount[i] = [level_amount[i][1], len(level_amount[i][0]), level_amount[i][1] / len(level_amount[i][0]),
                       level_amount[i][1] / level_amount[i][2]]

print(level_amount)
#總金額/總人數/平均消費總金額/平均商品價格
