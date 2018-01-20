from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import pandas as pd
import numpy as np
import sys
import os
import matplotlib

print('Python version: '+sys.version)
print('Pandas version: '+pd.__version__)
print('Matplotlib version: '+matplotlib.__version__)

bp = os.path.join(os.path.expanduser('~'),'DataAnalysis','mecadata_analysis')

fp = os.path.join(bp,'area_info.csv')
da = pd.read_csv(fp,names=['area_id','area_name','area_url'])

fp = os.path.join(bp,'current_iteminfos.csv')
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
	areastr = 'area%d' % area_i
	df_area = df[df['area_id']==area_i]
	rs_area = df_area.groupby(['main_type'])['main_type'].count().reset_index(name='count').sort_values(['count'],ascending=False).head(10)
	#print da[da['area_id']==area_i]['area_name']
	#print rs_area[['main_type','count']].T
	#fig = rs_area.plot.bar(x=['main_type'],y=['count'],alpha=0.3,figsize=(10,4)).get_figure()
	#fig.savefig(os.path.join(bp,str(area_i)+'_area.png'))
	#plt.close(fig)
	rs_area.to_json(os.path.join(bp,'html','json',areastr+'_maintype.json'),orient='records')
	maintype_i = 0
	for maintype in rs_area['main_type']:
		maintype_i += 1
		maintypestr = 'maintype%d' % maintype_i
		df_main = df_area[df_area['main_type']==maintype]
		rs_main = df_main.groupby(['mid_type'])['mid_type'].count().reset_index(name='count').sort_values(['count'],ascending=False).head(10)
		rs_main.to_json(os.path.join(bp,'html','json',areastr+'_'+maintypestr+'_midtype.json'),orient='records')
		midtype_i = 0
		for midtype in rs_main['mid_type']:
			midtype_i += 1
			midtypestr = 'midtype%d' % midtype_i
			df_mid = df_main[df_main['mid_type']==midtype]
			rs_mid = df_mid.groupby(['sub_type'])['sub_type'].count().reset_index(name='count').sort_values(['count'],ascending=False).head(10)
			rs_mid.to_json(os.path.join(bp,'html','json',areastr+'_'+maintypestr+'_'+midtypestr+'_subtype.json'),orient='records')
			subtype_i = 0
			for subtype in rs_mid['sub_type']:
				subtype_i += 1
				subtypestr = '_%d' % subtype_i
				df_sub = df_mid[df_mid['sub_type']==subtype][['item_id','price_text','price']].sort_values(['price'],ascending=True)
				df_sub.to_json(os.path.join(bp,'html','json',areastr+'_'+maintypestr+'_'+midtypestr+'_subtype'+subtypestr+'.json'),orient='records')
