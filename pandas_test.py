from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import os
import matplotlib

print('Python version: '+sys.version)
print('Pandas version: '+pd.__version__)
print('Matplotlib version: '+matplotlib.__version__)

fp = os.path.join(os.path.expanduser('~'),'DataAnalysis','mecadata','area_info.csv')
da = pd.read_csv(fp,names=['area_id','area_name','area_url'])

fp = os.path.join(os.path.expanduser('~'),'DataAnalysis','mecadata','items_iteminfo_4.csv')
df = pd.read_csv(fp)
#price = df['price']
#count, division = np.histogram(price,bins=[i for i in range(0,1000,2)],range=(0,100))
#print count
#print division
#print "min: %10.2f, max: %10.2f" % (price.min(),price.max())
### plot the histogram of prie ###
#plt.hist(price,bins=[i for i in range(price.min(),50000,100)])
#plt.savefig(os.path.join(os.path.expanduser('~'),'DataAnalysis','mecadata','items_iteminfo_4_price_histogram.png'))

### count the main_type of each area and print out the top 10 of them ###
for area_i in range(1,48):
	df_area = df[df['area_id']==area_i]
	rs_area = df_area.groupby(['main_type'])['main_type'].count().reset_index(name='count').sort_values(['count'],ascending=False).head(10)
	print da[da['area_id']==area_i]['area_name']
	print rs_area[['main_type','count']].T
