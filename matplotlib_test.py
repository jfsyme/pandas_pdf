# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 01:06:09 2021

@author: James
"""


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# link to gapminder data
data_url = 'http://bit.ly/2cLzoxH'
# read data from url as pandas dataframe
gapminder = pd.read_csv(data_url)

gapminder.columns = ['country','year','population',
                     'continent','life_exp','gdp_per_cap']

gapbrazil = gapminder[gapminder['country']=='Brazil']
gapbrazil = gapbrazil[['year','life_exp','gdp_per_cap']]

gapbrazil['year'] = gapbrazil['year'].astype('int64')
gapbrazil['life_exp'] = gapbrazil['life_exp'].round(decimals=1)
gapbrazil['gdp_per_cap'] = gapbrazil['gdp_per_cap'].round(decimals=0)

#create a plotting function
def plotGraph(X,Y):
      fig = plt.figure()
      plt.plot(X, Y, color='red')
      return fig

#define plots
plot1 = plotGraph(gapbrazil.year, gapbrazil.gdp_per_cap)
plot2 = plotGraph(gapbrazil.year, gapbrazil.life_exp)
#plot3 = plotGraph(tempDLstats_2, tempDLlabels_2)

#plot table
plot3, ax = plt.subplots()
plot3.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.table(cellText=gapbrazil.values, colLabels=gapbrazil.columns, loc='center')


pp = PdfPages('foo.pdf')
pp.savefig(plot1)
pp.savefig(plot2)
pp.savefig(plot3)
pp.close()