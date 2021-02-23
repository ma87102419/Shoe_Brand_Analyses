#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
from datetime import datetime


# In[2]:


date = [["2018", "07", 31], ["2018", "08", 31], ["2018", "09", 30], ["2018", "10", 31], ["2018", "11", 30], ["2018", "12", 31],
        ["2019", "01", 31], ["2019", "02", 28], ["2019", "03", 31], ["2019", "04", 30], ["2019", "05", 31], ["2019", "06", 30],
        ["2019", "07", 31], ["2019", "08", 31], ["2019", "09", 30], ["2019", "10", 31], ["2019", "11", 30], ["2019", "12", 31],
        ["2020", "01", 31], ["2020", "02", 28], ["2020", "03", 31], ["2020", "04", 30]]


# In[19]:


#2018-06
df1806 = pd.read_csv("/Users/pangyuan/Desktop/91ForNTUDataSet/123_new/search_2018-06-26.csv")
for i in range(27, 31):
    path = "/Users/pangyuan/Desktop/91ForNTUDataSet/123_new/search_2018-06-" + str(i) + ".csv"
    df = pd.read_csv(path)
    DF = pd.concat([df, df1806], axis = 0)


# In[20]:


for i in date:
    for j in range(1, i[2]):
        if j < 10:
            path = "/Users/pangyuan/Desktop/91ForNTUDataSet/123_new/search_" + str(i[0]) + "-" + i[1] + "-0" + str(j) + ".csv"
        else:
            path = "/Users/pangyuan/Desktop/91ForNTUDataSet/123_new/search_" + str(i[0]) + "-" + i[1] + "-" + str(j) + ".csv"
        df = pd.read_csv(path)
        DF = pd.concat([df, DF], axis = 0)


# In[5]:


order = pd.read_csv("/Users/pangyuan/Desktop/91ForNTUDataSet/OrderData.csv")


# In[30]:


all_search = DF.groupby(['uid']).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
DF_search_vip = DF.groupby(['uid']).size().reset_index(name='counts').sort_values(by='counts', ascending=False).head(15)


# In[26]:


all_search = DF.groupby(['uid']).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
DF_search_vip = DF.groupby(['uid']).size().reset_index(name='counts').sort_values(by='counts', ascending=False).head(15)#>1000次的顧客
search = list(DF_search_vip["uid"])
all_search[15:50]

DF.isna().sum() #181842
len(DF) #493713


# In[36]:


first = DF.loc[DF["uid"] == "jmPin5xB18Y61zGiw9xqSO3v5CW4eZqpq6oypBX%2F9BI%3D"]
first_list = list(first["pr"])


# In[7]:


VIP = pd.DataFrame()
for i in search:
    vip = order.loc[order["MemberID"] == i]
    VIP = pd.concat([vip, VIP])


# In[8]:


VIP["TotalPrice"].mean() #1220.575 也偏低
VIP_finish = len(VIP.loc[VIP["Status"]=="Finish"])/len(VIP) #0.275 非常低
print("搜尋VIP平均訂單價格：" + str(VIP["TotalPrice"].mean()))
print("搜尋VIP訂單完成率：" + str(VIP_finish))


# In[10]:


count = DF.groupby(['pr']).size().reset_index(name='counts').sort_values(by='counts', ascending=False).head(25)
count


# In[50]:


plt.figure(figsize=(15,3))
plt.bar(count["pr"], count["counts"],color = 'pink')


# In[53]:


search = input()
a = count.loc[count["pr"] == search]
print(a)


# In[55]:


order["Status"].unique()


# In[56]:


order.sort_values(by=['TradesDateTime']) #2013~202004 分析201901~202004


# In[57]:


l = []
for i in order["TradesDateTime"]:
    l.append(i)


# In[58]:


date = []
for i in l:
    date.append(i[0:7])


# In[59]:


order["Date"] = date


# In[61]:


order1901 = order.loc[order["Date"] == "2019-01"]#13123
order1902 = order.loc[order["Date"] == "2019-02"]#8661
order1903 = order.loc[order["Date"] == "2019-03"]#10565
order1904 = order.loc[order["Date"] == "2019-04"]#12338
order1905 = order.loc[order["Date"] == "2019-05"]#13149
order1906 = order.loc[order["Date"] == "2019-06"]#13057
order1907 = order.loc[order["Date"] == "2019-07"]#11614
order1908 = order.loc[order["Date"] == "2019-08"]#11397
order1909 = order.loc[order["Date"] == "2019-09"]#11244
order1910 = order.loc[order["Date"] == "2019-10"]#14515
order1911 = order.loc[order["Date"] == "2019-11"]#17119
order1912 = order.loc[order["Date"] == "2019-12"]#16261
order2001 = order.loc[order["Date"] == "2020-01"]#13815
order2002 = order.loc[order["Date"] == "2020-02"]#9350
order2003 = order.loc[order["Date"] == "2020-03"]#9688
order2004 = order.loc[order["Date"] == "2020-04"]#8481

O = ["1901","1902","1903","1904","1905","1906","1907","1908","1909","1910","1911","1912","2001","2002","2003","2004"]
C = [13123,8661,10565,12338,13149,13057,11614,11397,11244,14515,17119,16261,13815,9350,9688,8481]



# In[63]:


plt.figure(figsize=(10,3))
plt.plot(O,C,'s-',color = 'pink', label="TSMC")


# In[64]:


order1901_finish = len(order1901.loc[order["Status"]=="Finish"])
order1902_finish = len(order1902.loc[order["Status"]=="Finish"])
order1903_finish = len(order1903.loc[order["Status"]=="Finish"])
order1904_finish = len(order1904.loc[order["Status"]=="Finish"])
order1905_finish = len(order1905.loc[order["Status"]=="Finish"])
order1906_finish = len(order1906.loc[order["Status"]=="Finish"])
order1907_finish = len(order1907.loc[order["Status"]=="Finish"])
order1908_finish = len(order1908.loc[order["Status"]=="Finish"])
order1909_finish = len(order1909.loc[order["Status"]=="Finish"])
order1910_finish = len(order1910.loc[order["Status"]=="Finish"])
order1911_finish = len(order1911.loc[order["Status"]=="Finish"])
order1912_finish = len(order1912.loc[order["Status"]=="Finish"])
order2001_finish = len(order2001.loc[order["Status"]=="Finish"])
order2002_finish = len(order2002.loc[order["Status"]=="Finish"])
order2003_finish = len(order2003.loc[order["Status"]=="Finish"])
order2004_finish = len(order2004.loc[order["Status"]=="Finish"])


# In[74]:


order01_finish = order1901.loc[order["Status"]=="Finish"]
order02_finish = order1902.loc[order["Status"]=="Finish"]
order03_finish = order1903.loc[order["Status"]=="Finish"]
order04_finish = order1904.loc[order["Status"]=="Finish"]
order05_finish = order1905.loc[order["Status"]=="Finish"]
order06_finish = order1906.loc[order["Status"]=="Finish"]
order07_finish = order1907.loc[order["Status"]=="Finish"]
order08_finish = order1908.loc[order["Status"]=="Finish"]
order09_finish = order1909.loc[order["Status"]=="Finish"]
order10_finish = order1910.loc[order["Status"]=="Finish"]
order11_finish = order1911.loc[order["Status"]=="Finish"]
order12_finish = order1912.loc[order["Status"]=="Finish"]
order0120_finish = order2001.loc[order["Status"]=="Finish"]
order0220_finish = order2002.loc[order["Status"]=="Finish"]
order0320_finish = order2003.loc[order["Status"]=="Finish"]
order0420_finish = order2004.loc[order["Status"]=="Finish"]


# In[65]:


finish_rate = [order1901_finish/13123,order1902_finish/8661,order1903_finish/10565,order1904_finish/12338,order1905_finish/13149,order1906_finish/13057,order1907_finish/11614,order1908_finish/11397,order1909_finish/11244,order1910_finish/14515,order1911_finish/17119,order1912_finish/16261,order2001_finish/13815,order2002_finish/9350,order2003_finish/9688,order2004_finish/8481]


# In[66]:


finish = len(order.loc[order["Status"]=="Finish"])/len(order)
finish


# In[67]:


plt.figure(figsize=(10,3))
plt.plot(O,finish_rate,'s-',color = 'pink', label="TSMC")


# In[82]:


price1901 = order01_finish.loc[order["Date"] == "2019-01"]["TotalPrice"].mean()
price1902 = order02_finish.loc[order["Date"] == "2019-02"]["TotalPrice"].mean()
price1903 = order03_finish.loc[order["Date"] == "2019-03"]["TotalPrice"].mean()
price1904 = order04_finish.loc[order["Date"] == "2019-04"]["TotalPrice"].mean()
price1905 = order05_finish.loc[order["Date"] == "2019-05"]["TotalPrice"].mean()
price1906 = order06_finish.loc[order["Date"] == "2019-06"]["TotalPrice"].mean()
price1907 = order07_finish.loc[order["Date"] == "2019-07"]["TotalPrice"].mean()
price1908 = order08_finish.loc[order["Date"] == "2019-08"]["TotalPrice"].mean()
price1909 = order09_finish.loc[order["Date"] == "2019-09"]["TotalPrice"].mean()
price1910 = order10_finish.loc[order["Date"] == "2019-10"]["TotalPrice"].mean()
price1911 = order11_finish.loc[order["Date"] == "2019-11"]["TotalPrice"].mean()
price1912 = order12_finish.loc[order["Date"] == "2019-12"]["TotalPrice"].mean()
price2001 = order0120_finish.loc[order["Date"] == "2020-01"]["TotalPrice"].mean()
price2002 = order0220_finish.loc[order["Date"] == "2020-02"]["TotalPrice"].mean()
price2003 = order0320_finish.loc[order["Date"] == "2020-03"]["TotalPrice"].mean()
price2004 = order0420_finish.loc[order["Date"] == "2020-04"]["TotalPrice"].mean()

price = [price1901,price1902,price1903,price1904,price1905,price1906,price1907,price1908,price1909,price1910,price1911,price1912,price2001,price2002,price2003,price2004]


# In[83]:


plt.figure(figsize=(10,3))
plt.plot(O,price,'s-',color = 'pink', label="TSMC")


# In[80]:


price01 = order.loc[order["Date"] == "2019-01"]["TotalPrice"].mean()
price02 = order.loc[order["Date"] == "2019-02"]["TotalPrice"].mean()
price03 = order.loc[order["Date"] == "2019-03"]["TotalPrice"].mean()
price04 = order.loc[order["Date"] == "2019-04"]["TotalPrice"].mean()
price05 = order.loc[order["Date"] == "2019-05"]["TotalPrice"].mean()
price06 = order.loc[order["Date"] == "2019-06"]["TotalPrice"].mean()
price07 = order.loc[order["Date"] == "2019-07"]["TotalPrice"].mean()
price08 = order.loc[order["Date"] == "2019-08"]["TotalPrice"].mean()
price09 = order.loc[order["Date"] == "2019-09"]["TotalPrice"].mean()
price10 = order.loc[order["Date"] == "2019-10"]["TotalPrice"].mean()
price11 = order.loc[order["Date"] == "2019-11"]["TotalPrice"].mean()
price12 = order.loc[order["Date"] == "2019-12"]["TotalPrice"].mean()
price0120 = order.loc[order["Date"] == "2020-01"]["TotalPrice"].mean()
price0220 = order.loc[order["Date"] == "2020-02"]["TotalPrice"].mean()
price0320 = order.loc[order["Date"] == "2020-03"]["TotalPrice"].mean()
price0420 = order.loc[order["Date"] == "2020-04"]["TotalPrice"].mean()

price2 = [price01,price02,price03,price04,price05,price06,price07,price08,price09,price10,price11,price12,price0120,price0220,price0320,price0420]


# In[87]:


plt.figure(figsize=(10,3))
plt.plot(O,price2,'s-',color = 'pink', label="all order")
plt.plot(O,price,'s-',color = 'red', label="finish order")
plt.legend()
plt.show


# In[71]:


price1901 = order.loc[order["Date"] == "2019-01"]["TotalPrice"].mean()
price1902 = order.loc[order["Date"] == "2019-02"]["TotalPrice"].mean()
price1903 = order.loc[order["Date"] == "2019-03"]["TotalPrice"].mean()
price1904 = order.loc[order["Date"] == "2019-04"]["TotalPrice"].mean()
price1905 = order.loc[order["Date"] == "2019-05"]["TotalPrice"].mean()
price1906 = order.loc[order["Date"] == "2019-06"]["TotalPrice"].mean()
price1907 = order.loc[order["Date"] == "2019-07"]["TotalPrice"].mean()
price1908 = order.loc[order["Date"] == "2019-08"]["TotalPrice"].mean()
price1909 = order.loc[order["Date"] == "2019-09"]["TotalPrice"].mean()
price1910 = order.loc[order["Date"] == "2019-10"]["TotalPrice"].mean()
price1911 = order.loc[order["Date"] == "2019-11"]["TotalPrice"].mean()
price1912 = order.loc[order["Date"] == "2019-12"]["TotalPrice"].mean()
price2001 = order.loc[order["Date"] == "2020-01"]["TotalPrice"].mean()
price2002 = order.loc[order["Date"] == "2020-02"]["TotalPrice"].mean()
price2003 = order.loc[order["Date"] == "2020-03"]["TotalPrice"].mean()
price2004 = order.loc[order["Date"] == "2020-04"]["TotalPrice"].mean()

price = [price1901,price1902,price1903,price1904,price1905,price1906,price1907,price1908,price1909,price1910,price1911,price1912,price2001,price2002,price2003,price2004]


# In[ ]:




