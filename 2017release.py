import pandas as pd 
import matplotlib.pyplot as plt
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
f=pd.read_excel('2017Release_5.xlsx')
f
sex = f.groupby('性別').count()
sex
label = 'Female','Male'
size = [sex.iloc[0]['車號'],sex.iloc[1]['車號']]
print(size)
plt.pie(size,labels=label,autopct='%1.1f%%')
