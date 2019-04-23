import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

read=r'C:\Users\Claude\Desktop\NKUST\碩一(下)\服務決策數據\HW3\網路書局.csv'
rv=open(read)
data=pd.read_csv(rv)

for  i  in  range(1,199):
          name=data.columns[i]
          data[name].replace(1,name,inplace=True) ##編碼轉換中文

set=[]                                   ##去除每筆無購買的部分
record = []
for i in range(0,200):
      for j in range(1,199):
          if data.values[i,j]== 0:
               continue
          record.append(data.values[i,j])
      set.append(record)
      record=[]
#print(set)
association_rules=apriori(set[:3],min_support=0.1,min_confidence=0.1,min_lift=1,min_length=2)
association_results = list(association_rules)
print(association_results[100])
#DATA=pd.DataFrame(association_results)








# for item in association_results:
#    pair = item[0]
#    items = [x for x in pair]
#    print("Rule: " + items[0] + " -> " + items[1])
#    print("Support: " + str(item[1]))
#    print("Confidence: " + str(item[2][0][2]))
#    print("Lift: " + str(item[2][0][3]))
#    print("=====================================")
