import pandas as pd
import numpy as np

'''SOLVED!
1. how to use pandas group by aggregate multiple columns
https://stackoverflow.com/questions/48768650/groupby-sum-and-count-on-multiple-columns-in-python
https://stackoverflow.com/questions/14529838/apply-multiple-functions-to-multiple-groupby-columns
'''
df = pd.DataFrame(
    {
        "AA": [1, 1, 2, 2],
        "BB": [1, 2, 3, 4],
        "CC": ['A','A','A','B'],
        "DD": [0.362838, 0.227877, 1.267767, -0.562860],
    }
)
df_sum = df.groupby(['AA','CC'])[['BB','DD']].sum()
df_mean = df.groupby(['AA','CC'])[['BB','DD']].mean()
print(df_sum, df_mean)

'''SOLVED!
2. How to merge two groupby dataframe on pandas?
https://stackoverflow.com/questions/52425332/merge-pandas-groupby-objects'''
df_new = pd.concat([df_sum, df_mean],axis=1)
print(df_new)

# testdf.reset_index().to_csv('CCCC_output_summary.txt', sep='\t', header=True, index=False)

'''SOLVED!
3. How to write groupby dataframe into csv?
https://stackoverflow.com/questions/35025917/python-pandas-writing-groupby-output-to-file'''
df_new.reset_index().to_csv('test.csv', sep='\t', header=True, index=False)

'''
4. specific match with file: 从其他文件中读取相应的数据，如果指定的列中含有该数据，则挑选出来'''


''' Solved!
5. pandas choose range and a specific column - there are mulitipule columns within the range and specific column 
https://stackoverflow.com/questions/66719246/slicing-columns-from-a-dataframe-with-range-and-specific-columns-selected'''
print(df.iloc[:,list(range(0,2))+[-1]])

'''Solved!
6. drop nan value
https://stackoverflow.com/questions/22551403/python-pandas-filtering-out-nan-from-a-data-selection-of-a-column-of-strings'''

'''
Solved!!!
7. Reshape pivot table
https://pandas.pydata.org/docs/user_guide/reshaping.html
'''
# 这个解决方案非常好用。由于planning和其他的数据组都只会给定数据分析的结果，这个结果表往往是由透视表改装的。如果要对该透视表的数据重新分析或者画图，则可以使用reshap透视表的方法
# 可以用于planning的continuation, attainment and progression 表

'''Solved!!!
8. using the row where a given text located as the column name and then delete this row
https://stackoverflow.com/questions/26147180/convert-row-to-column-header-for-pandas-dataframe
'''
df = pd.DataFrame({"A": [1, 'a',2 , 3], "B": [4,'b', 5, 6], "C": [7,'c', 8, 9]})
columnindex = df.index[df['C'].isin(['c'])].tolist()[0]
df.rename(columns=df.loc[[columnindex]].to_dict('records')[0], inplace=True)
df = df.drop(columnindex)

'''Solved!!!
9. fill null values in mutipule columns based on another column records
https://stackoverflow.com/questions/57303445/fill-na-in-multiple-columns-with-values-from-another-column-within-the-pandas-da
'''
df = pd.DataFrame({"A": [np.nan, 'a',2 , 3], "B": [np.nan,'b', np.nan, 6], "C": [7,'c', 8, 9]})
df[['B','A']] = df[['B','A']].T.fillna(df['C']).T

'''Solved!!!
10. how to change the multipule columns name?
https://stackoverflow.com/questions/38101009/changing-multiple-column-names-but-not-all-of-them-pandas-python
'''
df = pd.DataFrame({"A": [np.nan, 'a',2 , 3], "B": [np.nan,'b', np.nan, 6], "C": [7,'c', 8, 9]})
oldname = df.columns[[0,2]]
newname = ['AC', 'BD']
df.rename(columns=dict(zip(oldname, newname)), inplace=True)

'''Solved!!!
11. how to compare the data with the previous year?
https://stackoverflow.com/questions/48347497/pandas-groupby-multiple-fields-then-diff
'''
df = pd.DataFrame({"A": ['Uni', 'Uni', 'Benchmark', 'Benchmark'], "B": [2022, 2021, 2022, 2021], "C": [76.82,75.43, 79.03,80.2], "D":['A', 'B', 'A', 'B']})
df = df.sort_values(by=['A','B'])
df['diff'] = df.groupby(['A'])['C'].diff()

'''Solved!!!
12. how to compare the data with the benchmark?
'''
df = pd.DataFrame({"A": ['Uni', 'Uni', 'Benchmark', 'Benchmark'], "B": [2022, 2021, 2022, 2021], "C": [76.82,75.43, 79.03,80.2], "D":['A', 'B', 'A', 'B']})
list1 = [x for x in df['A'].unique() if x.lower() in ['benchmark', 'threshold']]
df2 = df.loc[df['A'].isin(list1),:]
df3 = df.merge(df2, how = 'outer', on = ['B', 'D'], suffixes=('', '_bench'))
df3['benchdiff'] = df3['C'] - df3['C_bench']
df = df3.iloc[:,[0,1,2,3,-1]]

'''Solved!!!
13. how to build radar chart using matplotlib
https://www.python-graph-gallery.com/391-radar-chart-with-several-individuals
https://www.pythoncharts.com/matplotlib/radar-charts/
'''
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# Set data
df = pd.DataFrame({'name': ['var1','var2','var3','var4','var1','var2','var3','var4'],'group': ['A', 'A', 'A', 'A', 'B','B','B','B'],
        'value': [29, 10, 9, 34, 8, 39, 23, 24]})

# ------- PART 1: Create background
 
# number of variable
categories= df.loc[df['group']=='A','name'].tolist()
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,40)

# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
def add_to_radar(group, color):
  values = df.loc[df['group']== group,'value'].tolist()
  values += values[:1]
  ax.plot(angles, values, color=color, linewidth=1, label= group)
  ax.fill(angles, values, color=color, alpha=0.25)

# Add each group to the chart.
add_to_radar('A', '#0009B8')
add_to_radar('B', '#DBC3D6')

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Show the graph
plt.show()

'''Solved!!!
14. how to move the element in list to specific order
https://stackoverflow.com/questions/1014523/simple-syntax-for-bringing-a-list-element-to-the-front-in-python
'''
l3 = ['University of Huddersfield', 'benchmark', 'A503', 'T115']
l3.insert(1,l3.pop(-1))

'''Solved!!!
15. how to select the specific columns from dataframe'''
df = pd.DataFrame({'name': ['var1','var2','var3','var4','var1','var2','var3','var4'],'group': ['A', 'A', 'A','A', 'B','B','B','B'],
                'value': [29, 10, 9, 34, 8, 39, 23, 24]})
colist = df.columns.tolist()
colist.pop(-2)
df = df.loc[:,colist]